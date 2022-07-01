from base_de_datos.db import conexion


try:
    with conexion.cursor() as cursor:
        #Datos de la Empresa
        cursor.execute("SELECT nombre, nit, direccion, telefono, razon_social FROM dbo.gen_empresa;")
        datos_empresa= cursor.fetchall()
        for empresa in datos_empresa:
            print("Datos de empresa")
        
        #Datos Empleados
        cursor.execute("SELECT name, email, role FROM dbo.users;")
        datos_usuarios= cursor.fetchall()
        
        cursor.execute("SELECT name FROM dbo.users;")
        datos_usuariosa= cursor.fetchall()
        
            
except Exception as e:
    print("Ocurrio un error al consultar: ",e)
finally:
    conexion.close()