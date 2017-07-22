#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from random import randint


def word_list_sum(word_list):
    sum = 0
    for word, value in word_list.items():
        sum += value
    return sum


def retrieve_random_word(word_list):
    rand_index = randint(1, word_list_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0:
            return word


def build_word_dict(text):
    # Remove newlines and quotes
    text = text.replace('\n', ' ')
    text = text.replace('"', '')

    # Make sure punctuation marks are treated as their own "words",
    # so that they will be included in the Markov chain
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")
    
    words = text.split(' ')
    # Filter out empty words
    words = [word for word in words if word != ""]

    word_dict = {}
    for i in range(1, len(words)):
        if words[i-1] not in word_dict:
            # Create a new dictionary for this word
            word_dict[words[i-1]] = {}
        if words[i] not in word_dict[words[i-1]]:
            word_dict[words[i-1]][words[i]] = 0
        word_dict[words[i-1]][words[i]] = word_dict[words[i-1]][words[i]] + 1
    return word_dict


text = requests.get("http://pythonscraping.com/files/inaugurationSpeech.txt")
word_dict = build_word_dict(str(text.text.decode('utf-8')))

# Generate a Markov chain of length 100
length = 100
chain = ""
current_word = "I"
for i in range(0, length):
    chain += current_word + " "
    current_word = retrieve_random_word(word_dict[current_word])
print chain