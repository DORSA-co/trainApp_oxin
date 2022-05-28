from camera_live import live_manager
import backend.camera_connection as camera_connection

cameras = camera_connection.connect_manage_cameras()
live = live_manager(path='/home/reyhane/camera_images')
live.save_camera_images(cameras)