import glob
import os
import re

image_path = './Data/JPEGImages/*.jpg'
images = glob.glob(image_path)

def move(txt_file_path, dir_path):
    txt_file_path = './Data/ImageSets/Main/{}'.format(txt_file_path)
    with open(txt_file_path, 'r') as f:
        size_to_read = 6
        f_content = f.read(size_to_read)

        while len(f_content) > 0:
            for each_image in images:
                # Use Regex standard libray to extract image_id_number.
                m = re.search(r'.*/(.*)\.\w+', each_image)
                image_number = m.group(1)
                if (image_number == f_content[0:-1]):
                    original_path = './Data/JPEGImages/{}.jpg'.format(image_number)
                    moveto_path = '{}/{}.jpg'.format(dir_path, image_number)
                    os.rename(original_path, moveto_path)
                    print('Moved image index: {}'.format(image_number))
            #print(f_content, end='')
            f_content = f.read(size_to_read)

def if_not_exist_then_make(txt_file_path, dir_path):
    if os.path.exists(dir_path):
        print('Directory Already exists!')
    else:
        os.mkdir(dir_path)            # Create dir_path directory
        move(txt_file_path, dir_path) # move the images into dir_path directory through .txt file

if os.path.exists('./Splited-data'):
    if_not_exist_then_make('test.txt',     './Splited-data/Test-data')
    if_not_exist_then_make('trainval.txt', './Splited-data/Train-data')
else:
    os.mkdir('Splited-data')
    if_not_exist_then_make('test.txt',      './Splited-data/Test-data')
    if_not_exist_then_make('trainval.txt', './Splited-data/Train-data')
