
# notes
# - before running, update extSrcPath so it points to a local copy of the ExtJS src folder.
#      - the path should be relative to this files


# questions
# - is extSrcContents in a usable format?
# - should all this be in some kind of class?
# - would it be best to have the object/dictionary in this format
#    extSrcContents.container.Container.*some config option*


import os
import json
import re

# relative path to the ExtJS src folder without trailing slash
extSrcPath = '../../htdocs/extjs/4.1.0/src'

# declate the object (dictionary??) to store the files/folders
extSrcContents = {}


# looks inside the passed folder for files/folders.
# if it sees a folder it calls itself to get the contents of that folder .... and so on until there is only files
# returns a json object (ish) with the folder contents
def getFolderContents(path=extSrcPath):
    folderItems = os.listdir(path)
    files = []

    for item in folderItems:
        if os.path.isdir(path + '/' + item):
        # this is a folder.
        # create a dictionary to hold the folders contents and call the getFolderContents method
            folder = {}
            folder[item] = getFolderContents(path + '/' + item)
            files.append(folder)
        else:
        # this is a file
            files.append(item)
            # open the file
            openItem = open(path + '/' + item, "rt")
            # read the file
            openItemText = openItem.read()
            # search for any string before an ':' in openItemText and store in findColon as a list
            findColon = re.findall('((\w)*?)(:|( :))', openItemText)
            # findColon holds something that looks like "('getBy', 'y', ' :', ' :')"
            # iterate through each list in the findColon list and only print out the first item
            for i in findColon:
                print(i[0])
            openItem.close

    return files


#call it
extSrcContents["root"] = getFolderContents()

# create the files.json file and dump the extSrcContents dictionary
allFiles = open("allFiles.json", "w+", encoding="utf-8")
allFiles.write(json.dumps(extSrcContents, indent=4))
allFiles.close()
