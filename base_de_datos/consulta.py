from base_de_datos.db import conexion
# from db import conexion

try:
    with conexion.cursor() as cursor:
        #Datos de la Empresa
        cursor.execute(
            "SELECT nombre,nit,direccion,telefono,razon_social,tipo_regimen,ruta_archivo_tiquetes_dibal,ruta_archivo_tx_dival,ruta_ip_marques,tipo_escaner,tercero_sucursal_pos_id,prod_lista_precios_id,gen_municipios_id,created_at,updated_at,token_fac_elect,test_id_fe,producto_bolsa_id,gen_iva_excluido_id,licencia,ruta_archivo_tiquetes_epelsa,ruta_archivo_precios_epelsa,fact_grupo,print_logo_pos,email_backup_fact_elect,cantidad_caracteres,bloquear_tercero,precio_bascula_marques,ruta_archivo_txt_ishida,ruta_archivo_tiquetes_ishida,secciones_dibal,secciones_epelsa,secciones_ishida FROM dbo.gen_empresa;"
            )
        datos_empresa= cursor.fetchall()
        for empresa in datos_empresa:
            print("Datos de empresa")
        
        #Datos Empleados
        cursor.execute("SELECT name, email, role FROM dbo.users;")
        datos_usuarios= cursor.fetchall()
        
        cursor.execute("SELECT name FROM dbo.users;")
        datos_usuariosa= cursor.fetchall()
        
        #Datos Departamentos
        cursor.execute("SELECT id,nombre FROM dbo.gen_departamentos;")
        datos_departamento=cursor.fetchall()
        departamentos=[]
        for departamento in datos_departamento:
            departamentos.append(departamento.nombre)    
        #Datos Municipios de acuerdo al departamento
        cursor.execute("SELECT id,nombre,departamento_id FROM dbo.gen_municipios;")
        datos_municipo=cursor.fetchall()
        municipios=[]
        for municipio in datos_municipo:
            municipios.append(municipio.nombre)
            
        #Datos terceros
        cursor.execute("SELECT id,nombre FROM dbo.terceros;")
        datos_terceros=cursor.fetchall()
        terceros=[]
        for tercero in datos_terceros:
            terceros.append(tercero.nombre) 
            
        #Datos Sucursales
        cursor.execute("SELECT direccion, nombre FROM dbo.tercero_sucursales;")
        datos_suscursales_terceros=cursor.fetchall()
        sucursales=[]
        for sucursal in datos_suscursales_terceros:
            sucursales.append(sucursal.nombre)
        
        #Lista de Precios
        cursor.execute("SELECT  nombre FROM dbo.prod_lista_precios;")
        datos_lista_precios=cursor.fetchall()
        lista_precios=[]
        for precios in datos_lista_precios:
            lista_precios.append(precios.nombre)
        
        #Baculas no aparece
        # Secciones Bascula Dibal 
        cursor.execute("SELECT  secciones_dibal FROM dbo.gen_empresa;")
        datos_secciones=cursor.fetchall()
        secciones=[]
        for seccion in datos_secciones:
            secciones.append(seccion.secciones_dibal)
        #Licencia por defecto
        #Cantidad de caracteres por defecto =48
            
            
except Exception as e:
    print("Ocurrio un error al consultar: ",e)
finally:
    conexion.close()