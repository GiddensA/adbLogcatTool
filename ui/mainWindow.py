from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils.UIUtils import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        displaySize = GetWindowSize()
        self.setupUi(self, (displaySize[0] / 3, displaySize[1] * 3 / 5))

    def setupUi(self, MainWindow, windowSize):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(windowSize[0], windowSize[1])
        MainWindow.setMaximumSize(windowSize[0], windowSize[1])
        MainWindow.setMinimumSize(windowSize[0], windowSize[1])

        self.action_general_settings = QAction(MainWindow)
        self.action_general_settings.setObjectName(u"action_general_settings")
        self.action_log_level_settings = QAction(MainWindow)
        self.action_log_level_settings.setObjectName(u"action_log_level_settings")
        self.action_refresh_device_list = QAction(MainWindow)
        self.action_refresh_device_list.setObjectName(u"action_refresh_device_list")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, windowSize[0], windowSize[1]))
        self.verticalLayout_main = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_device = QHBoxLayout()
        self.horizontalLayout_device.setObjectName(u"horizontalLayout_device")
        self.horizontalLayout_device.setContentsMargins(10, 0, 10, -1)
        self.label_device = QLabel(self.verticalLayoutWidget)
        self.label_device.setObjectName(u"label_device")

        self.horizontalLayout_device.addWidget(self.label_device)

        self.comboBox_device_list = QComboBox(self.verticalLayoutWidget)
        self.comboBox_device_list.setObjectName(u"comboBox_device_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_device_list.sizePolicy().hasHeightForWidth())
        self.comboBox_device_list.setSizePolicy(sizePolicy)

        self.horizontalLayout_device.addWidget(self.comboBox_device_list)

        self.verticalLayout_device_buttom = QVBoxLayout()
        self.verticalLayout_device_buttom.setObjectName(u"verticalLayout_device_buttom")
        self.pushButton_root = QPushButton(self.verticalLayoutWidget)
        self.pushButton_root.setObjectName(u"pushButton_root")

        self.verticalLayout_device_buttom.addWidget(self.pushButton_root)

        self.pushButton_kill_cam = QPushButton(self.verticalLayoutWidget)
        self.pushButton_kill_cam.setObjectName(u"pushButton_kill_cam")

        self.verticalLayout_device_buttom.addWidget(self.pushButton_kill_cam)


        self.horizontalLayout_device.addLayout(self.verticalLayout_device_buttom)


        self.verticalLayout_main.addLayout(self.horizontalLayout_device)

        self.tabWidget_main = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tab_log_level = QWidget()
        self.tab_log_level.setObjectName(u"tab_log_level")
        self.tabWidget_main.addTab(self.tab_log_level, "")
        self.tabWidget_main.setCurrentWidget(self.tab_log_level)
        self.tab_log_pull = QWidget()
        self.tab_log_pull.setObjectName(u"tab_log_pull")
        self.tabWidget_main.addTab(self.tab_log_pull, "")

        self.verticalLayout_main.addWidget(self.tabWidget_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, windowSize[0], 22))
        self.menu_setting = QMenu(self.menubar)
        self.menu_setting.setObjectName(u"menu_setting")
        self.menu_device = QMenu(self.menubar)
        self.menu_device.setObjectName(u"menu_device")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_device.menuAction())
        self.menu_setting.addAction(self.action_general_settings)
        self.menu_setting.addAction(self.action_log_level_settings)
        self.menu_device.addAction(self.action_refresh_device_list)

        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"adb logcat tool", None))
        self.action_general_settings.setText(QCoreApplication.translate("MainWindow", u"\u901a\u7528\u8bbe\u7f6e", None))
        self.action_log_level_settings.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790log\u7b49\u7ea7\u8bbe\u7f6e", None))
        self.action_refresh_device_list.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u8bbe\u5907\u5217\u8868", None))
        self.label_device.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u5217\u8868", None))
        self.pushButton_root.setText(QCoreApplication.translate("MainWindow", u"root & remount", None))
        self.pushButton_kill_cam.setText(QCoreApplication.translate("MainWindow", u"kill Camera server", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_log_level), QCoreApplication.translate("MainWindow", u"log\u7b49\u7ea7\u8bbe\u7f6e", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_log_pull), QCoreApplication.translate("MainWindow", u"log\u62c9\u53d6", None))
        self.menu_setting.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu_device.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907", None))
    # retranslateUi
