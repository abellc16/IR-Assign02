# Authors:    Camby Abell, Tim Gwaltney, Jamie Rios
# Assignment: Programming Assignment 02 - Creating a postional index
# Class:      CSCI 4130
# Filename:   positional_Index.py

################################################
# HOW TO RUN THE PROGRAM:
#
# [INSERT HOW TO RUN PROGRAM HERE.]
################################################

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
    textNorm = re.findall('[a-z]+', text)
    normText = []
    for token in textNorm:
        normText.append(stemmer.stem(token))
    return normText



# Reads the corpus file by file and normalizes each file
def read_corpus(dict, corpus):
    for i in dict:
        text = open(os.path.join(corpus, i)).read()
        words = normalize_text(text)
        file.write(str(createPositionalIndex(words, i)))

# Creates positional index
def createPositionalIndex(words, i):
    index = {}
    for idx, word in enumerate(words):
        if not word in index:
            index[word] = [i,idx]
        else: index[word].append((idx))
    return index


# Main function calls
def main():  
        corpus = input("Input corpus name: ")
        dictionary = make_dictionary(corpus)
        read_corpus(dictionary, corpus)
       

if __name__ == '__main__':
    main()

file.close()
