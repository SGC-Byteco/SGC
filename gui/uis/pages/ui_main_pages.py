# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesvzLhgR.ui'
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
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
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
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 561))
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
        self.Titulo_Datos_empresa.setAlignment(Qt.AlignCenter)

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
        self.scrollArea = QScrollArea(self.page_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 841, 681))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 839, 679))
        self.Datos_de_la_empresa = QLabel(self.scrollAreaWidgetContents)
        self.Datos_de_la_empresa.setObjectName(u"Datos_de_la_empresa")
        self.Datos_de_la_empresa.setGeometry(QRect(0, 0, 831, 21))
        self.Datos_de_la_empresa.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.Datos_de_la_empresa.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 60, 841, 31))
        self.datosEmpresa = QHBoxLayout(self.horizontalLayoutWidget)
        self.datosEmpresa.setSpacing(60)
        self.datosEmpresa.setObjectName(u"datosEmpresa")
        self.datosEmpresa.setContentsMargins(20, 0, 20, 0)
        self.datosEmpresa_nombre = QLineEdit(self.horizontalLayoutWidget)
        self.datosEmpresa_nombre.setObjectName(u"datosEmpresa_nombre")

        self.datosEmpresa.addWidget(self.datosEmpresa_nombre)

        self.datosEmpresa_razon_social = QLineEdit(self.horizontalLayoutWidget)
        self.datosEmpresa_razon_social.setObjectName(u"datosEmpresa_razon_social")

        self.datosEmpresa.addWidget(self.datosEmpresa_razon_social)

        self.datosEmpresa_direccion = QLineEdit(self.horizontalLayoutWidget)
        self.datosEmpresa_direccion.setObjectName(u"datosEmpresa_direccion")

        self.datosEmpresa.addWidget(self.datosEmpresa_direccion)

        self.horizontalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 110, 841, 31))
        self.datosEmpresa1 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.datosEmpresa1.setSpacing(60)
        self.datosEmpresa1.setObjectName(u"datosEmpresa1")
        self.datosEmpresa1.setContentsMargins(20, 0, 20, 0)
        self.datosEmpresa_telefono = QLineEdit(self.horizontalLayoutWidget_2)
        self.datosEmpresa_telefono.setObjectName(u"datosEmpresa_telefono")

        self.datosEmpresa1.addWidget(self.datosEmpresa_telefono)

        self.datosEmpresa_tipo_regimen = QLineEdit(self.horizontalLayoutWidget_2)
        self.datosEmpresa_tipo_regimen.setObjectName(u"datosEmpresa_tipo_regimen")

        self.datosEmpresa1.addWidget(self.datosEmpresa_tipo_regimen)

        self.datosEmpresa_nit = QLineEdit(self.horizontalLayoutWidget_2)
        self.datosEmpresa_nit.setObjectName(u"datosEmpresa_nit")

        self.datosEmpresa1.addWidget(self.datosEmpresa_nit)

        self.horizontalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(-10, 160, 841, 31))
        self.datosEmpresa3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.datosEmpresa3.setSpacing(60)
        self.datosEmpresa3.setObjectName(u"datosEmpresa3")
        self.datosEmpresa3.setContentsMargins(20, 0, 20, 0)
        self.datosEmpresa_departamento = QComboBox(self.horizontalLayoutWidget_3)
        self.datosEmpresa_departamento.setObjectName(u"datosEmpresa_departamento")

        self.datosEmpresa3.addWidget(self.datosEmpresa_departamento)

        self.datosEmpresa_municipio = QComboBox(self.horizontalLayoutWidget_3)
        self.datosEmpresa_municipio.setObjectName(u"datosEmpresa_municipio")

        self.datosEmpresa3.addWidget(self.datosEmpresa_municipio)

        self.horizontalLayoutWidget_4 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 220, 841, 31))
        self.datosEmpresa4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.datosEmpresa4.setSpacing(60)
        self.datosEmpresa4.setObjectName(u"datosEmpresa4")
        self.datosEmpresa4.setContentsMargins(20, 0, 20, 0)
        self.datosEmpresa_tercero = QComboBox(self.horizontalLayoutWidget_4)
        self.datosEmpresa_tercero.setObjectName(u"datosEmpresa_tercero")

        self.datosEmpresa4.addWidget(self.datosEmpresa_tercero)

        self.datosEmpresa_sucursal = QComboBox(self.horizontalLayoutWidget_4)
        self.datosEmpresa_sucursal.setObjectName(u"datosEmpresa_sucursal")

        self.datosEmpresa4.addWidget(self.datosEmpresa_sucursal)

        self.datosEmpresa_lista_precios = QComboBox(self.horizontalLayoutWidget_4)
        self.datosEmpresa_lista_precios.setObjectName(u"datosEmpresa_lista_precios")

        self.datosEmpresa4.addWidget(self.datosEmpresa_lista_precios)

        self.datosEmpresa_tipo_escaner = QComboBox(self.horizontalLayoutWidget_4)
        self.datosEmpresa_tipo_escaner.setObjectName(u"datosEmpresa_tipo_escaner")

        self.datosEmpresa4.addWidget(self.datosEmpresa_tipo_escaner)

        self.datosEmpresa_licencia = QLineEdit(self.horizontalLayoutWidget_4)
        self.datosEmpresa_licencia.setObjectName(u"datosEmpresa_licencia")
        self.datosEmpresa_licencia.setMaximumSize(QSize(80, 16777215))

        self.datosEmpresa4.addWidget(self.datosEmpresa_licencia)

        self.labelEmpresa_nombre = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_nombre.setObjectName(u"labelEmpresa_nombre")
        self.labelEmpresa_nombre.setGeometry(QRect(20, 40, 101, 16))
        font1 = QFont()
        font1.setPointSize(9)
        self.labelEmpresa_nombre.setFont(font1)
        self.labelEmpresa_razon_social = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_razon_social.setObjectName(u"labelEmpresa_razon_social")
        self.labelEmpresa_razon_social.setGeometry(QRect(300, 40, 101, 16))
        self.labelEmpresa_razon_social.setFont(font1)
        self.labelEmpresa_direccion = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_direccion.setObjectName(u"labelEmpresa_direccion")
        self.labelEmpresa_direccion.setGeometry(QRect(590, 40, 101, 16))
        self.labelEmpresa_direccion.setFont(font1)
        self.labelEmpresa_telefono = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_telefono.setObjectName(u"labelEmpresa_telefono")
        self.labelEmpresa_telefono.setGeometry(QRect(20, 90, 101, 16))
        self.labelEmpresa_telefono.setFont(font1)
        self.labelEmpresa_tipo_regimen = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_tipo_regimen.setObjectName(u"labelEmpresa_tipo_regimen")
        self.labelEmpresa_tipo_regimen.setGeometry(QRect(310, 90, 101, 16))
        self.labelEmpresa_tipo_regimen.setFont(font1)
        self.labelEmpresa_nit = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_nit.setObjectName(u"labelEmpresa_nit")
        self.labelEmpresa_nit.setGeometry(QRect(590, 90, 101, 16))
        self.labelEmpresa_nit.setFont(font1)
        self.labelEmpresa_departamento = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_departamento.setObjectName(u"labelEmpresa_departamento")
        self.labelEmpresa_departamento.setGeometry(QRect(10, 140, 101, 16))
        self.labelEmpresa_departamento.setFont(font1)
        self.labelEmpresa_municipio = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_municipio.setObjectName(u"labelEmpresa_municipio")
        self.labelEmpresa_municipio.setGeometry(QRect(440, 140, 101, 16))
        self.labelEmpresa_municipio.setFont(font1)
        self.labelEmpresa_tercero = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_tercero.setObjectName(u"labelEmpresa_tercero")
        self.labelEmpresa_tercero.setGeometry(QRect(20, 200, 171, 16))
        self.labelEmpresa_tercero.setFont(font1)
        self.labelEmpresa_sucursal = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_sucursal.setObjectName(u"labelEmpresa_sucursal")
        self.labelEmpresa_sucursal.setGeometry(QRect(200, 200, 101, 16))
        self.labelEmpresa_sucursal.setFont(font1)
        self.labelEmpresa_lista_precios = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_lista_precios.setObjectName(u"labelEmpresa_lista_precios")
        self.labelEmpresa_lista_precios.setGeometry(QRect(380, 200, 131, 16))
        self.labelEmpresa_lista_precios.setFont(font1)
        self.labelEmpresa_escaner = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_escaner.setObjectName(u"labelEmpresa_escaner")
        self.labelEmpresa_escaner.setGeometry(QRect(560, 200, 101, 16))
        self.labelEmpresa_escaner.setFont(font1)
        self.labelEmpresa_licencia = QLabel(self.scrollAreaWidgetContents)
        self.labelEmpresa_licencia.setObjectName(u"labelEmpresa_licencia")
        self.labelEmpresa_licencia.setGeometry(QRect(740, 200, 101, 16))
        self.labelEmpresa_licencia.setFont(font1)
        self.Datos_de_la_empresa_2 = QLabel(self.scrollAreaWidgetContents)
        self.Datos_de_la_empresa_2.setObjectName(u"Datos_de_la_empresa_2")
        self.Datos_de_la_empresa_2.setGeometry(QRect(0, 270, 831, 31))
        self.Datos_de_la_empresa_2.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.Datos_de_la_empresa_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_15 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(0, 530, 831, 31))
        self.layout_configuracion_factura_3 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.layout_configuracion_factura_3.setObjectName(u"layout_configuracion_factura_3")
        self.layout_configuracion_factura_3.setContentsMargins(0, 0, 0, 0)
        self.configuracion_boton_factura_eliminar = QPushButton(self.horizontalLayoutWidget_15)
        self.configuracion_boton_factura_eliminar.setObjectName(u"configuracion_boton_factura_eliminar")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_eliminar)

        self.configuracion_boton_factura_limpiar = QPushButton(self.horizontalLayoutWidget_15)
        self.configuracion_boton_factura_limpiar.setObjectName(u"configuracion_boton_factura_limpiar")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_limpiar)

        self.configuracion_boton_factura_guardar = QPushButton(self.horizontalLayoutWidget_15)
        self.configuracion_boton_factura_guardar.setObjectName(u"configuracion_boton_factura_guardar")

        self.layout_configuracion_factura_3.addWidget(self.configuracion_boton_factura_guardar)

        self.configuraciones_basculas_2 = QTabWidget(self.scrollAreaWidgetContents)
        self.configuraciones_basculas_2.setObjectName(u"configuraciones_basculas_2")
        self.configuraciones_basculas_2.setGeometry(QRect(0, 310, 841, 181))
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

        self.layout_configuracion_pos_2.addWidget(self.config_linea_pos_2)

        self.configuraciones_basculas_2.addTab(self.tab, "")
        self.Basculas = QWidget()
        self.Basculas.setObjectName(u"Basculas")
        self.configuraciones_basculas = QTabWidget(self.Basculas)
        self.configuraciones_basculas.setObjectName(u"configuraciones_basculas")
        self.configuraciones_basculas.setGeometry(QRect(0, 10, 821, 151))
        self.bascula_Dibal_2 = QWidget()
        self.bascula_Dibal_2.setObjectName(u"bascula_Dibal_2")
        self.horizontalLayoutWidget_16 = QWidget(self.bascula_Dibal_2)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(0, 30, 531, 31))
        self.layout_configuracion_dibal_5 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.layout_configuracion_dibal_5.setObjectName(u"layout_configuracion_dibal_5")
        self.layout_configuracion_dibal_5.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_dibal_3 = QLineEdit(self.horizontalLayoutWidget_16)
        self.configuracion_linea_dibal_3.setObjectName(u"configuracion_linea_dibal_3")
        self.configuracion_linea_dibal_3.setMaximumSize(QSize(500, 16777215))

        self.layout_configuracion_dibal_5.addWidget(self.configuracion_linea_dibal_3)

        self.configuracion_secciones_2 = QComboBox(self.horizontalLayoutWidget_16)
        self.configuracion_secciones_2.setObjectName(u"configuracion_secciones_2")

        self.layout_configuracion_dibal_5.addWidget(self.configuracion_secciones_2)

        self.config_label_dibal_4 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_4.setObjectName(u"config_label_dibal_4")
        self.config_label_dibal_4.setGeometry(QRect(0, 10, 121, 16))
        self.config_label_dibal_5 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_5.setObjectName(u"config_label_dibal_5")
        self.config_label_dibal_5.setGeometry(QRect(460, 10, 71, 16))
        self.horizontalLayoutWidget_17 = QWidget(self.bascula_Dibal_2)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(0, 80, 531, 31))
        self.layout_configuracion_dibal_6 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.layout_configuracion_dibal_6.setObjectName(u"layout_configuracion_dibal_6")
        self.layout_configuracion_dibal_6.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_dibal_4 = QLineEdit(self.horizontalLayoutWidget_17)
        self.configuracion_linea_dibal_4.setObjectName(u"configuracion_linea_dibal_4")
        self.configuracion_linea_dibal_4.setMaximumSize(QSize(500, 16777215))

        self.layout_configuracion_dibal_6.addWidget(self.configuracion_linea_dibal_4)

        self.boton_configuracion_dibal_2 = QPushButton(self.horizontalLayoutWidget_17)
        self.boton_configuracion_dibal_2.setObjectName(u"boton_configuracion_dibal_2")

        self.layout_configuracion_dibal_6.addWidget(self.boton_configuracion_dibal_2)

        self.config_label_dibal_6 = QLabel(self.bascula_Dibal_2)
        self.config_label_dibal_6.setObjectName(u"config_label_dibal_6")
        self.config_label_dibal_6.setGeometry(QRect(0, 60, 251, 16))
        self.configuraciones_basculas.addTab(self.bascula_Dibal_2, "")
        self.bascula_epelsa_2 = QWidget()
        self.bascula_epelsa_2.setObjectName(u"bascula_epelsa_2")
        self.horizontalLayoutWidget_18 = QWidget(self.bascula_epelsa_2)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(0, 30, 531, 31))
        self.layout_configuracion_epelsa_3 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.layout_configuracion_epelsa_3.setObjectName(u"layout_configuracion_epelsa_3")
        self.layout_configuracion_epelsa_3.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_epelsa_3 = QLineEdit(self.horizontalLayoutWidget_18)
        self.configuracion_linea_epelsa_3.setObjectName(u"configuracion_linea_epelsa_3")
        self.configuracion_linea_epelsa_3.setMaximumSize(QSize(545, 16777215))

        self.layout_configuracion_epelsa_3.addWidget(self.configuracion_linea_epelsa_3)

        self.config_label_epelsa_3 = QLabel(self.bascula_epelsa_2)
        self.config_label_epelsa_3.setObjectName(u"config_label_epelsa_3")
        self.config_label_epelsa_3.setGeometry(QRect(0, 10, 161, 16))
        self.horizontalLayoutWidget_19 = QWidget(self.bascula_epelsa_2)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(0, 80, 531, 31))
        self.layout_configuracion_dibal_7 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.layout_configuracion_dibal_7.setObjectName(u"layout_configuracion_dibal_7")
        self.layout_configuracion_dibal_7.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_epelsa_4 = QLineEdit(self.horizontalLayoutWidget_19)
        self.configuracion_linea_epelsa_4.setObjectName(u"configuracion_linea_epelsa_4")
        self.configuracion_linea_epelsa_4.setMaximumSize(QSize(500, 16777215))

        self.layout_configuracion_dibal_7.addWidget(self.configuracion_linea_epelsa_4)

        self.boton_configuracion_epelsa_2 = QPushButton(self.horizontalLayoutWidget_19)
        self.boton_configuracion_epelsa_2.setObjectName(u"boton_configuracion_epelsa_2")

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
        self.horizontalLayoutWidget_20.setGeometry(QRect(0, 30, 531, 31))
        self.layout_configuracion_epelsa_4 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.layout_configuracion_epelsa_4.setObjectName(u"layout_configuracion_epelsa_4")
        self.layout_configuracion_epelsa_4.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_ishida_3 = QLineEdit(self.horizontalLayoutWidget_20)
        self.configuracion_linea_ishida_3.setObjectName(u"configuracion_linea_ishida_3")
        self.configuracion_linea_ishida_3.setMaximumSize(QSize(545, 16777215))

        self.layout_configuracion_epelsa_4.addWidget(self.configuracion_linea_ishida_3)

        self.horizontalLayoutWidget_21 = QWidget(self.bascula_ishida_2)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(0, 80, 531, 31))
        self.layout_configuracion_dibal_8 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.layout_configuracion_dibal_8.setObjectName(u"layout_configuracion_dibal_8")
        self.layout_configuracion_dibal_8.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_ishida_4 = QLineEdit(self.horizontalLayoutWidget_21)
        self.configuracion_linea_ishida_4.setObjectName(u"configuracion_linea_ishida_4")
        self.configuracion_linea_ishida_4.setMaximumSize(QSize(500, 16777215))

        self.layout_configuracion_dibal_8.addWidget(self.configuracion_linea_ishida_4)

        self.boton_configuracion_ishida_2 = QPushButton(self.horizontalLayoutWidget_21)
        self.boton_configuracion_ishida_2.setObjectName(u"boton_configuracion_ishida_2")

        self.layout_configuracion_dibal_8.addWidget(self.boton_configuracion_ishida_2)

        self.config_label_ishida_4 = QLabel(self.bascula_ishida_2)
        self.config_label_ishida_4.setObjectName(u"config_label_ishida_4")
        self.config_label_ishida_4.setGeometry(QRect(0, 60, 291, 16))
        self.configuraciones_basculas.addTab(self.bascula_ishida_2, "")
        self.bascula_marques_2 = QWidget()
        self.bascula_marques_2.setObjectName(u"bascula_marques_2")
        self.horizontalLayoutWidget_22 = QWidget(self.bascula_marques_2)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(0, 30, 531, 31))
        self.layout_configuracion_marques_3 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.layout_configuracion_marques_3.setObjectName(u"layout_configuracion_marques_3")
        self.layout_configuracion_marques_3.setContentsMargins(0, 0, 0, 0)
        self.configuracion_linea_marques_2 = QLineEdit(self.horizontalLayoutWidget_22)
        self.configuracion_linea_marques_2.setObjectName(u"configuracion_linea_marques_2")
        self.configuracion_linea_marques_2.setMaximumSize(QSize(545, 16777215))

        self.layout_configuracion_marques_3.addWidget(self.configuracion_linea_marques_2)

        self.config_label_marques_2 = QLabel(self.bascula_marques_2)
        self.config_label_marques_2.setObjectName(u"config_label_marques_2")
        self.config_label_marques_2.setGeometry(QRect(0, 10, 241, 16))
        self.horizontalLayoutWidget_23 = QWidget(self.bascula_marques_2)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(30, 70, 491, 41))
        self.layout_configuracion_marques_4 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.layout_configuracion_marques_4.setObjectName(u"layout_configuracion_marques_4")
        self.layout_configuracion_marques_4.setContentsMargins(0, 0, 0, 0)
        self.boton_configuracion_marques_4 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_4.setObjectName(u"boton_configuracion_marques_4")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_4)

        self.boton_configuracion_marques_5 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_5.setObjectName(u"boton_configuracion_marques_5")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_5)

        self.boton_configuracion_marques_6 = QPushButton(self.horizontalLayoutWidget_23)
        self.boton_configuracion_marques_6.setObjectName(u"boton_configuracion_marques_6")

        self.layout_configuracion_marques_4.addWidget(self.boton_configuracion_marques_6)

        self.configuraciones_basculas.addTab(self.bascula_marques_2, "")
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

        self.layout_configuracion_factura.addWidget(self.configuracion_linea_factura_token)

        self.configuracion_linea_factura_Dian = QLineEdit(self.horizontalLayoutWidget_13)
        self.configuracion_linea_factura_Dian.setObjectName(u"configuracion_linea_factura_Dian")

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

        self.layout_configuracion_factura_2.addWidget(self.configuracion_linea_factura_impuesto_bolsa)

        self.configuracion_linea_factura_Impuesto_excluido = QComboBox(self.horizontalLayoutWidget_14)
        self.configuracion_linea_factura_Impuesto_excluido.setObjectName(u"configuracion_linea_factura_Impuesto_excluido")

        self.layout_configuracion_factura_2.addWidget(self.configuracion_linea_factura_Impuesto_excluido)

        self.configuracion_linea_factura_email = QLineEdit(self.horizontalLayoutWidget_14)
        self.configuracion_linea_factura_email.setObjectName(u"configuracion_linea_factura_email")
        self.configuracion_linea_factura_email.setMaximumSize(QSize(411, 16777215))

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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pages.addWidget(self.page_5)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)
        self.configuraciones_basculas_2.setCurrentIndex(1)
        self.configuraciones_basculas.setCurrentIndex(0)


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
        self.labelEmpresa_departamento.setText(QCoreApplication.translate("MainPages", u"Direccion", None))
        self.labelEmpresa_municipio.setText(QCoreApplication.translate("MainPages", u"Municipio", None))
        self.labelEmpresa_tercero.setText(QCoreApplication.translate("MainPages", u"Tercero POS por defecto", None))
        self.labelEmpresa_sucursal.setText(QCoreApplication.translate("MainPages", u"Sucursal", None))
        self.labelEmpresa_lista_precios.setText(QCoreApplication.translate("MainPages", u"Lista de precios defecto", None))
        self.labelEmpresa_escaner.setText(QCoreApplication.translate("MainPages", u"Tipo Escaner", None))
        self.labelEmpresa_licencia.setText(QCoreApplication.translate("MainPages", u"Licencia", None))
        self.Datos_de_la_empresa_2.setText(QCoreApplication.translate("MainPages", u"Configuracion de Impresoras y Basculas", None))
        self.configuracion_boton_factura_eliminar.setText(QCoreApplication.translate("MainPages", u"ELIMINAR DATOS HABIL FE", None))
        self.configuracion_boton_factura_limpiar.setText(QCoreApplication.translate("MainPages", u"LIMPIAR TIQUETES", None))
        self.configuracion_boton_factura_guardar.setText(QCoreApplication.translate("MainPages", u"GUARDAR EDICION", None))
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
    # retranslateUi

