# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:33:58 2020

@author: kritik
"""

import json#importing json library
from difflib import get_close_matches #to get closest matches


re = "y"
while re == "y" or re == "yes":
    data = json.load(open("data.json"))#loading and opening data.json file inside this python file

    def meaningsOf(word):#function to find Exact word in data.json
        if word in data:
            return data[word]
        
        elif len(get_close_matches(word , data.keys())) > 0 : #to get close realated search using difflib module
            print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
            decide = input("press y for yes or n for no:\t")
            if decide == "y":
                
                return data[get_close_matches(word , data.keys())[0]]
                
            elif decide == "n":
                return("Sorry the no result found")
            else:
                return("You have entered wrong input please enter just y or n")
        
    
    word = input("enter the word :\t").lower()#user input for searching meanings
    result = meaningsOf(word)
    if result == None:#if there is no matching words in data.json
        print("Sorry no result found for this word\n please try something different")
    elif type(result) == list :
        for meanings in result:
            print("___________________________________________________________________")
            word = get_close_matches(word, data.keys())[0]#to get the correct value of below word variable.
            print(word + " means:\t" + meanings + "\n") #This is just for good looks.
            print("___________________________________________________________________")
    else:
        print(result)
        
    re = input("re-find (yes/no or y/n) :\t").lower()

