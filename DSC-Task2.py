import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(indent+ os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(subindent+ f)

def run():
    print('Program to show the file tree of the current tree')
    print('Type filetree to show the file tree of the current folder')
    print('Type filetree <dir> to show the file tree of the given directory')
    print('Type the file name to find files of the same name (if extention is not given, it finds files with the same name, and different extentions too)')
    inp = input()
    if inp == 'filetree':
        list_files('.')
    elif inp.startswith('filetree'):
        list_files(inp.split()[1])
    else:
        with open('.dirignore') as ignorefile:
            ignoredirs = ignorefile.readlines()
        for root, dirs, files in os.walk(str(os.path.normpath('.'))):
            for i in files:
                if inp in i:
                    if len(ignoredirs)>0:
                        for k in ignoredirs:
                            if not str(os.path.normpath(root)).startswith(str(os.path.normpath(k))):
                                print(os.path.abspath(os.path.normpath(root+'\\'+i)))
                    else:
                        print(os.path.abspath(os.path.normpath(root+'\\'+i)))
run()
input()
