# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:54:19 2023

@author: Larica Tsang
"""

fileText = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
rotation = 2

myFile = open("ciphertext1-2.txt", "r")

for line in myFile:     
    line = line.strip()
    fileText.append(line)

fileWords = [list(word) for phrase in fileText for word in phrase.split()]

for chars in fileWords:
    count = 0
    while count < len(chars):
        char = chars[count]
        if char.isalpha():
            position = alphabet.find(char)
            chars[count] = letters[(position-rotation)%26]
        count += 1

new_words = []
for words in fileWords:
    new_words.append(''.join(words))

encryptMessage = ' '.join(new_words)
print(encryptMessage)
myFile.close()