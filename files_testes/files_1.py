'''
Selective Copy

Write a program that walks through a folder tree and searches for files 
with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.
'''

import os, shutil, re

def simple_backup(dir, extension):
    """
    This function receives a directory (dir) and a extension type (ext)
    and copy all files in to this directory to a .backup new directory inside 
    the directory, and copy all these files to the new .backup directory.
    """
    try:
        os.mkdir(os.path.join(dir,'.backup'))
    except FileExistsError:
        print("Diretorio de backup já existe. \n Copiando e sobreescrevendo os arquivos para o diretorio de backup")

    filenameRegex = re.compile(r'{}$'.format(extension), re.IGNORECASE)
    for folderName, subfolderName, filenames in os.walk(dir):
        for filename in filenames:
            if filenameRegex.search(filename) != None:
                print(filename)






dir = '/home/renato/workspace/automateboringstuff/files_testes'
ext = '.py'

simple_backup(dir=dir, extension=ext)