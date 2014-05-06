#!python3.4
# -*- coding: utf-8 -*-

# DSL Converter. It should take a Lingvo decompiled .dsl dictionary as input and generate a well-formed XML for OS X Dictionary.app

import sys
import re               #import regular expressions module
import urllib.parse     # urllib.parse.quote_plus('string_of_characters_like_these:$#@=?%^Q^$')
                        # 'string_of_characters_like_these%3A%24%23%40%3D%3F%25%5EQ%5E%24'
import os
import pipes 
import shlex
import unicodedata

wordforms = []
words = []


flectionsFile = open('/Users/Alex/Development/Dictionaries development/WordForms/lexique-dicollecte-fr-v5.0.2/lexique-dicollecte-fr-v5.0.2.txt', 'r', encoding='utf-8')

outputflectionsFile = open('/Users/Alex/Development/Dictionaries development/WordForms/wordforms_fr.txt', 'w+', encoding='utf-8')

flectionFileContents = flectionsFile.read().splitlines()
flectionFileContents = flectionFileContents[15:]


for flection in flectionFileContents:
    inputstring = flection.split() 
    
    if inputstring[2] not in words:
        words.append(inputstring[2])
        wordforms.append(inputstring[1])
    else:
        wordforms[words.index(inputstring[2])] = wordforms[words.index(inputstring[2])] + ' ' + inputstring[1]

for i in range(len(words)):
    outputflectionsFile.write(words[i] + '\n')
    outputflectionsFile.write('\t' + wordforms[i] + '\n')