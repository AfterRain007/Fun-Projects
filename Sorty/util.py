from datetime import datetime
import os, re

#Take All File from the Directory
def take_file_list(directory):
    #Take List of All File in Directory
    files_list = list((root, file) for root, dirs, files in os.walk(directory) for file in files)
    
    #Take Year of All File in the Files_list
    year = list(takeYear(f"{root}/{file}") for root, file in files_list)
    
    #Combine Both List
    files_list = [tup + (num,) for tup, num in zip(files_list, year)]
    
    return files_list

#Take Year of Creation from File Directory
def takeYear(fileDir):
    timestamp = os.path.getmtime(fileDir)
    timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.year

#Filtering list1 with list2
def filterList(list1, list2):
    filtered_list = [item for item in list1 if item not in list2]
    return filtered_list

#Return a List of File to Move
def list_files_format(files, reg):
    #files_list = []
    compiled_patterns = [re.compile(pattern) for pattern in reg["regex"]]
    
    files_list = [file for file in files if any(re.search(pattern, file[1].lower()) for pattern in compiled_patterns)]
    '''
    for file in files:
        if any(re.search(ext, file[1].lower()) for ext in compiled_patterns):
            files_list.append(file)
    '''     
    return files_list
   
#Moving the File
def moveFile(files, reg):
    for file in files:
        fileDir = f"{file[0]}/{file[1]}"
        try:
            os.rename(fileDir, f"./{reg['folder_name']}/{file[2]}/{file[1]}")
        except FileExistsError:
            continue
            #print(f"{file[1]} exist in the destination folder")
        except FileNotFoundError:
            os.makedirs(f"./{reg['folder_name']}/{file[2]}")
            os.rename(fileDir, f"./{reg['folder_name']}/{file[2]}/{file[1]}")
    
#Sorting the Item in Respect to Regular Expression and It's year of Creation
def sortRegex(files, regexDict):
    amount = []
    for Reg in regexDict:
        file2Move = list_files_format(files, Reg)
        amount.append(len(file2Move))
        moveFile(file2Move, Reg)
        files = filterList(files, file2Move)
        
    return sum(amount)