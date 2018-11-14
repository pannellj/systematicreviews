# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:31:22 2017

This python script imports all text files in the directory "Keywords" 
Extracts the key words section of the paper to a list
Writes the full list to a new text file

@author: em10636 (Jennifer Pannell)
"""
import glob
from itertools import chain

list_of_files = glob.glob('./Keywords/*.txt')

## What to look for at the beginning of key words
substr = "key words:" 
substr2 = "keywords:"
substr3 = "key words"
substr4 = "keywords"
# create empty list for key words & failed searches
keywordlist = []
faillist = []

## loop reads all files in directory line by line 
## looks for each sub string (substr) in each line of file
## If not found, writes file name to fail list

for fileName in list_of_files:
    with open(fileName, 'r', encoding="utf8") as myfile:
        data=myfile.readlines() # read in lines as list
        data=[element.lower() for element in data] # convert all to lowercase
        teststring = "start" #create test string
        for line in data:
            if substr in line:
                kw = line[(len(substr)+1):-1] # return from end of "key words:" to end of line
                kw = kw.lower() # convert all to lower case
                keywordlist.append(kw) # add to list of key words
                teststring = str(fileName) # this is for testing whether search failed
            elif substr2 in line:
                kw = line[(len(substr2)+1):-1]
                kw = kw.lower()
                keywordlist.append(kw)
                teststring = str(fileName)
            elif substr3 in line:
                kw = line[(len(substr3)+1):-1]
                kw = kw.lower()
                keywordlist.append(kw)
                teststring = str(fileName)
            elif substr4 in line:
                kw = line[(len(substr4)+1):-1]
                kw = kw.lower()
                keywordlist.append(kw)
                teststring = str(fileName)
        if teststring != str(fileName): # did this search fail?
            faillist.append(str(fileName)+" Keywords not found!") # add file name to fail list
            myfile.close() #close file
            kw = "" # make kw blank so it doesn't print last file kw
        print(kw) # print the key words
        myfile.close() # close the file

# split keywordlist by comma or semicolon
keywordlist=(list(chain.from_iterable(ele.split(",") for ele in keywordlist)))
keywordlist=(list(chain.from_iterable(ele.split(";") for ele in keywordlist)))
keywordlist=(list(chain.from_iterable(ele.split("\x02") for ele in keywordlist)))
keywordlist=(list(chain.from_iterable(ele.split(u'\u2022') for ele in keywordlist)))

# strip white space
keywordlist=[x.strip() for x in keywordlist]
# sort list of keywords alphabetically
keywordlist=sorted(keywordlist)

print(keywordlist) # print the final list

# write final list to text file
outfile = open("keywords.txt", "w") 
outfile.write(str(keywordlist))

# write fail list to text file
failfile = open("failedfiles.txt","w")
failfile.write(str(faillist))

# close everything
outfile.close()
failfile.close()
