from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from gensim import corpora,models
import gensim
import nltk
import re
import json
import os
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def load_corpus(file_path):

    '''
    Args: folder path
    Returns: id list and corresponding content list
    '''

    restaurant_id_list = []
    restaurant_content_list = []

    with open(file_path, 'r', encoding="utf-8") as f:
        restaurant = json.load(f)
        for k,v in restaurant.items():
            restaurant_id_list.append(k)
            restaurant_content_list.append(v)
    f.close()

    return restaurant_id_list, restaurant_content_list


def clean_text(doc_set):

    '''
    Args: a list of documents
    Returns: a list of cleaned text
    '''

    cleaned_texts = []

    for doc in doc_set:

        # clean and tokenize document string
        raw_text = doc.lower()
        raw_text = re.sub(r"[^\w\s]", "", raw_text)
        tokens = nltk.word_tokenize(raw_text)

        # remove stop words from tokens
        stop = stopwords.words("english")
        cleaned_tokens = [token for token in tokens if token not in stop]

        # add tokens to list
        cleaned_texts.append(cleaned_tokens)

    return cleaned_texts


def training_lda(cleaned_texts, n_topics):

    '''
    Args: a list of cleaned text
    Returns: a lda model
    '''

    dictionary = corpora.Dictionary(cleaned_texts)
    corpus = [dictionary.doc2bow(text) for text in cleaned_texts]

    # need to tune parameter here
    ldamodel = gensim.models.ldamulticore.LdaMulticore(corpus, num_topics=n_topics, id2word = dictionary, workers = 15, chunksize = 20000, passes=10, iterations=400, eval_every = 500)

    return ldamodel, corpus, dictionary


def save_results(ldamodel, corpus, restaurant_id_list, n_topics):

    '''
    Export LDA results to a file (topic collection and topic distributions of docs)
    Args: lda model, corpus, the list of news IDs, number of topics
    Returns: none

    '''

    # 1. get topic collections of documents
    topic_dictionary = {} # initialize a dictionrary of <topicid, [docid, docid, ..]>
    for i in range(0, n_topics):
        topic_dictionary[i] = []

    for i in range(0,len(corpus)):
        # get the topic with the highest probability
        most_probable_topic = ldamodel[corpus[i]][0][0]
        # add to the list
        topic_dictionary[most_probable_topic].append(restaurant_id_list[i])

    # save to a json file
    with open("/pine/scr/j/i/jiaming/yelp/scripts/topic_collection.json", 'w') as f:
        json.dump(topic_dictionary,f)
    f.close()

    # 2. get document distribution probability of topics
    doc_prob_distribution = {}
    for i in range(0,len(corpus)):
        doc_prob_distribution[restaurant_id_list[i]] = ldamodel[corpus[i]]

    # save to a json file
    for k,v in doc_prob_distribution.items():
        file_name = "/pine/scr/j/i/jiaming/yelp/lda_prob/" + k + ".txt"
        with open(file_name, 'w') as f:
            for item in v:
                f.write(str(item))
                f.write("\n")
        f.close()


def main():
    restaurant_id_list, restaurant_content_list = load_corpus("/pine/scr/j/i/jiaming/yelp/scripts/restaurant.keywords.json")
    cleaned_texts = clean_text(restaurant_content_list)
    n_topics = 50
    ldamodel, corpus, dictionary = training_lda(cleaned_texts, n_topics)
    save_results(ldamodel, corpus, restaurant_id_list, n_topics)

if __name__ == "__main__":
    main()






