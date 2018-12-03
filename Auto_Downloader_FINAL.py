# Name: G Ung
# Date last modified: Sunday 2 Sep 2018
# Version: 3.0

'''
This python script opens a file named urls.txt in the  current folder and
downloads each url sequentually. Downloaded files are saved into the current folder.

Requirements
* In urls.txt URLs must be one per line and no line can be blank
* The URL must not use GET parameters (e.g. http://server/retrieve?file=myfile)
* urls.txt must be stored in the same folder as this file
* You must have read and write permission to this folder
* This script is MacOS and Windows compatible
'''
import os
import shutil
import glob
import os.path
import urllib.request
import pathlib
from pathlib import Path
from os.path import abspath

print("This script will download an image file from URL list in urls.txt \nlocated in current directory",
      os.getcwd(), "and save it in a folder of your choice")

mydir = Path(input(" \nEnter save location (e.g. /tmp/downloads or C:\Temp\Downloads): "))

if not (os.path.isdir(mydir)):
    os.makedirs(mydir)
path = os.path.abspath(mydir)

# Check with
# print(path + "\n")

# data_folder = Path(os.getcwd())
# file_to_open = data_folder / "urls.txt"
# Check with
# print(file_to_open.read_text())
# read = file_to_open.read_text()

links = open('urls.txt', 'r')
for link in links:

    # Get one line of text (e.g. http://server/files/grades.doc),
    # then get the filename from the end of the URL
    link = link.strip()
    filename = link.rsplit('/', 1)[-1]

    # Does this file exist in this folder? If not, download it
    if not (os.path.isfile(filename)):
        # print('Downloading: ' + filename)
        # Prints download status to user and prints "save as" path (location)
        print("DOWNLOADING FROM: ", link, "\nSAVING: ", filename, " TO >> ", path)
        try:
            urllib.request.urlretrieve(link, filename)
            print("File size was", os.path.getsize(filename))
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')

    # File exists; don't download
    else:
        print("This file exists already.")

if(mydir.resolve() != pathlib.Path.cwd()):
    # Takes all image files in .jpg format and moves to mydir
    files = glob.iglob(os.path.join(os.getcwd(), "*.jpg"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, mydir)

# Check with
# os.chdir(mydir)
# print(os.listdir())
# print(os.getcwd())
links.close()
print("\nFinished downloading.")
