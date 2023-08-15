import os
import shutil

path = "dataset"
dir_list = os.listdir(path)

age_list = []

for imagefile in dir_list:
    index_list = []

    for index, character in enumerate(imagefile):
        if character == "_":
            index_list.append(index)

    birth = imagefile[index_list[0] + 1:index_list[0] + 5]
    photo = imagefile[index_list[1] + 1:index_list[1] + 5]
    age = int(photo) - int(birth)

    print(imagefile, birth, photo, age)

    age_list.append(age)
    
   
    if age < 30:
        folder_name = f'ageDataset/<30'
    elif age < 40:
        folder_name = f'ageDataset/30-40'
    elif age < 50:
        folder_name = f'ageDataset/40-50'
    else:
        folder_name = f'ageDataset/50+'
        
        # Create the destination folder if it doesn't exist
    if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
    source = os.path.join(path, imagefile)
    destination = os.path.join(folder_name, imagefile)
        
        # Move or copy the image file to the destination folder
    shutil.copy(source, destination)
  
