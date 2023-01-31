# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 02:54:19 2023

@author: Larica Tsang
"""

fileText = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
rotation = 2

# Opening the file with the text to be encrypted/decrypted
myFile = open("ciphertext1-2.txt", "r")

# Removing spaces at the start and end of the words and adding it to a new list
for line in myFile:     
    fileText.append(line.strip())

# Creating a list of letters within words within the list of words
fileWords = [list(word) for phrase in fileText for word in phrase.split()]

# Changing the original letter into an encrypted/decrypted letter
for chars in fileWords:
    count = 0
    while count < len(chars):
        char = chars[count]
        if char.isalpha():
            position = alphabet.find(char)
            chars[count] = letters[(position-rotation)%26]
        count += 1

# Joining all the letters and words into one sentence  
new_words = []
for words in fileWords:
    new_words.append(''.join(words))
newMessage = ' '.join(new_words)

# Showing the final new encrypted/decrypted message
print(newMessage)
myFile.close()