# Authors:    Camby Abell, Tim Gwaltney, Jamie Rios
# Assignment: Programming Assignment 02 - Creating a postional index
# Class:      CSCI 4130
# Filename:   positional_Index.py

################################################
# HOW TO RUN THE PROGRAM:
#
# [INSERT HOW TO RUN PROGRAM HERE.]
################################################

import re
import os
import nltk


# Extract tokens and identify vocabulary for the
# dictionary
def make_dictionary(corpus):
    new_dict = os.listdir(corpus)
    return new_dict


# Takes a text as a parameter
# Removes punctuation
# Makes everything lowercase
# Handles stemming/lemmatization
def normalize_text(text):
    return re.findall('[a-z]+', text.lower())


# Reads the corpus file by file and normalizes each file
def read_corpus(dict, corpus):
    for i in dict:
        text = open(os.path.join(corpus, i)).read()
        words = normalize_text(text)
