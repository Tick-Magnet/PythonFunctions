# -*- coding: utf-8 -*-
"""
@author: Jacob Bowers
"""

def Square():
  
    n = int(input())
    s = str(n)
    o = ""
    
    for x in str(s):
        o += str(int(x) ** 2)
    
    i = int(o)
    print(i)
    
    return(i)

Square()