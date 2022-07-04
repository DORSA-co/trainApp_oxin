from backend import camera_connection
from camera_live_thread import ImageManager

if __name__ == '__main__':
    cameras = camera_connection.connect_manage_cameras()
    print(cameras.get_connected_cameras_by_id())
    i = ImageManager('user', None, cameras)
    i.start()
