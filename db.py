#CONEXION a Base De Datos

import pyodbc

servidor= "DESKTOP-54UEJ6B"
base_de_datos="sgc"
usuario="sa"
contraseña="123"

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+servidor+
                              ';DATABASE='+base_de_datos+';UID='+usuario+';PWD=' + contraseña)
    # OK! conexión exitosa
    print("Conexion exitosa a la base de datos")
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)