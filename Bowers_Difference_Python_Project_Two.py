# -*- coding: utf-8 -*-
"""
@author: Jacob Bowers
"""

def Difference():
    x = int(input())
   
    p = str(x)
    sumofsquare = 0
    squareofsum = 0
    
    print("Definitions:")
    print("For example, for a given number " + p +":")
    
    x += 1
    for i in range(x):
        y = int(i) ** 2
        sumofsquare += y
    stsumofsquare = str(sumofsquare)
    
    if (x > 4):
        print("The sum of the squares is: 1^2 + 2^2 + ... + " + p + "^2 = " + stsumofsquare)    
    else: 
        print("The sum of the squares is: " + stsumofsquare) 
        
    b = 0   
    for a in range(x):
        b += a
        squareofsum = b
    stb = str(b)
    squareofsum = squareofsum ** 2
    stsquareofsum = str(squareofsum)
    
    if (x > 4):
        print("The square of the sum is: (1 + 2 + ... + " + p + ")^2 = " + stb + "^2 = " + stsquareofsum)    
    else: 
        print("The square of the sum is: " +stb + "^2 = " + stsquareofsum) 
    
    dif = squareofsum - sumofsquare
    stdif = str(dif)
    print("Therefore, the difference is: " + stsquareofsum + " - " + stsumofsquare + " = " + stdif)
    
    return dif
Difference()

