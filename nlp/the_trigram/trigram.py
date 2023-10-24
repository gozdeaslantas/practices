#!/bin/python3
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = sys.stdin.read()
    if len(s) == 0:
        print('')
    sentences = s.lower().split('.')
    
    ''' sentences[0]: i came from the moon
        sentences[1]: he went to the other room
        sentences[2]: she went to the drawing room
        ...
    '''
    freq = {}
    window_size = 3
    triple = ''
    for sent in sentences:
        sent_arr = sent.strip().split(' ')
        for ind in range(len(sent_arr)):
            triple = ' '.join(sent_arr[ind:ind+window_size])
            triple = triple.strip()
            if len(triple.split()) == 3:
                if triple in list(freq.keys()):
                    freq[triple.strip()] += 1
                else:
                    freq[triple.strip()] = 1
                if ind + window_size == len(sent_arr):
                    break
                
                
    '''
        expected freq table:
        i came from: 1
        came from the: 1
        ..
        he went to: 1
        went to the: 2
        she went to: 1
    '''
    '''triples = pd.DataFrame(freq, columns=['triple', 'count']).sort_values('count', ascending=False)
    print(triples.iloc[0]['triple'])
    '''
        
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(list(dict(sorted_freq).keys())[0])
