# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 08:37:26 2021

@author: Jacob Bowers
"""

def sumsquare1(n):
    
    
    print("Definitions:")
    print("For example, for a given number",n,"\b:")
    
    y = range(n+1)
    t = map(lambda a: a * a,y)
    
    sumofsquare = sum(t)
    print("The sum of the squares is =",sumofsquare)
    print()
    
    y = range(x+1)
    
    squareofsum = sum(y)
    squareofsum = pow(squareofsum, 2)
    print("The squares of the sum is =",squareofsum)
    
    dif = abs(squareofsum - sumofsquare)
    print("Therefore, the difference is:",squareofsum,"-",sumofsquare,"=",dif)
    
    return dif

x = int(input())
sumsquare1(x)

