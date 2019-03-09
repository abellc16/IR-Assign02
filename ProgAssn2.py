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

def strip_punct(text):
    translator = str.maketrans('','',string.punctuation)
    return text.translate(translator)

##extract tokens
def tokens(text):
    return re.findall('[a-z]+', text.lower())


#Given a text corpus, develop a positional index. Process phrase and proximity
#queries using the positional index.
def main():

    corpus = sys.argv[1]
#create a directory from the corpus
    directory = os.listdir(corpus)
##sort the directory in alphabetical order
    directory.sort()

    punct_strip = str.maketrans('','', string.punctuation)
#read the files in the directory
    for file in directory:
        filename = open(os.path.join(corpus, file), 'r')
        text = filename.read()

        text = toLower(text)




if __name__ == '__main__':
    main()
