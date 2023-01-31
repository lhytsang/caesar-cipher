# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:54:19 2023

@author: Larica Tsang
"""

fileText = []

myFile = open("ciphertext1-2.txt", "r")
for line in myFile:     
    line = line.strip()
    #print(line)
    fileText.append(line)
#print(fileText)
fileWords = [word for phrase in fileText for word in phrase.split()]
print(fileWords)
myFile.close()