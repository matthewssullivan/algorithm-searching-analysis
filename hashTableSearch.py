# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:15:48 2018

@author: oneey_000
"""

class Entry:
    def __init__(self, word,number):
        self.word=word
        self.number=number
    def __repr__(self):
        return (self.word + ": " + str(self.number))
    def __str__(self):
        return (self.word + ": " + str(self.number))
    def __lt__(self,other):
        return self.word<other.word
hashTable=[[] for _ in range(100000)]   #creats list of empty lists
wordArray=[]    #array to store words read from file
concordance=[]  #array to store Entrys made of words from file
numCompare=0
numAssign=0
myFile = open("wordlist.txt", "r")      #reads from file
for line in myFile:
    if line[0].isalpha():
        wordArray.append(line.strip('\n').lower())
#print (wordArray)
masterList=list(set(wordArray)) #removes duplicates from wordArray
masterList.sort()
wordsInHash=0
print("Number of words total: " + str(len(wordArray)))
print("Number of unique words: " + str(len(masterList)))
for word in wordArray:  #Creates hash table using words in wordArray
    sum=0
    inTable=False
    sum = hash(word)%100000     #uses python hash function and limits it to size of array
    for contents in hashTable[sum]:     #steps through elements in the list at that address
        if word == contents.word:       #if the word is already there
            inTable=True
            contents.number+=1          #iterates word number
            break
    if inTable==False:                  # if it reaches the end and the word is not present
        hashTable[sum].append(Entry(word,1))    #Adds new entry and sets the number to one
        wordsInHash+=1          #iterates the number of words in the hash
for item in masterList:     #steps through master list
    sum=0
    sum=hash(item)%100000
    for contents in hashTable[sum]:         #steps through the array at the hashed address
        if (item == contents.word):         #if the word is in the array
            concordance.append(contents)    #append the entry to the concordance
            numAssign+=1
            numCompare+=1
            break
        else:
            numCompare+=1
#concordance.sort       ## works, but sorting masterlist first aids in debugging
for entry in concordance:
    if entry in concordance[:10] or entry in concordance[-10:]:
        print (entry)
print("Number of comparisons: " + str(numCompare))
print("Number of assignments: " + str(numAssign))    