# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:51:22 2018

@author: oneey_000
"""
totalCompare=0
totalAssign=0
class Entry:        #same class to store Entries in concordance
    def __init__(self, word, number):
        self.word=word
        self.number=number
    def __repr__(self):
        return (self.word + ": " + str(self.number))
    def __str__(self):
        return (self.word + ": " + str(self.number))
    def __lt__(self,other):
        return self.word<other.word
def binarySearch(array, search, compareNum, begin, end):
    wordCount=0
    middle = int((begin+end)/2) 
    if begin>end:   #Terminates if word not found
        return None
    elif array[middle] > search:    #recursively calls search on lower half
        compareNum+=1
        return binarySearch(array,search, compareNum, begin, middle-1)
    elif array[middle] < search:    #recusively calls search on upper half
        compareNum+=1
        return binarySearch(array,search, compareNum, middle+1, end)
    else:       # if the search term is found
        compareNum+=1
        wordCount+=1
        left = middle-1
        right = middle+1
        while (left>=0) and (array[left]==search):  #steps through array backwards until word is not found or beginning is reached
            left-=1
            wordCount+=1
            compareNum+=1
        while (right < len(array)-1) and (array[right]==search):#steps through array until word is not found or end is reached
            right+=1
            wordCount+=1
            compareNum+=1
        return wordCount, compareNum  #returns both the word count and the number of comparisons
wordArray=[]
concordance=[]
myFile = open("wordlist.txt", "r")  #reads into wordArray from file
for line in myFile:
    if line[0].isalpha():
        wordArray.append(line.strip('\n').lower())
masterList=list(set(wordArray))     #removes doubles from wordArray and stores in masterList
#masterList.sort()
print("Number of words total: " + str(len(wordArray)))
print("Number of unique words: " + str(len(masterList)))
wordArray.sort() #sorts wordArray
for item in masterList:
    concordance.append(Entry(item,str(binarySearch(wordArray,item,0,0,len(wordArray))[0]))) #appends each item from masterArray
    totalAssign+=1
    totalCompare+= binarySearch(wordArray,item,0,0,len(wordArray))[1] #increments totalCompare by number of operations during search
concordance.sort()      #sorts concordance
for entry in concordance:       #prints out first and last 10 entries
    if entry in concordance[:10] or entry in concordance[-10:]:
        print(entry)
print("Total number of comparisons: " + str(totalCompare))
print("Total number of assignments: " + str(totalAssign))