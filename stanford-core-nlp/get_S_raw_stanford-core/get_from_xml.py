#! /usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Kensuke Mitsuzawa'
__version__ = '2013/4/25'

import re,sys,os,glob

def conv_to_uni(i_list):
    return_list=[]
    for element in i_list: return_list.append(element.decode('utf-8'))
    return return_list
def conv_to_utf(i_list):
    return_list=[]
    for element in i_list: return_list.append(element.encode('utf-8'))
    return return_list
def get_S_raw(xml_file):
    xml_file=conv_to_uni(xml_file.readlines())
    #入力は読み込み済みのファイル。リスト化はこの関数内で行う
    word_list_set=[]
    S_tree_set=[]
    for line in xml_file:
        if re.findall(ur'<sentence id="\d+">',line):
            sentence_start='t'
            sentence_id=int(line.replace(u'      <sentence id="',u'').replace(u'">\r\n',u''))
            continue
        elif re.findall(ur'<tokens>',line):
            tokens_start='t'
            word_list=[]
            continue
        elif re.findall(ur'<word>.+</word>',line):
            word=line.replace(u'            <word>',u'').replace(u'</word>\r\n',u'')
            word_list.append(word)
            continue
        elif re.findall(ur'</tokens>',line):
            tokens_start='f'
            one_sentence_word_tuple=(sentence_id,conv_to_utf(word_list))
            word_list_set.append(one_sentence_word_tuple)
            continue
        elif re.findall(ur'<parse>.+</parse>',line):
            S_tree=line.replace(u'        <parse>',u'').replace(u'</parse>\r\n',u'')
            one_sentence_S_tuple=(sentence_id,S_tree)
            S_tree_set.append(one_sentence_S_tuple)
            continue
        elif re.findall(ur'</sentence>',line):
            sentence_start='f'
            continue
        else: continue
    return S_tree_set,word_list_set
def open_xml_recursive(path_to_dir):
    target_file_list=[]
    for root,dirs,files in os.walk(path_to_dir):
        for f in glob.glob(os.path.join(root,'*.xml')):
            target_file_list.append(f)
    return target_file_list
def main():
    if len(sys.argv) == 2:
        target_file_list=open_xml_recursive(sys.argv[1])
    else: sys.exit('write more arg')
    for target_file in target_file_list:
        S_tree_set,word_list_set=get_S_raw(open(target_file,'r'))
        write_S=open(target_file+'.S','w')
        write_raw=open(target_file+'.raw','w')
        for i,S_tree in enumerate(S_tree_set):
            write_S.write(str(S_tree[0])+'\t'+S_tree[1]+'\n')
            write_raw.write(str(word_list_set[i][0])+'\t'+' '.join(word_list_set[i][1])+'\n')
if __name__ == '__main__':
    main()
