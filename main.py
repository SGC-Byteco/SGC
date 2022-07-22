from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
#importar barra circular
from gui.uis.circular_progress.circular_progress import CircularProgress
#impórtar splash screen
from gui.uis.login.ui_splash_screen import Ui_SplashScreen
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
# MAIN WINDOW
from gui.uis.windows.main_window import *
# WIDGETS
from gui.widgets import *
# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'
#contador para la barra circular
contador=0
# Base De Datos
from base_de_datos.db import conexion
from base_de_datos.consulta import *
# MAIN WINDOW
# //////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self) 
        
        # Placeholder de la pagina empresa
        self.ui.load_pages.datosEmpresa_departamento.setPlaceholderText(defecto_departamento)
        self.ui.load_pages.datosEmpresa_departamento.setCurrentIndex(-1)
        self.ui.load_pages.datosEmpresa_municipio.setPlaceholderText(defecto_municipio)
        self.ui.load_pages.datosEmpresa_municipio.setCurrentIndex(-1)
        self.ui.load_pages.datosEmpresa_tercero.setCurrentText(defecto_tercero)
        self.ui.load_pages.datosEmpresa_sucursal.setCurrentText(defecto_sucursal)
        self.ui.load_pages.datosEmpresa_lista_precios.setCurrentText(defecto_lista_de_precios)
        self.ui.load_pages.datosEmpresa_tipo_escaner.setCurrentText(defecto_tipo_de_escaner)
        self.ui.load_pages.configuracion_secciones_2.setCurrentText(defecto_secciones)
        self.ui.load_pages.configuracion_linea_factura_impuesto_bolsa.setCurrentText(defecto_impuesto_bolsa)
        self.ui.load_pages.configuracion_linea_factura_Impuesto_excluido.setCurrentText(defecto_impuesto_excluido)
        
    def change_value(self, value):
        self.progress.set_value(value)
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active         
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(True)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        if btn.objectName() == "btn_widgets":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # LOAD USER PAGE
        if btn.objectName() == "btn_add_user":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
            
        # LOAD PAGE DATOS EMPRESA
        if btn.objectName()== "btn_new_file":
            #Salect Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            
            # Load Page 4
            MainFunctions.set_page(self,self.ui.load_pages.page_5)

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Tab informativo",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")
    
    # ////////////////////////////////// Señales pagina5//////////////////////////
    # def indice_cambiado(self,indice):
    #     print("El indice del departamento es ",indice)
    # def texto_cambiado(self,texto):
    #     print("El texto corresponde a",texto)
    def departamento_municipio(self,indice):
        muni=[]
        index=indice+1
        for i in de_mu:
            if index==i[2]:
                muni.append(i[1])
        self.ui.load_pages.datosEmpresa_municipio.clear()
        self.ui.load_pages.datosEmpresa_municipio.addItems(muni)
        self.ui.load_pages.datosEmpresa_municipio.setPlaceholderText("")
        
    # Boton de guardar edicion
    def boton_guardar_edicion(self):
        print("Validacion de datos")
        self.estado=True
        
        # Datos Nombre
        self.datosEmpresa_nombre= self.ui.load_pages.datosEmpresa_nombre.text()
        self.datosEmpresa_razon_social= self.ui.load_pages.datosEmpresa_razon_social.text()
        self.datosEmpresa_direccion= self.ui.load_pages.datosEmpresa_direccion.text()
        
        # Datos Empresa
        self.datosEmpresa_telefono= self.ui.load_pages.datosEmpresa_telefono.text()
        self.datosEmpresa_tipo_regimen =self.ui.load_pages.datosEmpresa_tipo_regimen.text()
        self.datosEmpresa_nit= self.ui.load_pages.datosEmpresa_nit.text()
        
        # Datos departamentos y municipios
        self.datosEmpresa_departamento= self.ui.load_pages.datosEmpresa_departamento.currentText()
        self.datosEmpresa_municipio= self.ui.load_pages.datosEmpresa_municipio.currentText()
        
        # Datos Terceros, Sucursal, Lista precio, Tipo escaner,licencia
        self.datosEmpresa_tercero=self.ui.load_pages.datosEmpresa_tercero.currentText()
        self.datosEmpresa_sucursal=self.ui.load_pages.datosEmpresa_sucursal.currentText()
        self.datosEmpresa_lista_precios=self.ui.load_pages.datosEmpresa_lista_precios.currentText()
        self.datosEmpresa_escaner=self.ui.load_pages.datosEmpresa_tipo_escaner.currentText()
        self.datosEmpresa_licencia=self.ui.load_pages.datosEmpresa_licencia.text()
        
        # Impresora POS
        self.datosEmpresa_impresora_pos=self.ui.load_pages.config_linea_pos_2.text()
        
        # Basculas
        # Bascula Dibal
        self.datosEmpresa_ruta_dibal=self.ui.load_pages.configuracion_linea_dibal_3.text()
        self.datosEmpresa_secciones_dibal=self.ui.load_pages.configuracion_secciones_2.currentText()
        self.datosEmpresa_archivo_dibal=self.ui.load_pages.configuracion_linea_dibal_4.text()
        
        # Bascula Epelsa
        self.datosEmpresa_ruta_epelsa=self.ui.load_pages.configuracion_linea_epelsa_3.text()
        self.datosEmpresa_ruta_precio_epelsa=self.ui.load_pages.configuracion_linea_epelsa_4.text()
        
        # Bascula Ishida
        self.datosEmpresa_ruta_ishida=self.ui.load_pages.configuracion_linea_ishida_3.text()
        self.datosEmpresa_ruta_productos_ishida=self.ui.load_pages.configuracion_linea_ishida_4.text()
        
        # Bascula Marquez 
        self.datosEmpresa_ip_marques=self.ui.load_pages.configuracion_linea_marques_2.text()
        
        # Facturacion
        self.datosEmpresa_token_factura=self.ui.load_pages.configuracion_linea_factura_token.text()
        self.datosEmpresa_Dian=self.ui.load_pages.configuracion_linea_factura_Dian.text()
        self.datosEmpresa_impuesto_bolsa=self.ui.load_pages.configuracion_linea_factura_impuesto_bolsa.currentText()
        self.datosEmpresa_impuesto_excluido=self.ui.load_pages.configuracion_linea_factura_Impuesto_excluido.currentText()
        self.datosEmpresa_email=self.ui.load_pages.configuracion_linea_factura_email.text()
        
        # Condicion del place holder text
        if (self.ui.load_pages.datosEmpresa_departamento.currentIndex() == -1 or 
        self.ui.load_pages.datosEmpresa_municipio.currentIndex() ==-1):
            self.estado=False
            print("No se pueden actualizar los datos")
            
        boton_guardar(self.estado, self.datosEmpresa_nombre,self.datosEmpresa_razon_social,self.datosEmpresa_direccion,
               self.datosEmpresa_telefono,self.datosEmpresa_tipo_regimen,self.datosEmpresa_nit,
               self.datosEmpresa_departamento, self.datosEmpresa_municipio,self.datosEmpresa_tercero,
               self.datosEmpresa_sucursal,self.datosEmpresa_lista_precios,self.datosEmpresa_escaner,
               self.datosEmpresa_licencia,self.datosEmpresa_impresora_pos,self.datosEmpresa_ruta_dibal,
               self.datosEmpresa_secciones_dibal,self.datosEmpresa_archivo_dibal,self.datosEmpresa_ruta_epelsa,
               self.datosEmpresa_ruta_precio_epelsa,self.datosEmpresa_ruta_ishida,self.datosEmpresa_ruta_productos_ishida,
               self.datosEmpresa_ip_marques,self.datosEmpresa_token_factura,self.datosEmpresa_Dian,self.datosEmpresa_impuesto_bolsa,
               self.datosEmpresa_impuesto_excluido,self.datosEmpresa_email)


       
    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        
###### splash screen #######################################################        
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        #super().__init__()
        # REMOVER BARRA DE TITULO
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #aca va codigo circular
        #importar barra circular
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15,15)
        self.progress.add_shadow(True)
        #cambiar tamaño de la barra de carga circular
        self.progress.progress_width=10
        self.progress.progress_color=QColor(0x8be9fd)
        self.progress.bg_color = QColor(68,71,90,140)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()
        #APLICAR DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)
        
        #TEMPORIZADOR PARA CERRAR LA VENTANA
        self.timer =QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(25)
        
        settings = Settings()
        self.settings = settings.items
        
        self.show()
    # ACTUALIZAR BARRA DE PROGRESO 
    def update(self):
        global contador
        #valores de la barra de progreso
        self.progress.set_value(contador)
        if contador >=100:
            self.timer.stop()
            # apenas llegue a 100 cargar la main
            self.main=MainWindow()
            self.main.show()
            #   CERRAR SPLASH
            self.close()
        #INCREMENTADOR 
        contador +=1
        
        #aca termina codigo circular
        

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())

# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////    