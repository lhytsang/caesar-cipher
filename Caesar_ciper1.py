# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:54:19 2023

@author: Larica Tsang
"""

fileText = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
rotation = 11
myFile = open("ciphertext1-2.txt", "r")
for line in myFile:     
    line = line.strip()
    #print(line)
    fileText.append(line)
#print(fileText)
fileWords = [list(word) for phrase in fileText for word in phrase.split()]
#print(fileWords)
#fileChars = [letter for term in fileWords for letter in term]
#print(fileChars)

for chars in fileWords:
    count = 0
    while count < len(chars):
        char = chars[count]
        if char.isalpha():
            position = alphabet.find(char)
            chars[count] = letters[(position+rotation)%26]
        count += 1
print(fileWords)
myFile.close()