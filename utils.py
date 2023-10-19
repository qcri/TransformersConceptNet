import random
import sys
import json
import os
import argparse

from collections import Counter, defaultdict
from typing import Dict, List

def cluster_read(fname):
    """
    Given a txt file containing the latent concepts of a corresponding layer, The
    function loads all data in the file and returns it in form of lists. These lists 
    will be then used to create mappings between clusters, words, and sentences 

    Parameters
    ----------
    fname : str
        Path to where the latent concepts data is stored for a corresponding
        layer (Usually saved in a .txt file).

    Returns
    -------

    words: List
        A list of words corresponding to latent concepts of the passed data.
        Each word will be associated with a latent concept (also called a cluster)
    words_idx: List
        A list of word indices corresponding to occurance location of each word
        in the sentences.
    cluster_idx: List
        A list of cluster ids corresponding to the data passed. Each layer will
        have a group of clusters and each cluster contains a group of words
    sent_idx: List
        A list of sentence ids corresponding to which sentences the concept appears in
    """
    words = []
    words_idx = []
    cluster_idx = []
    sent_idx = []
    with open(fname) as f:
        for line in f:
            line  = line.rstrip('\r\n')
            parts = line.split("|||")
            words.append(parts[0])
            cluster_idx.append(int(parts[4]))
            words_idx.append(int(parts[3]))
            sent_idx.append(int(parts[2]))
    return words, words_idx, sent_idx, cluster_idx

def read_cluster_data(fname):
    """
    Given a .txt file corresponding to latent concepts of a layer, the function
    returns a mapping between cluster ids and words. The words corresponding to
    each cluster are returned in a list

    Parameters
    ----------
    fname : str
        Path to where the latent concepts data is stored for a corresponding
        layer (Usually saved in a .txt file).

    Returns
    -------

    clusterToWords: Dict
        A mapping (or dictionary) between cluster and words. The keys of the dictionary
        are clusters, and the corresponding values are words corresponding to that cluster.
      
    """
    clusterToWords  = defaultdict(list)
    words, words_idx, sent_idx, cluster_idx = cluster_read(fname)
    for i, elem in enumerate(cluster_idx):
        cluster = "c" + str(cluster_idx[i])
        clusterToWords[cluster].append(words[i])
    return clusterToWords


def map_clusters_to_sentences(fname: str): 

    """
    Given a .txt file corresponding to a latent concepts of a layer, the function returns a mapping between 
    cluster ids and sentence ids. 

    Parameters 
    ------------
    fname : str 
        Path to where the latent concepts data is stored for a corresponding layer. 
        (Usually stored in a .txt file)
    
    Returns
    ------------

    clusterToWords: Dict 

        A mapping (dictionary) between cluster and words. The keys of the dictionary are clusters, 
        and the corresponding values are words corresponding to that cluster. 
    """

    cluster_to_sent_ids = defaultdict(list) 
    words, words_idx, sent_idx, cluster_idx = cluster_read(fname)
    for i, elem in enumerate(cluster_idx): 
        cluster = "c" + str(cluster_idx[i])
        cluster_to_sent_ids[cluster].append(sent_idx[i])
    return cluster_to_sent_ids


def get_frequency_counts(clusterToWords):
    """
    given a mapping between clusters and word ids, the functions returns another
    mapping between clusters and counts of words in each cluster
    Parameters
    ----------
    clusterToWords : Dict
        A mapping between cluster ids and words


    Returns
    -------
    result: Dict
        A mapping between cluster ids and word counts for each cluster

    """
    result = {}
    for cluster in clusterToWords:
        count = Counter(clusterToWords[cluster])
        result[cluster] = list(count.items())
    return result



def read_annotations(path): 
    with open(path, "r") as reader: 
        labels = json.load(reader)
    return labels



def read_txt_file(path: str) -> List: 
    elements = []
    with open(path, 'r') as reader: 
        for line in reader: 
            elements.append(line.strip())
    return elements


def read_sentences(path_to_sentences: str) -> List: 
    """READING THE SENTENCES FILE. USED THE CODE DEVELOPED FOR THE TCAV PROJECT

    Parameters
    ----------
    path_to_sentences: str :
        

    Returns
    -------

    """
    lines = []
    with open(path_to_sentences, "r") as reader: 
        data = json.load(reader) 
        for line in data: 
            l = line.rstrip('\r\n')
            lines.append(l) 
    return lines


def load_all_cluster_data(clusters_path): 
    clusters = defaultdict(list)
 
    with open(clusters_path) as fp:
        for line_idx, line in enumerate(fp):
            token, _, sentence_idx, token_idx, cluster_idx = line.strip().rsplit("|||")

            sentence_idx = int(sentence_idx)
            token_idx = int(token_idx)
            cluster_idx = int(cluster_idx)

            clusters["c" + str(cluster_idx)].append((token, sentence_idx, token_idx))
    return clusters



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="path to the txt file where the clusters are stored")
    parser.add_argument("-c", "--cluster", help="Cluster For Which we want to return the words")
    args = parser.parse_args()

    cluster_to_words = read_cluster_data(args.file)

    print(cluster_to_words[args.cluster])





if __name__ == '__main__':
    main()
