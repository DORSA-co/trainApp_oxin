import os



settings = {
    'image_format' : '.jpg'
}

def sheet_image_path(main_path,id, side, camera_numbers, n_frame, format_img):
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path,str(id),'TOP', str(camera_numbers), str(n_frame) + str(format_img) ))
    
    elif 'bot' in side.lower() or 'down' in side.lower() :
        return(os.path.join(main_path,str(id),'BOTTOM', str(camera_numbers),str(n_frame) + str(format_img)  ))

def sheet_path(main_path,id):
    return(os.path.join(main_path,str(id)))




