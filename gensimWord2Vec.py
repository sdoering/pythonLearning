#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
from gensim.models import word2vec

"""
This is done to clean the imdb data and to save it into a cleaned file consisting of one sentence per line, to later be read via a gensim iterator. 

"""


class FileCreator(object):

	# Reading the files
	#
	def __init__(self,dirname):
		self.dirname = dirname
	def __iter__(self):
		for fname in os.listdir(self.dirname):
			open(os.path.join(self.dirname, fname))
		### HOW DO I GET ALL FILES IN ONE LIST HERE?
		### IS ONE REVIEW ALSO ONE SENTENCE?

		### TBD
			
	# Splitting the files


	# Creating output-files and writing to disc





"""
This part is the gensim iterator. 

"""

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def __iter__(self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname, fname)):
				yield line.split()

sentences = MySentences('/some/directory') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)