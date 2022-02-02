import os
import time

capitalAascii = 65
# renames a file or directory
# os.rename()

# Gets items that are in the given path and sorts them
def get_items_in_directory(path):
    items = []
    # looping through the items in the directory and adding them to a list
    for item in os.listdir(path):
        # Recursively going into directories
        if os.path.isdir(path + item):
            time.sleep(0.0005)
            get_items_in_directory(path+item + "/")

        if not item.startswith('.'):
            for i in range(len(item)):
                if item[i] == '_' and ord(item[i-1]) < capitalAascii:
                    item = item[i+1: len(item)]
                    break
            items.append(item)
    # sorting the newly created list in alphabetical order
    items.sort()
    numberedItems = number_items_in_directory(items)
    return rename_files(path, numberedItems)

# Takes the new sorted items and numbers them
def number_items_in_directory(items):
    i = 1
    newArray = []
    for j in items:
        newArray.append(str(i) + "_" + j)
        i += 1
        # print(newArray[i-2])
    return newArray


# Loop through list of items in directory
# if the item contains 
def rename_files(path, items):
    iter = 1
    for item in items:
        digitLength = len(str(iter)) # Get length of number in front of filename
        for p in os.listdir(path):
            if p == item[digitLength+1:len(item)]:
                # print('renamed' + " " + p)
                # print("item: " + item)
                # print("p: " + p)
                time.sleep(0.0005)
                os.rename(path+p, path+item)
                break
        iter += 1
    return os.listdir(path)

# Loops until user wants to stop organizing files
print("")
print("WARNING: THIS PROGRAM WILL RENAME FILES AND FOLDERS AND DOES NOT HAVE AN UNDO BUTTON!")
print("MAKE SURE TO PASTE THE CORRECT DESIRED PATH INTO THE PROMPT.")
print("")
run = True
while(run):
    print("__________________________________________")
    print("If you would like to exit, type 'exit()'")
    print("")
    path = input("Enter path of directory: ")
    if path.__contains__('exit()'):
        run = False
        break

    if path[-1].__contains__('/'):
        pass
    else:
        path = path + '/'

    # Checks if path exists
    if os.path.exists(path):
        # Runs recursive methods to number and rename all files and sub-directories in path
        numberedItems = get_items_in_directory(path)
        print('done')
        print('')
    else:
        print("That path does not exist. Please enter another.")
        print('')

    