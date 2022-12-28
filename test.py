import os
import glob
import base64
from sys import platform
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6 import QtWidgets as sQtWidgets
from PySide6 import QtGui as sQtGui
from PySide6 import QtCore as sQtCore
from PySide6.QtCore import Signal as sSignal

import texts

# default timeout and level for notif
TIMEOUT = 5000
LEVEL = 0


class NotificationIcon:

    Info, Success, Warning, Error, Close = range(5)
    
    Types = {
        Info: None,
        Success: None,
        Warning: None,
        Error: None,
        Close: None
    }

    @classmethod
    def init(cls):
        cls.Types[cls.Info] = sQtGui.QPixmap(sQtGui.QImage.fromData(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC5ElEQVRYR8VX0VHbQBB9e/bkN3QQU0FMBSEVYFcQ8xPBJLJ1FWAqOMcaxogfTAWQCiAVRKkgTgfmM4zRZu6QhGzL0p0nDPr17e7bt7tv14RX/uiV48MJgAon+8TiAMRtMFogaqUJxADPwRRzg67kl8+xbWJWANR40iPQSSFgtX/mGQkaDr56V3VAKgGos4s2JXwJoF3naMPvMS+SrpTHs032GwGkdF+DsFMVnJm/oyGGeHico0EjIjpYes+YMyVd6R/flfkpBWCCQ9zaZM2LZDfLMGXsZ5kdI/lYBmINgHHyyLd1mWdBbAFAM/GY7K2WYx1AeB4T6L1N9umbGxZ0qktATaEAdCps48D39oq/LwEw3U5CN92LfczJoewfT7MAywDCaEbAuxeLrh0zz4L+0e4aAJfGy+sP3IMxlH1vpMJoSMCJDXgWtJeJVc6ACs9HBBrYODCJAFdYvAmkPJxnNqMwYht7Bn+T/lGg3z4DGEd3RPhQ54DBvwAOVkeqagRXfTLjh+x7+8sALOtfHLuiYzWOAiLoKbD58mnIGbCmLxUepS6NQmYlUGE0JeCTTXT9JvA9E9sZgO5iIpoyc6/YzcqSwQzgGgBXB7oXpH9klpRSkxY1xW/b7Iu2zk34PILPnazCqEPAtTWA8iZ0HsOu9L0bw4DzCJeNocMGNDpQ3IKO+6NUiJ4ysZNiBv5I3zPnmJmG5oM+wbS+9+qkvGi7NAXGmeUy0ioofa+XA0jH0UaMKpdRWs/adcwMqfV/tenqpqHY/Znt+j2gJi00RUzA201dXaxh9iZdZloJS+9H1otrkbRrD5InFqpPskxEshJQ468CkSmJC+i1HigaaxCAuCljgoDhwPdOjf7rFVxxuJrMkXScjtKc1rOLNpJk6nii5XmYzbngzlZn+RIb40kPJPTBYXUt6VEDJ8Pi6bWpNFb/jFYY6YGpDeKdjBmTKdMcxDGEmP73v2a2Gr/NOycGtglQZ/MPzEqCMLGckJEAAAAASUVORK5CYII=')))
        cls.Types[cls.Success] = sQtGui.QPixmap(sQtGui.QImage.fromData(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACZUlEQVRYR8VXS3LTQBDtVsDbcAPMCbB3limkcAKSG4QFdnaYE2BOQLKzxSLJCeAGSUQheSnfwLmB2VJhXmpExpFHI2sk2RWv5FJPv9evP9NieuIfPzE+VSJw8qt3IMDvmahDoDYxt2UAACXMWIIowR5ffn8TJbaBWRE4CXvHAH9RgKXOgQUI48CfXZbZbiTw8Xe/w3d0zkydMkem91IZpyWOJu5sUXS+kEAqt3B+MNOLOuDqDEBLxxFHk7eza5MfIwEJDjhXTYD1s8zinYlEjsCD7FdNI9cJpEq0RFdPR47AMOzLCn69zegz6UgCP+pmfa8RSKudnPNdgCufTOLDxJtdPP7PoA1Cd8HEL5sSUCCD0B0x8bc1f8Bi6sevcgS2VXh6hMOwDz0gsUddNaxWKRjeuKfE/KlJ9Dq4UYH/o/Ns6scj+bgiMAjdayb26xLQwTfVEwg3gRcf6ARq578KuLo7VDc8psCQqwfjr4EfjYvkrAquFJ56UYpdSkAZSmNd1rrg0leOQFELgvA58OJTxVyRaAJORPOpF6UXnFUR5sDiXjs7UqsOMGMRlrWhTkJXpFL3mNrQZhA1lH3F0TiI5FurUQyMpn58VjhkSqQA4Tbw4nSVW6sBU5VXktXSeONlJH3s8jrOVr9RgVSFuNcWfzlh5n3LoKzMAPxxWuiULiQpiR2sZNnCyzIuWUr5Z1Ml0sgdHFZaShVDuR86/0huL3VXtDk/F4e11vKsTHLSCeKx7bYkW80hjLOrV1GhWH0ZrSlyh2MwdZhYfi8oZeYgLBmUiGd8sfVPM6syr2lUSYGaGBuP3QN6rVUwYV/egwAAAABJRU5ErkJggg==')))
        cls.Types[cls.Warning] = sQtGui.QPixmap(sQtGui.QImage.fromData(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACmElEQVRYR8VXTW7TUBD+xjYSXZFukOIsSE9AskNJJMoJmq4r7OYEwAkabhBOkB/Emt4gVIojdpgbpIumEitX6gKB7UHPkauXxLHfc4F6Z3l+vvnmm/fGhAd+6IHzQwvA9cfOITMfAdQAcx1EdVEAM/tEFADsWyaPn57MfdXClABcT1qnzHSWJiwMzrwgoF91vXGRbS6AH59ajd8hDYmoURQo67tgxoij42rv62KX/04Agu44xmciVMokT32YERgGjquvZ1+y4mQCWPUa0/sk3vQlwqssEFsAVrQbU4XKL/ai2+5PPK6waQ4AOsoDnDARh83NdmwBuJq0fQI9L6p+L7rd3+/5gbAToMPI+FbkIzRRc72mbLcGIFE7jGFRIPHddmZrvstJh1X8CHGv6sxHqe1GkPYCoGcqgcoCAPPCdr2DLQC6wqMoPEj7qdqCNKllxs30sLpjYDluDUDGG5XqhY2sal3w4PiD7c7fJnHShMtJR8zpy/8CALiwndnhBgD1/t+XAXkaZAaUVHwnHulg0W6BNEWlAQD8zna8gQB0Ne70iXCm2j55jCUAei1gxvuaO+uXAcDg7zXHSy640iKUAehOEDJFqDmGQkiPLO5Fv+KADXOqvCuIsrPGsIyQdHou22YeRMJgOdHTQTkAfGk7XrLKrWlAvOhcRgBfWiZ3RQti0zxXuUFXCXMuo0TRitfxugjbIxC5RYzI6s9kIGFh+KLOpiW22id5AUuI8IaisFG4kCQg/sFKJgtPLix3KWXGeRETRbQDuCFCV2spTYMm+2FEI1WBbYIRPTeiqFtqLZeDraaD+qrbkpgQAvfl1WsXU0p/RjIjYYhTkNFgcCVlRlRKoAAc+5aF0V//NVPoc2kTLQZKZ8lx/AMXBmMwuXUwOAAAAABJRU5ErkJggg==')))
        cls.Types[cls.Error] = sQtGui.QPixmap(sQtGui.QImage.fromData(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACrklEQVRYR82XW27aQBSG/4PtiNhIpStouoImKwjZAV1B07coWCpZQcgK6kh2lLeSFZSsIOwgdAdkBaUSEBQDpxpjU9vM+EJR03nDzJz/mzm3GcIrD3plfZQCeD47O1ho2jERNRmoE9AQG2BgBGBAwIiZe5Zh3JPjiG+5oxCAEF5q2iWITnMtRhOYu5XF4mr/9naYtSYXYGLbHQCXhYVTEwlom657rVqvBOB2uz71/a+ldq1SYe6ahnEhc4sSYGzbfQKOt915eh0D/ZrrnqS/SwEmrVYXRJ92Jb4OC+C65rrtuN0NgIltNwF837V4zN5Hy3V70e9NgFZrCKJ3CQDmJ9MwDsW36XzeB/AhA/CHqeuN2WxWX2paX2JraHneeynA+Pz8lCqVbxLjV5brimxAEJxqiEA8CjZVBvFy+bl2c9MV9hInoAw85qFpGEeRYQVEQjzMokcQHWxsiPne8jzh6j8AodGfyqNlHpiGcaKAkIk/gChwm2yYuv5W2FqfwLNtN5bAQ2bwySB83zENo50A8/1McaFRAU72XVek+mpk+D/JlIKI/xkee654uCbIhjVAqZIrgSgpLhiCwN4OAEj4vEB2yDybBCjsAol4ZD0nRdMQSRcUCsKUeNSw4o2mKMRGEOamoVx8FXDZKVosDYNMUHXAsBRnppo8RQcbpTgIGEkhykpFjnWxzGhPQYxt2yHgS/oIlKVYTJxImpG482nz+VG1Wh1N84pMCCGa0ULXHwmoJwCYnyzPW5fn/68dh7EgPbrMMl3gz7gro+n/7EoWD7w4a96l1NnJ1Yz5Lt6wCgFEk0r1CIkbiPnC9DxH5aHcd4FYGD5MOqVOg/muslh0/vphkm63k5eXZvA0I6qD+ZCI3jDzLxANiHn1NNvb6+30aVYgwLeeUsgFW1svsPA3Ncq4MHzVeO8AAAAASUVORK5CYII=')))
        cls.Types[cls.Close] = sQtGui.QPixmap(sQtGui.QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeElEQVQ4T2NkoBAwUqifgboGzJy76AIjE3NCWmL0BWwumzV/qcH/f38XpCfHGcDkUVwAUsDw9+8GBmbmAHRDcMlheAGbQnwGYw0DZA1gp+JwFUgKZyDCDQGpwuIlrGGAHHAUGUCRFygKRIqjkeKERE6+oG5eIMcFAOqSchGwiKKAAAAAAElFTkSuQmCC')))

    @classmethod
    def icon(cls, ntype):
        return cls.Types.get(ntype)


class NotificationItem(sQtWidgets.QWidget):

    closed = sSignal(sQtWidgets.QListWidgetItem)

    def __init__(self, title, message, font_size, font_style, timeout, item, *args, ntype=0, callback=None, **kwargs):
        super(NotificationItem, self).__init__(*args, **kwargs)
        self.item = item
        self.callback = callback
        layout = sQtWidgets.QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.bgWidget = sQtWidgets.QWidget(self)  # 背景控件, 用于支持动画效果
        layout.addWidget(self.bgWidget)

        layout = sQtWidgets.QGridLayout(self.bgWidget)
        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(10)

        # 标题左边图标
        layout.addWidget(
            QLabel(self, pixmap=NotificationIcon.icon(ntype)), 0, 0)

        # 标题
        self.labelTitle = sQtWidgets.QLabel(title, self)
        font = self.labelTitle.font()
        font.setBold(True)
        font.setPixelSize(font_size+3)
        font.setFamily(font_style)
        self.labelTitle.setFont(font)

        # 关闭按钮
        self.labelClose = sQtWidgets.QLabel(
            self, cursor=sQtCore.Qt.PointingHandCursor, pixmap=NotificationIcon.icon(NotificationIcon.Close))

        # 消息内容
        self.labelMessage = sQtWidgets.QLabel(
            message, self, cursor=sQtCore.Qt.PointingHandCursor, wordWrap=True, alignment=Qt.AlignLeft | Qt.AlignTop)
        font = self.labelMessage.font()
        font.setPixelSize(font_size)
        font.setFamily(font_style)
        self.labelMessage.setFont(font)
        self.labelMessage.adjustSize()

        # 添加到布局
        layout.addWidget(self.labelTitle, 0, 1)
        layout.addItem(sQtWidgets.QSpacerItem(
            40, 20, sQtWidgets.QSizePolicy.Expanding, sQtWidgets.QSizePolicy.Minimum), 0, 2)
        layout.addWidget(self.labelClose, 0, 3)
        layout.addWidget(self.labelMessage, 1, 1, 1, 2)

        # 边框阴影
        effect = sQtWidgets.QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setColor(sQtGui.QColor(0, 0, 0, 25))
        effect.setOffset(0, 2)
        self.setGraphicsEffect(effect)

        self.adjustSize()

        # 5秒自动关闭
        self._timer = sQtCore.QTimer(self, timeout=self.doClose)
        self._timer.setSingleShot(True)  # 只触发一次
        self._timer.start(timeout)

    def doClose(self):
        try:
            # 可能由于手动点击导致item已经被删除了
            self.closed.emit(self.item)
        except:
            pass

    def showAnimation(self, width):
        # 显示动画
        pass

    def closeAnimation(self):
        # 关闭动画
        pass

    def mousePressEvent(self, event):
        super(NotificationItem, self).mousePressEvent(event)
        w = self.childAt(event.pos())
        if not w:
            return
        if w == self.labelClose:  # 点击关闭图标
            # 先尝试停止计时器
            self._timer.stop()
            self.closed.emit(self.item)
        elif w == self.labelMessage and self.callback and callable(self.callback):
            # 点击消息内容
            self._timer.stop()
            self.closed.emit(self.item)
            self.callback()  # 回调

    def paintEvent(self, event):
        # 圆角以及背景色
        super(NotificationItem, self).paintEvent(event)
        painter = sQtGui.QPainter(self)
        path = sQtGui.QPainterPath()
        path.addRoundedRect(sQtCore.QRectF(self.rect()), 6, 6)
        painter.fillPath(path, sQtCore.Qt.white)


class NotificationWindow(sQtWidgets.QListWidget):

    _instance = None

    def __init__(self, *args, **kwargs):
        super(NotificationWindow, self).__init__(*args, **kwargs)
        self.setSpacing(8)
        self.setMinimumWidth(412)
        self.setMaximumWidth(412)
        QApplication.instance().setQuitOnLastWindowClosed(True)
        # 隐藏任务栏,无边框,置顶等
        self.setWindowFlags(self.windowFlags() | sQtCore.Qt.Tool |
                            sQtCore.Qt.FramelessWindowHint | sQtCore.Qt.WindowStaysOnTopHint)
        # 去掉窗口边框
        self.setFrameShape(self.NoFrame)
        # 背景透明
        self.viewport().setAutoFillBackground(False)
        self.setAttribute(sQtCore.Qt.WA_TranslucentBackground, True)
        # 不显示滚动条
        self.setVerticalScrollBarPolicy(sQtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(sQtCore.Qt.ScrollBarAlwaysOff)
        # 获取屏幕高宽
        #rect = QApplication.instance().desktop().availableGeometry(self)
        rect = self.window().screen().geometry()

        self.setMinimumHeight(rect.height())
        self.setMaximumHeight(rect.height())
        self.move(rect.width() - self.minimumWidth() - 18, 0)

    def removeItem(self, item):
        # 删除item
        w = self.itemWidget(item)
        self.removeItemWidget(item)
        item = self.takeItem(self.indexFromItem(item).row())
        w.close()
        w.deleteLater()
        del item

    @classmethod
    def _createInstance(cls):
        # 创建实例
        if not cls._instance:
            cls._instance = NotificationWindow()
            cls._instance.show()
            NotificationIcon.init()

    @classmethod
    def info(cls, title, message, font_size, font_style, timeout, callback=None):
        cls._createInstance()
        item = sQtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, font_size, font_style, timeout, item, cls._instance,
                             ntype=NotificationIcon.Info, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(sQtCore.QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def success(cls, title, message, font_size, font_style, timeout, callback=None):
        cls._createInstance()
        item = sQtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, font_size, font_style, timeout, item, cls._instance,
                             ntype=NotificationIcon.Success, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(sQtCore.QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def warning(cls, title, message, font_size, font_style, timeout, callback=None):
        cls._createInstance()
        item = sQtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, font_size, font_style, timeout, item, cls._instance,
                             ntype=NotificationIcon.Warning, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(sQtCore.QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def error(cls, title, message, font_size, font_style, timeout, callback=None):
        cls._createInstance()
        item = sQtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, font_size, font_style, timeout, item,
                             ntype=NotificationIcon.Error, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        width = cls._instance.width() - cls._instance.spacing()
        item.setSizeHint(sQtCore.QSize(width, w.height()))
        cls._instance.setItemWidget(item, w)


def callback():
    pass



class Notification_manager():
    """
    this class is used to manage and crate nottifications

    Args:
        message:
        level:

    Returns: None
    """

    def __init__(self, ui_obj, notif_mainfolderpath='./notifications', notifs_prefix='notification_', file_format='.txt', seprator=':::'):
        """
        this function is used to init notifcation manager classs

        Args:
            ui_obj (_type_): main ui object
            notif_mainfolderpath (str, optional): main folder path to store notification files. Defaults to './notifications'.
            notifs_prefix (str, optional): notification files prefix. Defaults to 'notification_'.
            file_format (str, optional): format of notification file. Defaults to '.txt'.
            seprator (str, optional): seprator for notification message, level and timeout. Defaults to ':::'.
        
        Returns: None
        """

        self.main_folderpath = notif_mainfolderpath
        self.notifs_prefix = notifs_prefix
        self.file_format = file_format
        self.seprator = seprator
        self.ui_obj = ui_obj

        # create main folder if not exist
        try:
            if not os.path.exists(self.main_folderpath):
                os.mkdir(self.main_folderpath)
            #
            self.ui_obj.logger.create_new_log(message=texts.MESSEGES['initialize_notif_ui']['en'], level=1)
            
        except:
            self.ui_obj.logger.create_new_log(message=texts.ERRORS['initialize_notif_ui_failed']['en'], level=5)

    def get_files_in_path(self, dir_path, reverse=False):
        """
        this function is used to get all files in a path, sorted by date (old to new)

        Args:
            dir_path (_type_): _description_
            reverse (bool, optional): a boolean to reverse sorting to new to old. Defaults to False.

        Returns:
            file_paths: list of file pathes
        """

        while True:
            try:
                file_paths = sorted(Path(dir_path).iterdir(), key=os.path.getmtime, reverse=reverse)
                break
            except:
                continue
        
        return file_paths
    
    def clear_directory(self):
        """
        this function is used to remove all files in notfication directory, mainly on app startup

        Args: None

        Returns: None
        """

        try:
            files = glob.glob(os.path.join(self.main_folderpath, '*'))
            for f in files:
                os.remove(f)

        except:
            self.ui_obj.logger.create_new_log(message=texts.ERRORS['notif_obj_clear_files_failed']['en'], level=5)
            return

    
    def append_new_notif(self, message, level=LEVEL, timeout=TIMEOUT):
        """
        this function is used to append a new notification in .txt format in notifications directory

        Args:
            message (string): notification message
            level (int, optional): an in between [0, 3] determning the level of message. Defaults to 0.
                0: info
                1: success
                2: warning
                3: error
            timeout (int, optional): timeout to close notifaication (in milisecondes)
        
        Returns: None
        """
        
        itr = 0
        timeout = 1000 if timeout <= 1000 else timeout

        try:
            while True:
                file_path = os.path.join(self.main_folderpath, self.notifs_prefix+str(itr)+self.file_format)

                # a file exists by this name
                if os.path.exists(file_path):
                    itr+=1

                else:
                    open(file_path, mode='a').close()
                    # write notif text in file
                    with open(file_path, mode='w') as file:
                        file.write(message + self.seprator + str(level) + self.seprator + str(timeout)) # message:::level:::timeout
                    file.close()

                    break
        
        except:
            self.ui_obj.logger.create_new_log(message=texts.ERRORS['notif_obj_append_file_failed']['en'], level=5)
            return

    
    def pop_and_create_new_notif(self, font_size=10, font_style='Arial'):
        """
        this function is used to read a new notification file (oldest one in notifications directory) and show it

        Args:
            font_size (int, optional): _description_. Defaults to 10.
            font_style (str, optional): _description_. Defaults to 'Arial'.

        Returns: None
        """

        try:
            # get notification file pathes
            file_paths = self.get_files_in_path(dir_path=self.main_folderpath, reverse=False)
            if len(file_paths) == 0:
                return

            # open file and read notification message
            with open(file_paths[0], 'r') as file:
                content = file.readline()
            file.close()

            content = content.split('\n', 1)[0].split(':::')
            message = ''
            level = LEVEL
            timeout = TIMEOUT
            #
            try:
                message = content[0]
                level = int(content[1]) if len(content)>1 else LEVEL
                timeout = int(content[2]) if len(content)>2 else TIMEOUT
            
            except:
                pass
                
            # delete file
            os.remove(file_paths[0])

            # create notification
            if message != '' and not message.isspace():
                self.create_new_notif(ui_obj=self.ui_obj, massage=message, font_size=font_size, font_style=font_style, level=level, timeout=timeout)

        except:
            self.ui_obj.logger.create_new_log(message=texts.ERRORS['notif_obj_pop_file_failed']['en'], level=5)
            return


    def create_new_notif(self, ui_obj, massage='message', font_size=10, font_style='Arial', level=LEVEL, timeout=TIMEOUT):
        """
        this function is used to create a new notification

        Args:
            message (str, optional): message text. Defaults to 'message'.
            font_size (int, optional):
            font_style (int, optional):
            level (int, optional): an in between [0, 3] determning the level of message. Defaults to 0.
                0: info
                1: success
                2: warning
                3: error
            timeout (int, optional): timeout to close notifaication (in milisecondes)
        
        Returns: None
        """

        timeout = 1000 if timeout <= 1000 else timeout
        
        # on linux
        if platform == "linux" or platform == "linux2":
            # info
            if level == 0:
                cmd = "notify-send '%s' '%s' -u low -t %s -i hint" % (texts.MESSEGES['info_notif'][ui_obj.language], massage, timeout)
            
            # success
            elif level == 1:
                cmd = "notify-send '%s' '%s' -u normal -t %s -i dialog-apply" % (texts.MESSEGES['success_notif'][ui_obj.language], massage, timeout)
            
            # warning
            elif level == 2:
                cmd = "notify-send '%s' '%s' -u critical -t %s -i empathy-away" % (texts.MESSEGES['warning_notif'][ui_obj.language], massage, timeout)
            
            # error
            elif level == 3:
                cmd = "notify-send '%s' '%s' -u critical -t %s -i gtk-stop" % (texts.ERRORS['error_notif'][ui_obj.language], massage, timeout)
            
            # else
            else:
                cmd = "notify-send '%s' '%s' -u normal -t %s -i hint" % (texts.MESSEGES['info_notif'][ui_obj.language], massage, timeout)
            
            # run command
            os.system(cmd)
            

        
        # on windows
        else:

            # increase font size
            try:
                font_size += 5
            except:
                font_size = int(font_size)
                font_size += 5

            # info
            if level == 0:
                NotificationWindow.info(texts.MESSEGES['info_notif'][ui_obj.language], massage, font_size, font_style, timeout, callback=callback)

            # success
            elif level == 1:
                NotificationWindow.success(texts.MESSEGES['success_notif'][ui_obj.language], massage, font_size, font_style, timeout, callback=callback)

            # warning
            elif level == 2:
                NotificationWindow.warning(texts.WARNINGS['warning_notif'][ui_obj.language], massage, font_size, font_style, timeout, callback=callback)

            # error
            elif level == 3:
                NotificationWindow.error(texts.ERRORS['error_notif'][ui_obj.language], massage, font_size, font_style, timeout, callback=callback)

            # else
            else:
                NotificationWindow.info(texts.MESSEGES['info_notif'][ui_obj.language], massage, font_size, font_style, timeout, callback=callback)
