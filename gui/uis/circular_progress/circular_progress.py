# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys
from turtle import width

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # propiedades de la clase
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_color = 0x498BD1
        self.progress_rounded_caps = True
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True
        
        # set tamaño sin layout
        self.resize(self.width, self.height)
    # drop sombra
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 150))
            self.setGraphicsEffect(self.shadow)
        
    #set valores
    def set_value(self, value):
        self.value = value
        self.repaint() # repintar cuando cambie el valor
        
    # paintEvent (diseño del circulo)   
    def paintEvent(self, e):
        # parametros de pintado
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value
        
        #   pintado
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remueve el los bordes pixelados
        paint.setFont(QFont(self.font_family, self.font_size))
        #crear rectangulo
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)
        
        # linea de progreso
        pen=QPen()
        pen.setColor(QColor(self.progress_color))# toma del color de la propiedades de arriba
        pen.setWidth(self.progress_width)
        
        # si es redondeado
        if self.progress_rounded_caps:
            pen.setCapStyle(Qt.RoundCap)
            
            
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)
        #crar texto
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")
        
        #final
        paint.end()
        