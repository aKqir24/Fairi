from shutil import move
from os import path, makedirs, listdir

keywords=[ "somefile" ] # TODO: The add gui will also add this
files_folder=[ "test" ] # TODO: The add gui with input folder settings will add this
extensions=[ '.png', '.pdf' ] # TODO: The add gui will add this
for folder in files_folder:
    for file in listdir(folder):
        for character in range(len(file)):
            for keyword in range(len(keywords)):
                if file[character:].startswith(keywords[keyword]):
                    file_type=path.splitext(file)[1].lower()
                    if file_type in extensions:
                        print(file[character:])
                        break
