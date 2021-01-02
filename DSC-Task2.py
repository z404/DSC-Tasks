'''
PROGRAM TO READ CURRENT DIRECTORY, INDEX PATHS, AND SEARCH FOR FILES
'''
#importing os for walking through directories
import os

#function to neatly display the files with an indent for subdirectories
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(indent+ os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(subindent+ f)

#menu based program to choose functionality
print('Program to show the file tree of the current tree')
print('Type filetree to show the file tree of the current folder')
print('Type filetree <dir> to show the file tree of the given directory')
print('Type the file name to find files of the same name')
#get input for menu
inp = input()
if inp == 'filetree':
    #list files in this directory
    list_files('.')
elif inp.startswith('filetree'):
    #list files in given directory
    list_files(inp.split()[1])
else:
    #if file exists, read the file and get ignored directories
    try:
        with open('.dirignore') as ignorefile:
            ignoredirs = ignorefile.readlines()
    except:
        ignoredirs = []
    #walk through each file and get files with same name
    for root, dirs, files in os.walk(str(os.path.normpath('.'))):
        for i in files:
            if inp in i:
                if len(ignoredirs)>0:
                    for k in ignoredirs:
                        if not str(os.path.normpath(root)).startswith(str(os.path.normpath(k))):
                            #printing absolute file path
                            print(os.path.abspath(os.path.normpath(root+'\\'+i)))
                else:
                    #printing absolute file path
                    print(os.path.abspath(os.path.normpath(root+'\\'+i)))
#as command prompt closes, this input is used to hold the cmd to stop it from closing after showing output
input()
