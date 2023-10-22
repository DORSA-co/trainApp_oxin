import os

def rename_subdirs(path):
    for subdir, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == 'Annotaions':
                old_name = os.path.join(subdir, dir)
                new_name = os.path.join(subdir, 'Annotations')
                os.rename(old_name, new_name)

rename_subdirs('../oxin_image_grabber/2023')