#
#Author: Jamison Brown
#Date: 3/5/19
#Course: CSCI 4130
#Instructor: Gudivada
#

from __future__ import division
from __future__ import print_function
import re
import math
import string
from collections import Counter
import os
import sys
from nltk.stem import *
from nltk.corpus import *
import numpy

##Text Normalization
#==================================================================

##stemming/lemmatization
stemmer = PorterStemmer()

##lowercasing / remove punctuation
#function toLower converts String
#text to lower case
def toLower(text):
    return text.lower()

#strip punctuation from a text
def strip_punct(text):
    translator = str.maketrans('','',string.punctuation)
    return text.translate(translator)

##extract tokens from a text
def tokens(text):
    return re.findall('[a-z]+', text.lower())

#function to create a dictionary given a list of tokens
def dictionary(mydict,tokens):
    for word in tokens:
        if word not in mydict:
            mydict[word] = 1
        else:
            count = mydict[word]
            mydict[word] = count+1
    return mydict

#use dictionary to create a postings list
#if the dictionary term occurs in a text then its entry in
#the postings list is 1 and it is 0 otherwise
#docList is a list of documents with each index containing the terms of that document


##function to build a postings list
##given a dictionary, a word occurs in a document
##if it is present in the dictionary and in the

#Given a text corpus, develop a positional index. Process phrase and proximity
#queries using the positional index.
def main():

    corpus = sys.argv[1]
    stop_words = set(stopwords.words('english'))
#create a directory from the corpus
    directory = os.listdir(corpus)
##sort the directory in alphabetical order
    directory.sort()

#list of document names in the corpus
    documentNames = [file for file in directory]

    rawFileNames = []#list of raw filenames

    for file in directory:
        filename = open(os.path.join(corpus,file), 'r')
        rawFileNames.append(filename)

#list of document text, each document is represented by its
#index and its text is stored as its elements
    fileText = []

    for file in rawFileNames:
        fileText.append(file.read())

#normalize text and extract tokens from each document stem the tokens
    for i in range(len(fileText)):
        fileText[i] = toLower(fileText[i])
        fileText[i] = strip_punct(fileText[i])
        fileText[i] = tokens(fileText[i])
        fileText[i] = [stemmer.stem(words) for words in fileText[i]]

#use the stemmed tokens to build a dictionary of the words used in the Corpus
    wordDictionary = {}
    for i in range(len(fileText)):
        dictionary(wordDictionary, fileText[i])

    dictionaryTerms = []
    for k, v in wordDictionary.items():
        dictionaryTerms.append(k)

    ##create postings_list
    for terms in dictionaryTerms:
        postings_list = []
        for i in range(len(fileText)):
            if terms not in fileText[i]:
                postings_list.append(0)
            else:
                postings_list.append(1)
        print(f'{terms}: {postings_list}')









if __name__ == '__main__':
    main()
