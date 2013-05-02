#! /usr/bin/python
# -*- coding:utf-8 -*-

import cPickle as pickle
import sys,os,argparse
import stanfordXmlParser

'''
OUTLINE:To get pickle file which includes all S trees of xml parsed file.
INPUT:directory path which includes xml parsed file. 
OUTPUT:pickle file(type:list)
DEPENDANT:stanfordXmlParser(https://github.com/keisks/preproc/blob/master/stanford-core-nlp/stanfordXmlParser.py)
'''
__author__ = 'Kensuke Mitsuzawa'
__version__ = '5/2'

def get_dic(path):
    parse_list = stanfordXmlParser.parseXml(path)
    return parse_list

def open_P(S_tree_set,dependency_tuple_set):
    P = open('all_parsed.pickle','w')
    dependency_P=open('dependency.pickle','w')
    pickle.dump(S_tree_set,P)
    pickle.dump(dependency_tuple_set,dependency_P)

def get_tree_set(args):
    parse_list_set = []
    dependency_tuple_set=[]
    files = os.listdir(args.path)
    for file in files:
        parse_list =  get_dic(args.path+file)
        parse_list_set.append(parse_list)
        #dependency_tuple_setにdependency情報を一文ごとに追加していきたい
        map(lambda x:dependency_tuple_set.append((x['word'] ,x['pos'] ,x['basDep'] ,x['colDepID'] ,x['ccpDepID'] ,x['ccpDep'] ,x['basDepID'])),parse_list)
        for one_sent_dep in dependency_tuple_set: print one_sent_dep,'\n'
                      
    return parse_list_set,dependency_tuple_set
def std_xml_dic(xml_dic):
    for one_sent in xml_dic: print one_sent,"\n"

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-m' ,'--mode' ,help='get pickle from xml mode(g) or open pickle mode(o)' ,required=True)
    parser.add_argument('-p', '--path' ,help='path to xml directory or path to pickle files')
    args=parser.parse_args()
    if args.mode == 'g':
        parsed_list,dependency_tuple_set = get_tree_set(args)
        open_P(parsed_list,dependency_tuple_set)
    elif args.mode == 'o':
        P=open(args.path ,'r')
        xml_dic=pickle.load(P)
    
    
