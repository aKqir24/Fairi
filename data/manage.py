'''
Manage the data that the users inputs, like folders and files and others.
'''

from shutil import move
from os import path, makedirs, listdir

def organize():
    data={
            "item_1": { 
                    "name": "Modules_EXT",
                    "key_sensitive": False,
                    "folders": [ "test" ],
                    "keywords": [ "somefile" ],
                    "extensions": [ '.png', '.pdf' ]
            }
    } 

    # FIX: the data dictionary can be get in the get.py which returns the dictionary
    # FIX: while calling it like this data=get() where it is also imported...

    for item in data.values():
        for folder in item['folders']:
            for file in listdir(folder):
                for character in range(len(file)):
                    for keyword in item['keywords']:
                        if item['key_sensitive'] == False:
                            keyword = keyword.casefold()
                            filename = file[character:].casefold()
                        else:
                            filename = file[character:]
                        if filename.startswith(keyword):
                            file_type=path.splitext(file)[1].lower()
                            if file_type in item['extensions']:
                                print(file[character:])
                                break
def verify():
    pass
organize()
