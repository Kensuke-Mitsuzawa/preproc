#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys
from pattern.en import pluralize

def decision(freq_line):
    T_F='F'
    word,s_freq,p_freq,s_prob,p_prob=freq_line.split('\t')
    if int(s_freq) >= 10000:
        if float(s_prob) >= 0.99:
            T_F='T'
            return T_F,word
        '''
    elif int(p_freq) >= 10000:
        if float(p_freq) >= 0.99:
            T_F='T'
            word=pluralize(word)
            return T_F,word
            '''
    else: None

if __name__ == '__main__':
    freq_lines=open(sys.argv[1],'r').readlines()
    for freq_line in freq_lines:
        if decision(freq_line) == None: pass
        else:
            T_F,word=decision(freq_line)
            if T_F == 'T':
                print word
