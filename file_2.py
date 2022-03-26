'''
Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or folders 
to take up the bulk of the space on your hard drive. 
If you’re trying to free up room on your computer, 
you’ll get the most bang for your buck by deleting the most massive of the unwanted files. 
But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, 
ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.
'''

import os, shutil, re

def find_big_files(directory: str, file_size: int, look_dir: bool):
    """
    Recebe 3 variaveis
    directory -> diretorio que será buscado
    file_size -> tamanho minimo para listar os arquivos/diretorios in MB
    look_dir -> incluir diretorios ou não
    """

    for folderName, subfolderName, filenames in os.walk(directory):
        for filename in filenames:
            fullFileName = os.path.join(directory,folderName,filename)
            print(f'O tamanho do arquivo, {filename} é {os.path.getsize(fullFileName)/1024}')



dir = '/home/renato/workspace/automateboringstuff/files_testes'

find_big_files(dir, 100, True)