#! /usr/bin/pyhon
# -*- coding:utf-8 -*-

__author__ = 'Kensuke Mitsuzawa'
__version__ = '2013/4/21'

import sys,os,re
import conv_to_uni
from nltk.tag.stanford import POSTagger

def get_dir_name(dir_name):
    files_list=[]
    for root,dirs,files in os.walk(dir_name):
        for f in files:
            if not re.findall(r'.raw',f) == []:
                files_list.append(os.path.join(root,f))

    return files_list

def sent_add_to_list(file_name):

    input_sent=open(file_name,'r').readlines()
    input_sent=conv_to_uni.from_utf(input_sent)

    return input_sent

def stan_pos(st,input_sent):
    """
    This function calls stanford POS tagger.In this function Stanford POS tagger directory must be in the same directory.And this function chooses model "wsj left 3 words" as normal POS tagging model. If you want to use other POS tagging models, please change first argument of st = POSTagger() below.

    """
    eval_sent = []
    for one_sent in input_sent:
        pos_result = st.tag(one_sent.split())
        print pos_result
        for one_tuple in pos_result:
            pos_format = one_tuple[0] + "_" + one_tuple[1]
            
            eval_sent.append(pos_format)

    return eval_sent

def write_to_text(file_name,posed_sent):
    write_text=open(file_name,'w')
    write_text.write((' '.join(posed_sent)))
    write_text.close()
if __name__ == '__main__':
    st = POSTagger("./stanford-postagger-2013-04-04/models/english-left3words-distsim.tagger","./stanford-postagger-2013-04-04/stanford-postagger.jar")
    if len(sys.argv) == 2:
        dir_name=sys.argv[1]
    else:
        sys.exit()
        
    file_list=get_dir_name(dir_name)
    for file_name in file_list:
        input_sent=sent_add_to_list(file_name)
        posed_sent=stan_pos(st,input_sent)
        write_to_text(file_name,posed_sent)
