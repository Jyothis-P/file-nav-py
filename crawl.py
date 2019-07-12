# Python code to search .mp3 files in current 
# folder (We can change file type/name and path 
# according to the requirements. 
import os 

# This is to get the directory that the program 
# is currently running in. 

def get_list():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    files_list = {}

    for root, dirs, files in os.walk(dir_path):
        if 'Music' not in root:
            continue
        for file in files: 

            # change the extension from '.mp3' to 
            # the one of your choice. 
            if file.endswith('.mp3'):
                path = root+'\\'+str(file)
                name = str(file)[:-4]
                files_list[ name ] = path
                print(path)

    print(str(len(files_list)) + ' files indexed. ')
    return files_list

