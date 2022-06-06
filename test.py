from camera_live import live_manager

live = live_manager(path='./oxin_image_grabber')
live.read_camera_images()
