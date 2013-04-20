#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys,os,glob
import get_P
'''
OUTLINE:To get only raw texts from Gigaword(http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2003T05) 
INPUT:Path to directory which contains Gigaword data.You can appoint parent directory. The "os.walk" module automatically get path to all sub-directory.  
OUTPUT: *.raw files are produced in the same directory as original Gigaword file. 
'''
'__author__'='Kensuke Mitsuzawa'
'__version__'='2013/4/21'

def get_dir_name(dir_name):
    files_list=[]
    for root,dirs,files in os.walk(dir_name):
        for f in files:
             files_list.append(os.path.join(root,f))
             
    return files_list

def write_to_file(sent_set,write_file):
    for sent in sent_set:
        write_file.write(''.join(sent))
    write_file.close()

if __name__ == '__main__':

    if len(sys.argv) == 2:
        dir_name=sys.argv[1]
    else:
        print 'Usage: python {0} path_to_dirrectry(which contains gigaword data)'.format(sys.argv[0])
        sys.exit()

    file_list = get_dir_name(dir_name)
    for file_name in file_list:
        write_file=open(file_name+'.raw','w')
        sent_set=get_P.call_from_other(file_name)
        write_to_file(sent_set,write_file)
