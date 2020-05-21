# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:33:58 2020

@author: kritik
"""

import json#importing json library

re = "y"
while re == "y" or re == "yes":
    data = json.load(open("data.json"))#loading and opening data.json file inside this python file

    def meaningsOf(word):#function to find word in data.json
        if word in data:
            return data[word]
        
    
    word = input("enter the word :\t").lower()#user input for searching meanings
    result = meaningsOf(word)
    if result == None:#if there is no matching words in data.json
        print("Sorry no result found for this word\n please try something different")
    else:
        for meanings in result:
            print("___________________________________________________________________")
            print(word + " means:\t" + meanings + "\n") #This is just for good looks.
            print("___________________________________________________________________")
        
    re = input("re-find (yes/no or y/n) :\t").lower()

