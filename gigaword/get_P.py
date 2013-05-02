#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
This is just one module of get_sent_from_dir.py.
'''
__author__='Kensuke Mitsuzawa'
__version__='2013/4/21'

import sys,re

def get_p_tag(path_to_file):

    add = 'n'
    sent_set=[]
    sent_list=[]
    file_list=open(path_to_file,'r').readlines()
    for line in file_list:

        if not re.findall(r'\<P\>',line) == []:
            add = 'y'
            continue

        elif not re.findall(r'\</P\>',line) == []:
            add = 'n'
            continue

        elif add == 'y':
            sent_list.append(line)
            sent_set.append(sent_list)
            sent_list = []
            continue

    return sent_set

def call_from_other(path_to_file):
    sent_set = get_p_tag(path_to_file)
    return sent_set
    
if __name__ == '__main__':
    path_to_file = sys.argv[1]
    sent_set = get_p_tag(path_to_file)
    print sent_set
