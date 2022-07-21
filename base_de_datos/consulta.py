from base_de_datos.db import conexion
# from db import conexion

import numpy as np

try:
    with conexion.cursor() as cursor:
        #Datos de la Empresa
        cursor.execute(
            "SELECT nombre,nit,direccion,telefono,razon_social,tipo_regimen,ruta_archivo_tiquetes_dibal,ruta_archivo_tx_dival,ruta_ip_marques,tipo_escaner,tercero_sucursal_pos_id,prod_lista_precios_id,gen_municipios_id,created_at,updated_at,token_fac_elect,test_id_fe,producto_bolsa_id,gen_iva_excluido_id,licencia,ruta_archivo_tiquetes_epelsa,ruta_archivo_precios_epelsa,fact_grupo,print_logo_pos,email_backup_fact_elect,cantidad_caracteres,bloquear_tercero,precio_bascula_marques,ruta_archivo_txt_ishida,ruta_archivo_tiquetes_ishida,secciones_dibal,secciones_epelsa,secciones_ishida FROM dbo.gen_empresa;"
            )
        datos_empresa= cursor.fetchall()
        for empresa in datos_empresa:
            print("Datos de empresa cargados correctamente")
        
        #Datos Empleados
        cursor.execute("SELECT name, email, role FROM dbo.users;")
        datos_usuarios= cursor.fetchall()
        
        cursor.execute("SELECT name FROM dbo.users;")
        datos_usuariosa= cursor.fetchall()
        
        #Datos Departamentos
        cursor.execute("SELECT id,nombre FROM dbo.gen_departamentos;")
        datos_departamento=cursor.fetchall()
        departamentos=[]
        departamentos_id=[]
        for departamento in datos_departamento:
            departamentos.append(departamento.nombre)
            departamentos_id.append(departamento.id)
        # print(departamentos_id)
        
        #Datos Municipios de acuerdo al departamento
        cursor.execute("SELECT id,nombre,departamento_id FROM dbo.gen_municipios;")
        datos_municipo=cursor.fetchall()
        municipios=[]
        for municipio in datos_municipo:
            municipios.append(municipio.nombre)
            # municipios.append(municipio.id)
        # print(municipios)
        
        # Inner JOIN DEPARTAMENTO MUNICIPIO
        cursor.execute("SELECT M.id,M.nombre,departamento_id,D.nombre as depar FROM dbo.gen_municipios M INNER JOIN dbo.gen_departamentos D on M.departamento_id=D.id")
        datos_D_M=cursor.fetchall()
        de_mu=[]
        for d_m in datos_D_M:
            de_mu.append(d_m)
        # print(de_mu)     
        
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
    
        # Ensayo de editar 
        def boton_guardar(estado,nombre,razon_social,direccion,
                   telefono,tipo_regimen,nit,departamento,municipio,
                   tercero,sucursal,lista_precios,tipo_escaner,licencia,
                   impresora_pos,ruta_dibal,secciones,archivo_dibal,ruta_epelsa,
                   ruta_precio_epelsa,ruta_ishida,ruta_productos_ishida,ruta_ip_marques):
            if estado==True:
                # Carga de archivo txt por defecto
                defecto_departamento=np.array(departamento)
                defecto_municipio=np.array(municipio)
                defecto_tercero=np.array(tercero)
                defecto_sucursal=np.array(sucursal)
                defecto_lista_de_precios=np.array(lista_precios)
                defecto_tipo_de_escaner=np.array(tipo_escaner)
                defecto_secciones=np.array(secciones)
                
                archivo=open("base_de_datos/defecto_empresa.txt","w")
                defec_departamento=str(defecto_departamento)
                defec_municipio=str(defecto_municipio)
                defec_tercero=str(defecto_tercero)
                defec_sucursal=str(defecto_sucursal)
                defec_lista_de_precios=str(defecto_lista_de_precios)
                defec_tipo_de_escaner=str(defecto_tipo_de_escaner)
                defec_secciones=str(defecto_secciones)
                
                archivo.write(defec_departamento)
                archivo.write('\n')
                archivo.write(defec_municipio)
                archivo.write('\n')
                archivo.write(defec_tercero)
                archivo.write('\n')
                archivo.write(defec_sucursal)
                archivo.write('\n')
                archivo.write(defec_lista_de_precios)
                archivo.write('\n')
                archivo.write(defec_tipo_de_escaner)
                archivo.write('\n')
                archivo.write(defec_secciones)
                archivo.close()
                
                #Carga de valores de campos de texto en la base da datos 
                try:
                    with conexion.cursor() as cursor:
                        # Datos Principales
                        consulta_empresa_1= "update dbo.gen_empresa set nombre=?,razon_social=?,direccion=?,"
                        consulta_empresa_2="telefono=?,tipo_regimen=?,nit=?,licencia=?,cantidad_caracteres=?,"
                        consulta_empresa_3="ruta_archivo_tiquetes_dibal=?,ruta_archivo_tx_dival=?,ruta_archivo_tiquetes_epelsa=?,"
                        consulta_empresa_4="ruta_archivo_precios_epelsa=?,ruta_archivo_txt_ishida=?,ruta_archivo_tiquetes_ishida=?,ruta_ip_marques WHERE id = ?;"
                        consulta_empresa=consulta_empresa_1+consulta_empresa_2+consulta_empresa_3+consulta_empresa_4
                        id = 1
                        cursor.execute(consulta_empresa,(nombre,razon_social,direccion,telefono,tipo_regimen,nit,licencia, 
                                                         impresora_pos,ruta_dibal,archivo_dibal,ruta_epelsa,ruta_precio_epelsa,
                                                         ruta_ishida,ruta_productos_ishida,ruta_ip_marques,id))                        
                        conexion.commit()
                        print("Datos Cambiados Correctamente")
                except Exception as e:
                    print("Ocurrió un error al editar: ", e)  
            else:
                print("Los datos no fueron actualizados")
            
        with open("base_de_datos/defecto_empresa.txt") as archivo_defecto:
            lineas= archivo_defecto.readlines()
            lineas= list(map(lambda l: l.rstrip('\n'),lineas))
            defecto_departamento=lineas[0]
            defecto_municipio=lineas[1]
            defecto_tercero=lineas[2]
            defecto_sucursal=lineas[3]
            defecto_lista_de_precios=lineas[4]
            defecto_tipo_de_escaner=lineas[5]
            defecto_secciones=lineas[6]

except Exception as e:
    print("Ocurrio un error al consultar: ",e)
# finally:
    # conexion.close()