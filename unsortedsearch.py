# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:12:44 2018

@author: oneey_000
"""
class Entry:                        ## Custom class to create concordance
    def __init__(self, word, number):
        self.word=word
        self.number=number
    def __repr__(self):     # used for debugging
        return (self.word + ": " + str(self.number))
    def __str__(self):      #used for debugging
        return (self.word + ": " + str(self.number))
    def __lt__(self,other): #used to sort
        return self.word<other.word
wordArray=[]
concordance=[]
compareNum=0
assignNum=0
myFile = open("wordlist.txt", "r")
for line in myFile:
    if line[0].isalpha():
        wordArray.append(line.strip('\n').lower())
masterList=list(set(wordArray))     #removes doubles from wordArray, stores in masterList
print("Number of words total: " + str(len(wordArray)))
print("Number of unique words" + str(len(masterList)))
for word in masterList:
    wordCount=0
    for item in wordArray: # Searching unsorted list
        if item == word:
            wordCount+=1
            compareNum +=1
        else:
            compareNum+=1
    concordance.append(Entry(word,wordCount))   #appends new Entry to concordance
    assignNum+=1
concordance.sort()      # sorts concordance using defined <
for entry in concordance:       #Prints only the first and last 10
    if entry in concordance[:10] or entry in concordance[-10:]:
        print (entry)
print ("Number of comparisons: " + str(compareNum))
print ("Number of assignments: " + str(assignNum))
    