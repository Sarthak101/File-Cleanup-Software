import os
import shutil
import re
import datetime
def getFiles():

    Direc = "C:/Users/Sarthak/Desktop/"
    #print(f"Files in the directory: {Direc}")
    files = os.listdir(Direc)
    # Filtering only the files.
    files = [f for f in files if os.path.isfile(Direc+'/'+f)]
    # print(*files, sep="\n")

    # print("last print" , files)
    return files

def create_folder_structure(main_folder, subfolders):
    try:
        # Create the full path for the main folder
        main_folder_path = os.path.join(os.getcwd(), main_folder)

        # Check if the main folder already exists
        if not os.path.exists(main_folder_path):
            # Create the main folder
            os.makedirs(main_folder_path)
            print(f"Folder '{main_folder}' created successfully.")
        else:
            print(f"Folder '{main_folder}' already exists.")

        # Create subfolders within the main folder
        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder_path, subfolder)
            # Check if the subfolder already exists
            if not os.path.exists(subfolder_path):
                # Create the subfolder
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created successfully.")
            else:
                print(f"Subfolder '{subfolder}' already exists.")
    except Exception as e:
        print(f"Error: {e}")


def sortFile(name , ext):
    destDict = {
        "Docs" : [".docx"],
        "Text" : [".txt"],
        "Html" :[".html"],
        "Audio": [".mp3",".aac"],
        "PDFS" : [".pdf"] ,
        "Images": [".jpg" , ".png" , ".gif" ] ,
        "Videos" :[".mp4" , ".ts"] 
    }
    
    for key, values in destDict.items():
        if ext in values:
            pathname = key

    print(pathname)

    destination = f"C:/Users/Sarthak/Desktop/Organizer/{pathname}"
    source = f'C:/Users/Sarthak/Desktop/{name}'

        # Open the file for writing
    with open('C:/Users/Sarthak/Desktop/Organizer/Logs.txt', 'a') as f:
        data = f" '{name}' to '{pathname}' at ({datetime.datetime.now()})\n"
        
        f.write(data + '\n')
        print(data)
        f.close()

    try:
        dest = shutil.move(source,destination)
    
    except:
        print(f"An error occured while moving file '{name}' to '{pathname}'")

def find_file_extensions(file_name):
    pattern = r'\.[a-zA-Z0-9]+$'

    match = re.search(pattern, file_name)
    
    if match:
        return match.group(0)
    else:
        return None



# Name of the main folder
main_folder = "Organizer"

# List of subfolder names
subfolders = ['Docs', 'Texts', 'Html', 'Audio', 'Pdfs', 'Images', 'Videos']

# Call the function to create the folder structure
create_folder_structure(main_folder, subfolders)

files = getFiles()
typeList = [".docx" ,
             ".txt" ,
               ".html" ,
                 ".mp3" ,
                   ".jpg" ,
                     ".gif" ,
                       ".png" ,
                         ".mp4" ,
                           ".aac" ,
                           ".pdf" , 
                           ".ts"]
for file in files:
    if find_file_extensions(file) in typeList:
        ext = find_file_extensions(file)
        sortFile(file , ext)
