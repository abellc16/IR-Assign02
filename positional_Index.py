# Authors:    Camby Abell, Tim Gwaltney, Jamie Rios
# Assignment: Programming Assignment 02 - Creating a postional index
# Class:      CSCI 4130
# Filename:   positional_Index.py

###############################################################
#                HOW TO RUN THE PROGRAM:
#
# 1. When prompted to enter a corpus, enter 'corpus'
# 2. You may then enter a single term search, such as 'east'
#
###############################################################

import math
import os
import re
import string
import sys
from nltk.stem import *
from nltk.corpus import *
import numpy
from collections import Counter
from collections import defaultdict


stemmer = PorterStemmer()
pl = open("PostingsList.txt", "w")
piFile = open("Positional.txt", "w")


# Takes a text as a parameter
# Removes punctuation
# Makes everything lowercase
# Handles stemming/lemmatization
def normalize_text(text):
    text_norm = re.findall('[a-z]+', text)
    norm_text = []
    for token in text_norm:
        norm_text.append(stemmer.stem(token))
    return norm_text


# Creates positional index
def create_positional_index(words, i):
    index = {}
    for idx, word in enumerate(words):
        if not word in index:
            index[word] = [i,idx]
        else: index[word].append(idx)
    return index


# Prompt user for query
def query_prompt():
    query = input("Specify query: ")
   # print("Your query: ", query)
    return query


def dictionary(mydict,tokens):
    for word in tokens:
        if word not in mydict:
            mydict[word] = 1
        else:
            count = mydict[word]
            mydict[word] = count+1
    return mydict


def postings_list(terms, docs):
    postingsMatrix = []
    for term in terms:
        row = []
        row.append(term)
        for i in range(len(docs)):
            if term not in docs[i]:
                row.append(0)
            else:
                row.append(1)
        postingsMatrix.append(row)
    return postingsMatrix


def single_term_search(query, dir, postings):
    count = 0
    n_query = stemmer.stem(query)
    print("The documents that contain your query are:")

    for item in postings:
        if n_query == item[0]:
            for x in range(1, len(item)):
                if item[x] == 1:
                    print(dir[x - 1])
                    count += 1

    if count == 0:
        print("No Matches Found")


# Main function calls
def main():  
    corpus = input("Input corpus name: ")

    # create a directory from the corpus
    directory = os.listdir(corpus)

    # sort the directory in alphabetical order
    directory.sort()

    # List of the names of the documents in the corpus
    raw_file_names = []  # list of raw filenames

    for file in directory:
        filename = open(os.path.join(corpus, file), 'r')
        raw_file_names.append(filename)

    # List of document texts, each doc is represented by
    # an index.
    file_text = []

    for file in raw_file_names:
        file_text.append(file.read())

    # Process to normalize text
    for i in range(len(file_text)):
        file_text[i] = normalize_text(file_text[i])
        pi = create_positional_index(file_text[i], directory[i])
        piFile.write(str(pi))


    # Take stemmed tokens to build dict
    word_dictionary = {}
    for i in range(len(file_text)):
        dictionary(word_dictionary, file_text[i])

    dictionary_terms = []
    for k, v in word_dictionary.items():
        dictionary_terms.append(k)

    # Construct postings list
    postings_matrix = postings_list(dictionary_terms, file_text)

    # Print postings list for debugging
    for row in postings_matrix:
        pl.write(str(row))
        pl.write('\n')

    user_query = query_prompt()
       
    single_term_search(user_query, directory, postings_matrix)

if __name__ == '__main__':
    main()

pl.close()
piFile.close()
