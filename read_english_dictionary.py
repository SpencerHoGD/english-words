#! /usr/bin/env python3
#encoding:utf-8
'''
Created on 2019-09-09
hexiaoming
'''

import os

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print('fate' in english_words)
    with open('
