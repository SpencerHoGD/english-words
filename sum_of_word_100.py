#! /usr/bin/env python3
#encoding:utf-8
'''
Created on 2019-09-09
hexiaoming
'''

import os


def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

#print(sum_of_word('attitude'))

with open('result.md', 'w') as result:
    with open('words_alpha.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                result.write(word)
