# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme,FluentWindow,
                            NavigationAvatarWidget,  SplitFluentWindow, FluentTranslator)
from qfluentwidgets import FluentIcon as FIF
from view.main_1_interface import Main_face
from view.cap_2_interface import Cap_face
from view.detect_3_interface import Detect_face
from view.seg_4_interface import Seg_face
from view.analyse_5_interface import Analyse_face
from view.payment_6_interface import Payment_face
class Window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.cap_face = Cap_face(self)
        self.main_face = Main_face(self)
        self.detect_face = Detect_face(self)
        self.seg_face = Seg_face(self)
        self.analy_face = Analyse_face(self)
        self.payment_face = Payment_face(self)
        self.initWindow()
        self.initNavigation()

    def initNavigation(self):
        self.addSubInterface(self.main_face, FIF.HOME, '个人中心')
        self.addSubInterface(self.cap_face, FIF.ALBUM, '拍摄舌苔')
        self.addSubInterface(self.detect_face, FIF.PHOTO, '检测舌苔')
        self.addSubInterface(self.seg_face, FIF.TILES, '分割检测')
        self.addSubInterface(self.analy_face,FIF.PIE_SINGLE, '检测结果')
        self.addSubInterface(self.payment_face,FIF.SHOPPING_CART, '套餐购买')

    def initWindow(self):
        self.resize(960, 700)
        self.setWindowTitle('智能感应镜')
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
