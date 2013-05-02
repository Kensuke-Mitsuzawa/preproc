#! /usr/bin/python
# -*- codig:utf-8 -*-
import sys

def from_utf(input_sent):
    return_sent=[]
    for element in input_sent:
        element_uni=element.decode('utf-8')
        return_sent.append(element_uni)

    return return_sent
