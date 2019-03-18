# Authors:    Camby Abell, Tim Gwaltney, Jamie Rios
# Assignment: Programming Assignment 02 - Creating a postional index
# Class:      CSCI 4130
# Filename:   positional_Index.py

###############################################################
#                HOW TO RUN THE PROGRAM:
#
# 1. When prompted to enter a corpus, enter 'corpus'
# 2. You may then enter a single term seach, such as 'east'
# 3. Or you may enter a two term positional query, such as
#    'east /3 carolina'. The '/3' will search for every
#    instance of those two terms appearing within 3 positions
#    of each other.
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
file = open("output.txt", 'w')


# Extract tokens and identify vocabulary for the
# dictionary
def make_dictionary(corpus):
    new_dict = os.listdir(corpus)
    for i in new_dict:
        print(i, "\n")
    return new_dict


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


# Reads the corpus file by file and normalizes each file
def read_corpus(dict, corpus):
    for i in dict:
        text = open(os.path.join(corpus, i)).read()
        words = normalize_text(text)
        file.write(str(create_positional_index(words, i)))


# Creates positional index
def create_positional_index(words, i):
    index = {}
    for idx, word in enumerate(words):
        if not word in index:
            index[word] = [i,idx]
        else: index[word].append((idx))
    return index


# Prompt user for query
def query_prompt():
    query = input("Specify query: ")
    print("Your query: ", query)
    return query


# Make a text lowercase
def to_lower(text):
    return text.lower()


# Strip punctuation from text
def strip_punct(text):
    translator = str.maketrans('','',string.punctuation)
    return text.translate(translator)


# Extract tokens from text
def tokens(text):
    return re.findall('[a-z]+', text.lower())


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
        for i in range(len(docs[i])):
                row.append(0)
            else:
                row.append(1)
        postingsMatrix.append(row)
    return postingsMatrix


# Main function calls
def main():  
    corpus = input("Input corpus name ('corpus'): ")
    stop_words = set(stopwords.words('english'))

    # create a directory from the corpus
    directory = os.listdir(corpus)

    # sort the directory in alphabetical order
    directory.sort()

    # List of the names of the documents in the corpus
    rawFileNames = []  # list of raw filenames

    for file in directory:
        filename = open(os.path.join(corpus, file), 'r')
        rawFileNames.append(filename)

    # List of document texts, each doc is represented by
    # an index.
    file_text = []

    for file in rawFileNames:
        file_text.append(file.read())

    # Process to normalize text
    for i in range(len(file_text)):
        file_text[i] = to_lower(file_text[i])
        file_text[i] = strip_punct(file_text[i])
        file_text[i] = tokens(file_text[i])
        file_text[i] = [stemmer.stem(words) for words in file_text[i]]

    # Take stemmed tokens to build dict
    word_dictionary = {}
    for i in range(len(file_text)):
        dictionary(word_dictionary, file_text[i])

    dictionary_terms = []
    for k, v in word_dictionary.items():
        dictionary_terms.append(k)

    # Construct postings list
    postings_matrix = postings_list(dictionary_terms, file_text)

    print(len(postings_matrix))

    # Print postings list for debugging
    # for row in postings_matrix:
    #     print(row)

    user_query = query_prompt()
       

if __name__ == '__main__':
    main()

file.close()
