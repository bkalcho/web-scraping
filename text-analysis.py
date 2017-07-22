#!/usr/bin/env python
__author__ = 'kalcho'

from nltk import word_tokenize
from nltk import Text


tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)