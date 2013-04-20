import cPickle as pickle
import sys,os
import stanfordXmlParser

'''
OUTLINE:To get pickle file which includes all S trees of xml parsed file.
INPUT:directory path which includes xml parsed file. 
OUTPUT:pickle file(type:list)
DEPENDANT:stanfordXmlParser(https://github.com/keisks/preproc/blob/master/stanford-core-nlp/stanfordXmlParser.py)
'''
__author__ = 'Kensuke Mitsuzawa'
__version__ = '4/20'

def get_dic(path):
    parse_list = stanfordXmlParser.parseXml(path)

    return parse_list

def open_P(S_tree_set):
    P = open('all_parsed.pickle','w')
    pickle.dump(S_tree_set,P)

def write_file():
    out = open('S_tree_str','w')
    return out

def get_tree_set(out):
    parse_list_set = []
    S_tree_set = []
    path = sys.argv[1]
    files = os.listdir(path)
    for file in files:
        parse_list =  get_dic(path+file)
        parse_list_set.append(parse_list)
        for one_sent in parse_list:
            S_tree_set.append(one_sent['tree'])
            out.write(one_sent['tree']+'\n')

    out.close()
    return S_tree_set

if __name__ == '__main__':
    out=write_file()
    S_tree_set = get_tree_set(out)
    open_P(S_tree_set)
    
    
    
