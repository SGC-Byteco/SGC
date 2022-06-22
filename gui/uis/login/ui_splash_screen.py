# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSuuKIP.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMinimumSize(QSize(300, 300))
        SplashScreen.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.contenedorS = QFrame(self.centralwidget)
        self.contenedorS.setObjectName(u"contenedorS")
        self.contenedorS.setFrameShape(QFrame.NoFrame)
        self.contenedorS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contenedorS)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.contenedorS)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame {\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	font: 9pt \"Segoe UI\";\n"
"	border-radius: 120px;\n"
"}")
        self.circle_bg.setFrameShape(QFrame.StyledPanel)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 180))
        self.texts.setStyleSheet(u"background:none;")
        self.texts.setFrameShape(QFrame.StyledPanel)
        self.texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.texts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.titulo = QLabel(self.texts)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMinimumSize(QSize(0, 30))
        self.titulo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.texts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.cargando = QLabel(self.frame_2)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(-1, -1, 100, 22))
        self.cargando.setMinimumSize(QSize(100, 22))
        self.cargando.setMaximumSize(QSize(100, 22))
        self.cargando.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1, Qt.AlignHCenter)

        self.Version = QLabel(self.texts)
        self.Version.setObjectName(u"Version")
        self.Version.setMinimumSize(QSize(100, 24))
        self.Version.setMaximumSize(QSize(100, 24))
        self.Version.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(68, 71, 90);\n"
"	color: rgb(151, 159, 200);\n"
"	border-radius: 12px;\n"
"}")
        self.Version.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Version, 3, 0, 1, 1, Qt.AlignHCenter)

        self.vacio = QFrame(self.texts)
        self.vacio.setObjectName(u"vacio")
        self.vacio.setMinimumSize(QSize(0, 80))
        self.vacio.setFrameShape(QFrame.StyledPanel)
        self.vacio.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.vacio, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.texts)


        self.verticalLayout_2.addWidget(self.circle_bg)


        self.verticalLayout.addWidget(self.contenedorS)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Cargando...", None))
        self.titulo.setText(QCoreApplication.translate("SplashScreen", u"S.G.C desktop Edition.", None))
        self.cargando.setText(QCoreApplication.translate("SplashScreen", u"Cargando...", None))
        self.Version.setText(QCoreApplication.translate("SplashScreen", u"Version 1.0.0", None))
    # retranslateUi

