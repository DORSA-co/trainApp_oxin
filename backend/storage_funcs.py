import shutil
import os
import subprocess
import string
from sys import platform
import psutil


# show storage status summary on dashboard, need to bugfix
def get_storage_status(disk_path):
    """
    this function is used to get storage statues of one drive

    Args:
        disk_path (_type_): drive path (in string)

    Returns:
        drive_info: in dict
    """

    try:
        total, used, free = shutil.disk_usage(disk_path)
        # Get the current working directory

        total = total/(2**30)
        free = free/(2**30)
        used = used/(2**30)
        drive_info = {'total': total, 'used': used, 'used_perc': used/total, 'free': free}
    
    except:
        drive_info = {'total': 0, 'used': 0, 'used_perc': 0, 'free': 0}
    
    return drive_info

# get available drives on windows
def get_available_drives():
    """
    this function is used to get system available drives list

    Args: None

    Returns:
        available_drives: in list
    """
    # on linux
    available_drives = []
    if platform == "linux" or platform == "linux2":
        for drive in psutil.disk_partitions():
            if '/media/' in drive.mountpoint and drive.device.startswith('/dev/sda'):
                available_drives.append(drive.mountpoint)
    
    # on windows
    else:
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    return available_drives





    