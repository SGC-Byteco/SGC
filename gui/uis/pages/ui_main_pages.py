# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesmpWnUM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 581)
        self.verticalLayout_7 = QVBoxLayout(MainPages)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setEnabled(True)
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 214, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalWidget = QWidget(self.page_4)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Titulo_Datos_empresa = QLabel(self.verticalWidget)
        self.Titulo_Datos_empresa.setObjectName(u"Titulo_Datos_empresa")
        self.Titulo_Datos_empresa.setFont(font)
        self.Titulo_Datos_empresa.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Titulo_Datos_empresa)

        self.Layout_Datos_empresa1 = QVBoxLayout()
        self.Layout_Datos_empresa1.setObjectName(u"Layout_Datos_empresa1")

        self.verticalLayout_2.addLayout(self.Layout_Datos_empresa1)

        self.Layout_Datos_empresa2 = QVBoxLayout()
        self.Layout_Datos_empresa2.setObjectName(u"Layout_Datos_empresa2")

        self.verticalLayout_2.addLayout(self.Layout_Datos_empresa2)


        self.verticalLayout_3.addWidget(self.verticalWidget)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.page_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"background-color: transparent;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 832, 553))
        self.scrollAreaContents.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Datos_de_la_empresa = QLabel(self.scrollAreaContents)
        self.Datos_de_la_empresa.setObjectName(u"Datos_de_la_empresa")
        self.Datos_de_la_empresa.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"")
        self.Datos_de_la_empresa.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Datos_de_la_empresa)

        self.layout_label = QHBoxLayout()
        self.layout_label.setSpacing(60)
        self.layout_label.setObjectName(u"layout_label")
        self.layout_label.setContentsMargins(20, -1, 20, -1)
        self.labelEmpresa_nombre = QLabel(self.scrollAreaContents)
        self.labelEmpresa_nombre.setObjectName(u"labelEmpresa_nombre")
        font1 = QFont()
        font1.setPointSize(9)
        self.labelEmpresa_nombre.setFont(font1)
        self.labelEmpresa_nombre.setStyleSheet(u"")

        self.layout_label.addWidget(self.labelEmpresa_nombre)

        self.labelEmpresa_razon_social = QLabel(self.scrollAreaContents)
        self.labelEmpresa_razon_social.setObjectName(u"labelEmpresa_razon_social")
        self.labelEmpresa_razon_social.setFont(font1)
        self.labelEmpresa_razon_social.setStyleSheet(u"")

        self.layout_label.addWidget(self.labelEmpresa_razon_social)

        self.labelEmpresa_direccion = QLabel(self.scrollAreaContents)
        self.labelEmpresa_direccion.setObjectName(u"labelEmpresa_direccion")
        self.labelEmpresa_direccion.setFont(font1)
        self.labelEmpresa_direccion.setStyleSheet(u"")

        self.layout_label.addWidget(self.labelEmpresa_direccion)


        self.verticalLayout_6.addLayout(self.layout_label)

        self.datosEmpresa = QHBoxLayout()
        self.datosEmpresa.setSpacing(60)
        self.datosEmpresa.setObjectName(u"datosEmpresa")
        self.datosEmpresa.setContentsMargins(20, 0, 20, -1)
        self.datosEmpresa_nombre = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_nombre.setObjectName(u"datosEmpresa_nombre")
        self.datosEmpresa_nombre.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa.addWidget(self.datosEmpresa_nombre)

        self.datosEmpresa_razon_social = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_razon_social.setObjectName(u"datosEmpresa_razon_social")
        self.datosEmpresa_razon_social.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa.addWidget(self.datosEmpresa_razon_social)

        self.datosEmpresa_direccion = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_direccion.setObjectName(u"datosEmpresa_direccion")
        self.datosEmpresa_direccion.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa.addWidget(self.datosEmpresa_direccion)


        self.verticalLayout_6.addLayout(self.datosEmpresa)

        self.layout_label_2 = QHBoxLayout()
        self.layout_label_2.setSpacing(60)
        self.layout_label_2.setObjectName(u"layout_label_2")
        self.layout_label_2.setContentsMargins(20, -1, 20, -1)
        self.labelEmpresa_telefono = QLabel(self.scrollAreaContents)
        self.labelEmpresa_telefono.setObjectName(u"labelEmpresa_telefono")
        self.labelEmpresa_telefono.setFont(font1)
        self.labelEmpresa_telefono.setStyleSheet(u"")

        self.layout_label_2.addWidget(self.labelEmpresa_telefono)

        self.labelEmpresa_tipo_regimen = QLabel(self.scrollAreaContents)
        self.labelEmpresa_tipo_regimen.setObjectName(u"labelEmpresa_tipo_regimen")
        self.labelEmpresa_tipo_regimen.setFont(font1)
        self.labelEmpresa_tipo_regimen.setStyleSheet(u"")

        self.layout_label_2.addWidget(self.labelEmpresa_tipo_regimen)

        self.labelEmpresa_nit = QLabel(self.scrollAreaContents)
        self.labelEmpresa_nit.setObjectName(u"labelEmpresa_nit")
        self.labelEmpresa_nit.setFont(font1)
        self.labelEmpresa_nit.setStyleSheet(u"")

        self.layout_label_2.addWidget(self.labelEmpresa_nit)


        self.verticalLayout_6.addLayout(self.layout_label_2)

        self.datosEmpresa1 = QHBoxLayout()
        self.datosEmpresa1.setSpacing(60)
        self.datosEmpresa1.setObjectName(u"datosEmpresa1")
        self.datosEmpresa1.setContentsMargins(20, 0, 20, -1)
        self.datosEmpresa_telefono = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_telefono.setObjectName(u"datosEmpresa_telefono")
        self.datosEmpresa_telefono.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa1.addWidget(self.datosEmpresa_telefono)

        self.datosEmpresa_tipo_regimen = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_tipo_regimen.setObjectName(u"datosEmpresa_tipo_regimen")
        self.datosEmpresa_tipo_regimen.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa1.addWidget(self.datosEmpresa_tipo_regimen)

        self.datosEmpresa_nit = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_nit.setObjectName(u"datosEmpresa_nit")
        self.datosEmpresa_nit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa1.addWidget(self.datosEmpresa_nit)


        self.verticalLayout_6.addLayout(self.datosEmpresa1)

        self.layout_label_3 = QHBoxLayout()
        self.layout_label_3.setSpacing(60)
        self.layout_label_3.setObjectName(u"layout_label_3")
        self.layout_label_3.setContentsMargins(20, -1, 20, -1)
        self.labelEmpresa_departamento = QLabel(self.scrollAreaContents)
        self.labelEmpresa_departamento.setObjectName(u"labelEmpresa_departamento")
        self.labelEmpresa_departamento.setFont(font1)
        self.labelEmpresa_departamento.setStyleSheet(u"")

        self.layout_label_3.addWidget(self.labelEmpresa_departamento)

        self.labelEmpresa_municipio = QLabel(self.scrollAreaContents)
        self.labelEmpresa_municipio.setObjectName(u"labelEmpresa_municipio")
        self.labelEmpresa_municipio.setFont(font1)
        self.labelEmpresa_municipio.setStyleSheet(u"")

        self.layout_label_3.addWidget(self.labelEmpresa_municipio)


        self.verticalLayout_6.addLayout(self.layout_label_3)

        self.datosEmpresa3 = QHBoxLayout()
        self.datosEmpresa3.setSpacing(60)
        self.datosEmpresa3.setObjectName(u"datosEmpresa3")
        self.datosEmpresa3.setContentsMargins(20, 0, 20, -1)
        self.datosEmpresa_departamento = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_departamento.setObjectName(u"datosEmpresa_departamento")
        self.datosEmpresa_departamento.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa3.addWidget(self.datosEmpresa_departamento)

        self.datosEmpresa_municipio = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_municipio.setObjectName(u"datosEmpresa_municipio")
        self.datosEmpresa_municipio.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa3.addWidget(self.datosEmpresa_municipio)


        self.verticalLayout_6.addLayout(self.datosEmpresa3)

        self.layout_label_4 = QHBoxLayout()
        self.layout_label_4.setSpacing(60)
        self.layout_label_4.setObjectName(u"layout_label_4")
        self.layout_label_4.setContentsMargins(20, -1, 20, -1)
        self.labelEmpresa_tercero = QLabel(self.scrollAreaContents)
        self.labelEmpresa_tercero.setObjectName(u"labelEmpresa_tercero")
        self.labelEmpresa_tercero.setFont(font1)
        self.labelEmpresa_tercero.setStyleSheet(u"")
        self.labelEmpresa_tercero.setAlignment(Qt.AlignCenter)

        self.layout_label_4.addWidget(self.labelEmpresa_tercero)

        self.labelEmpresa_sucursal = QLabel(self.scrollAreaContents)
        self.labelEmpresa_sucursal.setObjectName(u"labelEmpresa_sucursal")
        self.labelEmpresa_sucursal.setMaximumSize(QSize(98, 16777215))
        self.labelEmpresa_sucursal.setFont(font1)
        self.labelEmpresa_sucursal.setStyleSheet(u"")
        self.labelEmpresa_sucursal.setAlignment(Qt.AlignCenter)

        self.layout_label_4.addWidget(self.labelEmpresa_sucursal)

        self.labelEmpresa_lista_precios = QLabel(self.scrollAreaContents)
        self.labelEmpresa_lista_precios.setObjectName(u"labelEmpresa_lista_precios")
        self.labelEmpresa_lista_precios.setFont(font1)
        self.labelEmpresa_lista_precios.setStyleSheet(u"")
        self.labelEmpresa_lista_precios.setAlignment(Qt.AlignCenter)

        self.layout_label_4.addWidget(self.labelEmpresa_lista_precios)

        self.labelEmpresa_escaner = QLabel(self.scrollAreaContents)
        self.labelEmpresa_escaner.setObjectName(u"labelEmpresa_escaner")
        self.labelEmpresa_escaner.setFont(font1)
        self.labelEmpresa_escaner.setStyleSheet(u"")
        self.labelEmpresa_escaner.setAlignment(Qt.AlignCenter)

        self.layout_label_4.addWidget(self.labelEmpresa_escaner)

        self.labelEmpresa_licencia = QLabel(self.scrollAreaContents)
        self.labelEmpresa_licencia.setObjectName(u"labelEmpresa_licencia")
        self.labelEmpresa_licencia.setFont(font1)
        self.labelEmpresa_licencia.setStyleSheet(u"")
        self.labelEmpresa_licencia.setAlignment(Qt.AlignCenter)

        self.layout_label_4.addWidget(self.labelEmpresa_licencia)


        self.verticalLayout_6.addLayout(self.layout_label_4)

        self.datosEmpresa4 = QHBoxLayout()
        self.datosEmpresa4.setSpacing(60)
        self.datosEmpresa4.setObjectName(u"datosEmpresa4")
        self.datosEmpresa4.setContentsMargins(20, 0, 20, -1)
        self.datosEmpresa_tercero = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_tercero.setObjectName(u"datosEmpresa_tercero")
        self.datosEmpresa_tercero.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8px ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa4.addWidget(self.datosEmpresa_tercero)

        self.datosEmpresa_sucursal = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_sucursal.setObjectName(u"datosEmpresa_sucursal")
        self.datosEmpresa_sucursal.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8px ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa4.addWidget(self.datosEmpresa_sucursal)

        self.datosEmpresa_lista_precios = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_lista_precios.setObjectName(u"datosEmpresa_lista_precios")
        self.datosEmpresa_lista_precios.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa4.addWidget(self.datosEmpresa_lista_precios)

        self.datosEmpresa_tipo_escaner = QComboBox(self.scrollAreaContents)
        self.datosEmpresa_tipo_escaner.setObjectName(u"datosEmpresa_tipo_escaner")
        self.datosEmpresa_tipo_escaner.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.datosEmpresa4.addWidget(self.datosEmpresa_tipo_escaner)

        self.datosEmpresa_licencia = QLineEdit(self.scrollAreaContents)
        self.datosEmpresa_licencia.setObjectName(u"datosEmpresa_licencia")
        self.datosEmpresa_licencia.setMaximumSize(QSize(80, 16777215))
        self.datosEmpresa_licencia.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.datosEmpresa4.addWidget(self.datosEmpresa_licencia)


        self.verticalLayout_6.addLayout(self.datosEmpresa4)

        self.Datos_de_la_empresa_2 = QLabel(self.scrollAreaContents)
        self.Datos_de_la_empresa_2.setObjectName(u"Datos_de_la_empresa_2")
        self.Datos_de_la_empresa_2.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"")
        self.Datos_de_la_empresa_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Datos_de_la_empresa_2)

        self.configuraciones_basculas_2 = QTabWidget(self.scrollAreaContents)
        self.configuraciones_basculas_2.setObjectName(u"configuraciones_basculas_2")
        self.configuraciones_basculas_2.setMaximumSize(QSize(16777215, 815))
        self.configuraciones_basculas_2.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 4px solid #343b48;\n"
"	background-color: #343b48;\n"
"	border-radius:8px\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 10px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #343b48;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    min-width: 8px;\n"
"    padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background:  #1b1e23;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border-color: #568af2;\n"
"    border-bottom-color: #568af2; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"	background: #1b1e23;\n"
"	border-bottom-color: #8a95aa;\n"
"    margin-top: 2px; /* make no"
                        "n-selected tabs look smaller */\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 10, 821, 51))
        self.layout_configuracion_pos_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_configuracion_pos_2.setObjectName(u"layout_configuracion_pos_2")
        self.layout_configuracion_pos_2.setContentsMargins(0, 0, 0, 0)
        self.config_label_pos_2 = QLabel(self.verticalLayoutWidget_2)
        self.config_label_pos_2.setObjectName(u"config_label_pos_2")
        self.config_label_pos_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.layout_configuracion_pos_2.addWidget(self.config_label_pos_2)

        self.config_linea_pos_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.config_linea_pos_2.setObjectName(u"config_linea_pos_2")
        self.config_linea_pos_2.setMaximumSize(QSize(154, 16777215))
        self.config_linea_pos_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_pos_2.addWidget(self.config_linea_pos_2)

        self.configuraciones_basculas_2.addTab(self.tab, "")
        self.Basculas = QWidget()
        self.Basculas.setObjectName(u"Basculas")
        self.Basculas.setStyleSheet(u"background-color:transparent;\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.Basculas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.configuraciones_basculas = QTabWidget(self.Basculas)
        self.configuraciones_basculas.setObjectName(u"configuraciones_basculas")
        self.configuraciones_basculas.setMinimumSize(QSize(0, 56))
        self.configuraciones_basculas.setMaximumSize(QSize(16777215, 400))
        self.configuraciones_basculas.setStyleSheet(u"")
        self.bascula_Dibal_2 = QWidget()
        self.bascula_Dibal_2.setObjectName(u"bascula_Dibal_2")
        self.horizontalLayoutWidget_16 = QWidget(self.bascula_Dibal_2)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(0, 30, 631, 34))
        self.layout_configuracion_dibal_5 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.layout_configuracion_dibal_5.setObjectName(u"layout_configuracion_dibal_5")
        self.layout_configuracion_dibal_5.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_dibal_3 = QLineEdit(self.horizontalLayoutWidget_16)
        self.configuracion_linea_dibal_3.setObjectName(u"configuracion_linea_dibal_3")
        self.configuracion_linea_dibal_3.setMaximumSize(QSize(500, 16777215))
        self.configuracion_linea_dibal_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_dibal_5.addWidget(self.configuracion_linea_dibal_3)

        self.configuracion_secciones_2 = QComboBox(self.horizontalLayoutWidget_16)
        self.configuracion_secciones_2.setObjectName(u"configuracion_secciones_2")
        self.configuracion_secciones_2.setMaximumSize(QSize(16777212, 16777215))
        self.configuracion_secciones_2.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.layout_configuracion_dibal_5.addWidget(self.configuracion_secciones_2)

        self.config_label_dibal_4 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_4.setObjectName(u"config_label_dibal_4")
        self.config_label_dibal_4.setGeometry(QRect(0, 10, 121, 16))
        self.config_label_dibal_5 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_5.setObjectName(u"config_label_dibal_5")
        self.config_label_dibal_5.setGeometry(QRect(460, 10, 71, 16))
        self.horizontalLayoutWidget_17 = QWidget(self.bascula_Dibal_2)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(0, 80, 631, 34))
        self.layout_configuracion_dibal_6 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.layout_configuracion_dibal_6.setObjectName(u"layout_configuracion_dibal_6")
        self.layout_configuracion_dibal_6.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_dibal_4 = QLineEdit(self.horizontalLayoutWidget_17)
        self.configuracion_linea_dibal_4.setObjectName(u"configuracion_linea_dibal_4")
        self.configuracion_linea_dibal_4.setMaximumSize(QSize(500, 16777215))
        self.configuracion_linea_dibal_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_dibal_6.addWidget(self.configuracion_linea_dibal_4)

        self.boton_configuracion_dibal_2 = QPushButton(self.horizontalLayoutWidget_17)
        self.boton_configuracion_dibal_2.setObjectName(u"boton_configuracion_dibal_2")
        self.boton_configuracion_dibal_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_dibal_6.addWidget(self.boton_configuracion_dibal_2)

        self.config_label_dibal_6 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_6.setObjectName(u"config_label_dibal_6")
        self.config_label_dibal_6.setGeometry(QRect(0, 60, 251, 16))
        self.configuraciones_basculas.addTab(self.bascula_Dibal_2, "")
        self.bascula_epelsa_2 = QWidget()
        self.bascula_epelsa_2.setObjectName(u"bascula_epelsa_2")
        self.horizontalLayoutWidget_18 = QWidget(self.bascula_epelsa_2)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(0, 30, 631, 31))
        self.layout_configuracion_epelsa_3 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.layout_configuracion_epelsa_3.setSpacing(0)
        self.layout_configuracion_epelsa_3.setObjectName(u"layout_configuracion_epelsa_3")
        self.layout_configuracion_epelsa_3.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_epelsa_3 = QLineEdit(self.horizontalLayoutWidget_18)
        self.configuracion_linea_epelsa_3.setObjectName(u"configuracion_linea_epelsa_3")
        self.configuracion_linea_epelsa_3.setMinimumSize(QSize(80, 0))
        self.configuracion_linea_epelsa_3.setMaximumSize(QSize(649, 16777215))
        self.configuracion_linea_epelsa_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_epelsa_3.addWidget(self.configuracion_linea_epelsa_3)

        self.config_label_epelsa_3 = QLabel(self.bascula_epelsa_2)
        self.config_label_epelsa_3.setObjectName(u"config_label_epelsa_3")
        self.config_label_epelsa_3.setGeometry(QRect(0, 10, 161, 16))
        self.horizontalLayoutWidget_19 = QWidget(self.bascula_epelsa_2)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(0, 80, 631, 31))
        self.layout_configuracion_dibal_7 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.layout_configuracion_dibal_7.setObjectName(u"layout_configuracion_dibal_7")
        self.layout_configuracion_dibal_7.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_epelsa_4 = QLineEdit(self.horizontalLayoutWidget_19)
        self.configuracion_linea_epelsa_4.setObjectName(u"configuracion_linea_epelsa_4")
        self.configuracion_linea_epelsa_4.setMaximumSize(QSize(500, 16777215))
        self.configuracion_linea_epelsa_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_dibal_7.addWidget(self.configuracion_linea_epelsa_4)

        self.boton_configuracion_epelsa_2 = QPushButton(self.horizontalLayoutWidget_19)
        self.boton_configuracion_epelsa_2.setObjectName(u"boton_configuracion_epelsa_2")
        self.boton_configuracion_epelsa_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_dibal_7.addWidget(self.boton_configuracion_epelsa_2)

        self.config_label_epelsa_4 = QLabel(self.bascula_epelsa_2)
        self.config_label_epelsa_4.setObjectName(u"config_label_epelsa_4")
        self.config_label_epelsa_4.setGeometry(QRect(0, 60, 201, 16))
        self.configuraciones_basculas.addTab(self.bascula_epelsa_2, "")
        self.bascula_ishida_2 = QWidget()
        self.bascula_ishida_2.setObjectName(u"bascula_ishida_2")
        self.config_label_ishida_3 = QLabel(self.bascula_ishida_2)
        self.config_label_ishida_3.setObjectName(u"config_label_ishida_3")
        self.config_label_ishida_3.setGeometry(QRect(0, 10, 161, 16))
        self.horizontalLayoutWidget_20 = QWidget(self.bascula_ishida_2)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(0, 30, 631, 31))
        self.layout_configuracion_epelsa_4 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.layout_configuracion_epelsa_4.setObjectName(u"layout_configuracion_epelsa_4")
        self.layout_configuracion_epelsa_4.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_ishida_3 = QLineEdit(self.horizontalLayoutWidget_20)
        self.configuracion_linea_ishida_3.setObjectName(u"configuracion_linea_ishida_3")
        self.configuracion_linea_ishida_3.setMaximumSize(QSize(630, 16777215))
        self.configuracion_linea_ishida_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_epelsa_4.addWidget(self.configuracion_linea_ishida_3)

        self.horizontalLayoutWidget_21 = QWidget(self.bascula_ishida_2)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(0, 80, 631, 31))
        self.layout_configuracion_dibal_8 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.layout_configuracion_dibal_8.setObjectName(u"layout_configuracion_dibal_8")
        self.layout_configuracion_dibal_8.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_ishida_4 = QLineEdit(self.horizontalLayoutWidget_21)
        self.configuracion_linea_ishida_4.setObjectName(u"configuracion_linea_ishida_4")
        self.configuracion_linea_ishida_4.setMaximumSize(QSize(500, 16777215))
        self.configuracion_linea_ishida_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_dibal_8.addWidget(self.configuracion_linea_ishida_4)

        self.boton_configuracion_ishida_2 = QPushButton(self.horizontalLayoutWidget_21)
        self.boton_configuracion_ishida_2.setObjectName(u"boton_configuracion_ishida_2")
        self.boton_configuracion_ishida_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_dibal_8.addWidget(self.boton_configuracion_ishida_2)

        self.config_label_ishida_4 = QLabel(self.bascula_ishida_2)
        self.config_label_ishida_4.setObjectName(u"config_label_ishida_4")
        self.config_label_ishida_4.setGeometry(QRect(0, 60, 291, 16))
        self.configuraciones_basculas.addTab(self.bascula_ishida_2, "")
        self.bascula_marques_2 = QWidget()
        self.bascula_marques_2.setObjectName(u"bascula_marques_2")
        self.horizontalLayoutWidget_22 = QWidget(self.bascula_marques_2)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(0, 30, 631, 31))
        self.layout_configuracion_marques_3 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.layout_configuracion_marques_3.setObjectName(u"layout_configuracion_marques_3")
        self.layout_configuracion_marques_3.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_marques_2 = QLineEdit(self.horizontalLayoutWidget_22)
        self.configuracion_linea_marques_2.setObjectName(u"configuracion_linea_marques_2")
        self.configuracion_linea_marques_2.setMaximumSize(QSize(637, 16777215))
        self.configuracion_linea_marques_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_marques_3.addWidget(self.configuracion_linea_marques_2)

        self.config_label_marques_2 = QLabel(self.bascula_marques_2)
        self.config_label_marques_2.setObjectName(u"config_label_marques_2")
        self.config_label_marques_2.setGeometry(QRect(0, 10, 241, 16))
        self.horizontalLayoutWidget_23 = QWidget(self.bascula_marques_2)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(30, 70, 601, 41))
        self.layout_configuracion_marques_4 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.layout_configuracion_marques_4.setObjectName(u"layout_configuracion_marques_4")
        self.layout_configuracion_marques_4.setContentsMargins(0, 0, 0, 0)
        self.boton_configuracion_marques_4 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_4.setObjectName(u"boton_configuracion_marques_4")
        self.boton_configuracion_marques_4.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_4)

        self.boton_configuracion_marques_5 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_5.setObjectName(u"boton_configuracion_marques_5")
        self.boton_configuracion_marques_5.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_5)

        self.boton_configuracion_marques_6 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_6.setObjectName(u"boton_configuracion_marques_6")
        self.boton_configuracion_marques_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_6)

        self.configuraciones_basculas.addTab(self.bascula_marques_2, "")

        self.verticalLayout_10.addWidget(self.configuraciones_basculas)

        self.configuraciones_basculas_2.addTab(self.Basculas, "")
        self.facturacion_electronica = QWidget()
        self.facturacion_electronica.setObjectName(u"facturacion_electronica")
        self.configuracion_label_factura_token = QLabel(self.facturacion_electronica)
        self.configuracion_label_factura_token.setObjectName(u"configuracion_label_factura_token")
        self.configuracion_label_factura_token.setGeometry(QRect(0, 0, 161, 16))
        self.horizontalLayoutWidget_13 = QWidget(self.facturacion_electronica)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 20, 831, 31))
        self.layout_configuracion_factura = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.layout_configuracion_factura.setObjectName(u"layout_configuracion_factura")
        self.layout_configuracion_factura.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_factura_token = QLineEdit(self.horizontalLayoutWidget_13)
        self.configuracion_linea_factura_token.setObjectName(u"configuracion_linea_factura_token")
        self.configuracion_linea_factura_token.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_factura.addWidget(self.configuracion_linea_factura_token)

        self.configuracion_linea_factura_Dian = QLineEdit(self.horizontalLayoutWidget_13)
        self.configuracion_linea_factura_Dian.setObjectName(u"configuracion_linea_factura_Dian")
        self.configuracion_linea_factura_Dian.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_factura.addWidget(self.configuracion_linea_factura_Dian)

        self.configuracion_label_factura_token_2 = QLabel(self.facturacion_electronica)
        self.configuracion_label_factura_token_2.setObjectName(u"configuracion_label_factura_token_2")
        self.configuracion_label_factura_token_2.setGeometry(QRect(420, 0, 161, 16))
        self.horizontalLayoutWidget_14 = QWidget(self.facturacion_electronica)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(0, 70, 831, 31))
        self.layout_configuracion_factura_2 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.layout_configuracion_factura_2.setObjectName(u"layout_configuracion_factura_2")
        self.layout_configuracion_factura_2.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_factura_impuesto_bolsa = QComboBox(self.horizontalLayoutWidget_14)
        self.configuracion_linea_factura_impuesto_bolsa.setObjectName(u"configuracion_linea_factura_impuesto_bolsa")
        self.configuracion_linea_factura_impuesto_bolsa.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.layout_configuracion_factura_2.addWidget(self.configuracion_linea_factura_impuesto_bolsa)

        self.configuracion_linea_factura_Impuesto_excluido = QComboBox(self.horizontalLayoutWidget_14)
        self.configuracion_linea_factura_Impuesto_excluido.setObjectName(u"configuracion_linea_factura_Impuesto_excluido")
        self.configuracion_linea_factura_Impuesto_excluido.setStyleSheet(u"border: none;\n"
"color:#8a95aa ;\n"
"border-radius:8 ;	\n"
"background-color: #1b1e23;")

        self.layout_configuracion_factura_2.addWidget(self.configuracion_linea_factura_Impuesto_excluido)

        self.configuracion_linea_factura_email = QLineEdit(self.horizontalLayoutWidget_14)
        self.configuracion_linea_factura_email.setObjectName(u"configuracion_linea_factura_email")
        self.configuracion_linea_factura_email.setMaximumSize(QSize(411, 16777215))
        self.configuracion_linea_factura_email.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1e23;\n"
"	border-radius: 8px;\n"
"	border: 2px solid transparent;\n"
"	padding-left: 10px;\n"
"    padding-right: 10px;\n"
"	selection-color: #f5f6f9;\n"
"	selection-background-color: #568af2;\n"
"    color: #8a95aa;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #568af2;\n"
"    background-color: #21252d;\n"
"}")

        self.layout_configuracion_factura_2.addWidget(self.configuracion_linea_factura_email)

        self.configuracion_label_factura_token_3 = QLabel(self.facturacion_electronica)
        self.configuracion_label_factura_token_3.setObjectName(u"configuracion_label_factura_token_3")
        self.configuracion_label_factura_token_3.setGeometry(QRect(0, 50, 161, 16))
        self.configuracion_label_factura_token_5 = QLabel(self.facturacion_electronica)
        self.configuracion_label_factura_token_5.setObjectName(u"configuracion_label_factura_token_5")
        self.configuracion_label_factura_token_5.setGeometry(QRect(210, 50, 161, 16))
        self.configuracion_label_factura_token_4 = QLabel(self.facturacion_electronica)
        self.configuracion_label_factura_token_4.setObjectName(u"configuracion_label_factura_token_4")
        self.configuracion_label_factura_token_4.setGeometry(QRect(420, 50, 161, 16))
        self.configuraciones_basculas_2.addTab(self.facturacion_electronica, "")

        self.verticalLayout_6.addWidget(self.configuraciones_basculas_2)

        self.layout_configuracion_factura_3 = QHBoxLayout()
        self.layout_configuracion_factura_3.setObjectName(u"layout_configuracion_factura_3")
        self.layout_configuracion_factura_3.setContentsMargins(20, -1, 20, -1)
        self.configuracion_boton_factura_eliminar = QPushButton(self.scrollAreaContents)
        self.configuracion_boton_factura_eliminar.setObjectName(u"configuracion_boton_factura_eliminar")
        self.configuracion_boton_factura_eliminar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_eliminar)

        self.configuracion_boton_factura_limpiar = QPushButton(self.scrollAreaContents)
        self.configuracion_boton_factura_limpiar.setObjectName(u"configuracion_boton_factura_limpiar")
        self.configuracion_boton_factura_limpiar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_limpiar)

        self.configuracion_boton_factura_guardar = QPushButton(self.scrollAreaContents)
        self.configuracion_boton_factura_guardar.setObjectName(u"configuracion_boton_factura_guardar")
        self.configuracion_boton_factura_guardar.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    padding-left: 10px;\n"
"    padding-right: 5px;\n"
"    color: #8a95aa;\n"
"	border-radius: 8;	\n"
"	background-color: #1b1e23;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #21252d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: #272c36;\n"
"}")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_guardar)


        self.verticalLayout_6.addLayout(self.layout_configuracion_factura_3)

        self.scrollArea.setWidget(self.scrollAreaContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_4 = QVBoxLayout(self.page_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.scrollArea_2 = QScrollArea(self.page_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 50, 160, 80))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(310, 200, 160, 80))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 150, 75, 24))
        self.comboBox = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 90, 69, 22))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_6)
        self.scrollArea_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.verticalLayout_7.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)
        self.configuraciones_basculas_2.setCurrentIndex(1)
        self.configuraciones_basculas.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.Titulo_Datos_empresa.setText(QCoreApplication.translate("MainPages", u"Datos de la empresa", None))
        self.Datos_de_la_empresa.setText(QCoreApplication.translate("MainPages", u"Datos de la Empresa", None))
        self.labelEmpresa_nombre.setText(QCoreApplication.translate("MainPages", u"Nombre", None))
        self.labelEmpresa_razon_social.setText(QCoreApplication.translate("MainPages", u"Razon Social", None))
        self.labelEmpresa_direccion.setText(QCoreApplication.translate("MainPages", u"Direccion", None))
        self.labelEmpresa_telefono.setText(QCoreApplication.translate("MainPages", u"Telefono", None))
        self.labelEmpresa_tipo_regimen.setText(QCoreApplication.translate("MainPages", u"Tipo Regimen", None))
        self.labelEmpresa_nit.setText(QCoreApplication.translate("MainPages", u"NIT", None))
        self.labelEmpresa_departamento.setText(QCoreApplication.translate("MainPages", u"Departamento", None))
        self.labelEmpresa_municipio.setText(QCoreApplication.translate("MainPages", u"Municipio", None))
        self.labelEmpresa_tercero.setText(QCoreApplication.translate("MainPages", u"Tercero POS", None))
        self.labelEmpresa_sucursal.setText(QCoreApplication.translate("MainPages", u"Sucursal", None))
        self.labelEmpresa_lista_precios.setText(QCoreApplication.translate("MainPages", u"Lista de precios", None))
        self.labelEmpresa_escaner.setText(QCoreApplication.translate("MainPages", u"Tipo Escaner", None))
        self.labelEmpresa_licencia.setText(QCoreApplication.translate("MainPages", u"Licencia", None))
        self.Datos_de_la_empresa_2.setText(QCoreApplication.translate("MainPages", u"Configuracion de Impresoras y Basculas", None))
        self.config_label_pos_2.setText(QCoreApplication.translate("MainPages", u"Cantidad de caracteres", None))
        self.configuraciones_basculas_2.setTabText(self.configuraciones_basculas_2.indexOf(self.tab), QCoreApplication.translate("MainPages", u"Impresora POS", None))
        self.config_label_dibal_4.setText(QCoreApplication.translate("MainPages", u"Ruta Archivo Bascula", None))
        self.config_label_dibal_5.setText(QCoreApplication.translate("MainPages", u"Secciones", None))
        self.boton_configuracion_dibal_2.setText(QCoreApplication.translate("MainPages", u"Generar Archivo TXT", None))
        self.config_label_dibal_6.setText(QCoreApplication.translate("MainPages", u"Ruta de archivo TX subir datos a bascula Dibal", None))
        self.configuraciones_basculas.setTabText(self.configuraciones_basculas.indexOf(self.bascula_Dibal_2), QCoreApplication.translate("MainPages", u"Bascula Dibal", None))
        self.config_label_epelsa_3.setText(QCoreApplication.translate("MainPages", u"Ruta Archivo tiquetes Epelsa", None))
        self.boton_configuracion_epelsa_2.setText(QCoreApplication.translate("MainPages", u"Generar Archivo Precios", None))
        self.config_label_epelsa_4.setText(QCoreApplication.translate("MainPages", u"Ruta Archivo precios bascula Epelsa", None))
        self.configuraciones_basculas.setTabText(self.configuraciones_basculas.indexOf(self.bascula_epelsa_2), QCoreApplication.translate("MainPages", u"Bascula Epelsa", None))
        self.config_label_ishida_3.setText(QCoreApplication.translate("MainPages", u"Ruta Archivo Bascula", None))
        self.boton_configuracion_ishida_2.setText(QCoreApplication.translate("MainPages", u"Generar Archivo Productos", None))
        self.config_label_ishida_4.setText(QCoreApplication.translate("MainPages", u"Ruta archivo PRODUCTOS subir datos a bascula ishida", None))
        self.configuraciones_basculas.setTabText(self.configuraciones_basculas.indexOf(self.bascula_ishida_2), QCoreApplication.translate("MainPages", u"Bascula Ishida", None))
        self.config_label_marques_2.setText(QCoreApplication.translate("MainPages", u"Direccion IP de la bascula Marques maestra", None))
        self.boton_configuracion_marques_4.setText(QCoreApplication.translate("MainPages", u"ELIMINAR FAMILIAS", None))
        self.boton_configuracion_marques_5.setText(QCoreApplication.translate("MainPages", u"ELIMINAR PRODUCTOS", None))
        self.boton_configuracion_marques_6.setText(QCoreApplication.translate("MainPages", u"ELIMINAR DATOS A BASCULA", None))
        self.configuraciones_basculas.setTabText(self.configuraciones_basculas.indexOf(self.bascula_marques_2), QCoreApplication.translate("MainPages", u"Bascula Marques", None))
        self.configuraciones_basculas_2.setTabText(self.configuraciones_basculas_2.indexOf(self.Basculas), QCoreApplication.translate("MainPages", u"Basculas", None))
        self.configuracion_label_factura_token.setText(QCoreApplication.translate("MainPages", u"Token Facturacion Electronica", None))
        self.configuracion_label_factura_token_2.setText(QCoreApplication.translate("MainPages", u"id Test Dian FE", None))
        self.configuracion_label_factura_token_3.setText(QCoreApplication.translate("MainPages", u"Producto impuesto Bolsa", None))
        self.configuracion_label_factura_token_5.setText(QCoreApplication.translate("MainPages", u"Seleccione impuesto Excluido", None))
        self.configuracion_label_factura_token_4.setText(QCoreApplication.translate("MainPages", u"Email Backup FE", None))
        self.configuraciones_basculas_2.setTabText(self.configuraciones_basculas_2.indexOf(self.facturacion_electronica), QCoreApplication.translate("MainPages", u"Facturacion Electronica", None))
        self.configuracion_boton_factura_eliminar.setText(QCoreApplication.translate("MainPages", u"ELIMINAR DATOS HABIL FE", None))
        self.configuracion_boton_factura_limpiar.setText(QCoreApplication.translate("MainPages", u"LIMPIAR TIQUETES", None))
        self.configuracion_boton_factura_guardar.setText(QCoreApplication.translate("MainPages", u"GUARDAR EDICION", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Aqui no hay nada", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Por aca tampoco", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
    # retranslateUi

