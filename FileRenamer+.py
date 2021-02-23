#Importing OS to work with OS functions and Walk to walk out all subdirectories.
import os
from os import walk

#Getting CWD for refrence of program
currentDir = os.getcwd()

#Input asking for Step 1: File name pattern to look for:
step1 = input("Enter the original file pattern you are looking for, step 1: ")
#step1 = "CS-01-20"

#akign for step 1: file name pattern to replace with
step2 = input("Enter the original file pattern you are looking for, step 1: ")
#step2 = "ORL-01-20"


#Creating dictionary for dir/filenames
folderFilesDict = {}

for (dirpath, dirnames, filenames) in walk(currentDir):

    #Listing each file name indivudallly
    for singleFiles in filenames:
        #If step1 var in this file then save to dict
        if step1 in str(singleFiles):
            folderFilesDict[dirpath] = singleFiles

            #Creating new file name
            newName = step2 + singleFiles[len(step1):]

            # Renaming files:
            os.rename(dirpath + "\\" + singleFiles, dirpath + "\\" + newName)

            print(f"This file was renamed from this: {singleFiles} to this {newName} in this path {dirpath}\n")

print("----------------------------DONE----------------------------------- \n Press Enter to Exit or you can save output for logging.")
input()