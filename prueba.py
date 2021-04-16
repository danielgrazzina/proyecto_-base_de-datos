import sqlite3

def base_datos(op_BD,tabla,tu_clave=(),seleccion="",op_producto=9,op_cliente=9,op_pedido=9):
    # conexion base de datos
    miconexion=sqlite3.connect("inventario.db")
    micursor=miconexion.cursor()
    
    if op_BD == 0:
        # consultar
        if tabla ==  0:
            # tabla producto

            if op_producto == 0:
                #id_producto
                #try:
                micursor.execute("SELECT * FROM producto WHERE ID_PRODUCTO = ?",[seleccion])
                resultado=micursor.fetchone()
                #except Error:
                    #print(Error)    
            elif op_producto == 1:
                # precio_costo
                micursor.execute("SELECT * FROM producto WHERE PRECIO_COSTO = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_producto == 2:
                # precio_venta
                micursor.execute("SELECT * FROM producto WHERE PRECIO_VENTA = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_producto == 3:
                # cantidad_pro
                micursor.execute("SELECT * FROM producto WHERE CANTIDAD_PRODUCTO = ?",[seleccion])
                resultado=micursor.fetchone()
        elif tabla == 1:
            # tabla cliente
            if op_cliente == 0:
                # Cedula
                micursor.execute("SELECT * FROM cliente WHERE CI_CLIENTE = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_cliente == 1:
                # nombre
                micursor.execute("SELECT * FROM cliente WHERE NOMBRE = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_cliente == 2:
                #apellido
                micursor.execute("SELECT * FROM cliente WHERE APELLIDO = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_cliente == 3:
                #telefono
                micursor.execute("SELECT * FROM cliente WHERE TELEFONO = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_cliente == 4:
                #direccion
                micursor.execute("SELECT * FROM cliente WHERE DIRECCION = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_cliente == 5:
                #deuda
                micursor.execute("SELECT * FROM cliente WHERE DEUDA = ?",[seleccion])
                resultado=micursor.fetchone()
        elif tabla == 3:
            # tabla pedido
            if op_pedido == 0:
                # id_pedido
                micursor.execute("SELECT * FROM pedido WHERE ID_PRODUCTO = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_pedido == 1:
                # ci_cliente
                micursor.execute("SELECT * FROM pedido WHERE CI_CLIENTE = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_pedido == 2:
                # id_pedido
                micursor.execute("SELECT * FROM pedido WHERE ID_PRODUCTO = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_pedido == 3:
                # cantidad_ped
                micursor.execute("SELECT * FROM pedido WHERE CANTIDAD_PEDIDA = ?",[seleccion])
                resultado=micursor.fetchone()
            elif op_pedido == 4:
                # fecha
                micursor.execute("SELECT * FROM pedido WHERE FECHA = ?",[seleccion])
                resultado=micursor.fetchone()
    elif op_BD ==  1:
        #crear nuevo
        if tabla == 0:
            # productos
            micursor.execute("INSERT INTO producto VALUES(?, ?, ?, ?)",tu_clave)
            miconexion.commit()
        elif tabla == 1:
            # cliente
            micursor.execute("INSERT INTO cliente VALUES(?, ?, ?, ?, ?, ?)",tu_clave)
            miconexion.commit()
        elif tabla == 2:
            # pedido 
            micursor.execute("INSERT INTO pedido VALUES(?, ?, ?, ?, ?)",tu_clave)
            miconexion.commit()
    elif op_BD == 2:
        #actualizar
        if tabla == 0:
            # productos
            row0=tu_clave[0]
            row1=tu_clave[1]
            row2=tu_clave[2]
            row3=tu_clave[3]
            
            micursor.execute("UPDATE producto SET PRECIO_COSTO = ? , PRECIO_VENTA = ?, CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?",(row1,row2,row3,row0))
            miconexion.commit()
        elif tabla == 1:
            # cliente
            row0=tu_clave[0]
            row1=tu_clave[1]
            row2=tu_clave[2]
            row3=tu_clave[3]
            row4=tu_clave[4]
            row5=tu_clave[5]
            
            micursor.execute("UPDATE cliente SET NOMBRE = ?, APELLIDO = ?, TELEFONO = ?, DIRECCION = ?, DEUDA = ? WHERE CI_CLIENTE = ?",(row1,row2,row3,row4,row5,row0))
            miconexion.commit()
        elif tabla == 2:
            # pedido
            row0=tu_clave[0]
            row1=tu_clave[1]
            row2=tu_clave[2]
            row3=tu_clave[3]
            row4=tu_clave[4]
            
            micursor.execute("UPDATE producto SET CI_CLIENTE = ? , ID_PRODUCTO = ?, CANTIDAD_PEDIDA = ?, FECHA = ? WHERE ID_PEDIDO = ?",(row1,row2,row3,row4,row0))
            miconexion.commit() 

    elif op_BD == 3:
        #eliminar
        if tabla == 0:
            # productos
            row0=tu_clave[0]
            micursor.execute("DELETE FROM producto WHERE ID_PRODUCTO = ?",(row0,))
            miconexion.commit()
        elif tabla == 1:
            # cliente
            row0=tu_clave[0]
            micursor.execute("DELETE FROM cliente WHERE CI_CLIENTE = ?",(row0,))
            miconexion.commit()
        elif tabla == 2:
            # pedido
            row0=tu_clave[0]
            micursor.execute("DELETE FROM pedido WHERE ID_PEDIDO = ?",(row0,))
            miconexion.commit()
    miconexion.close()

def main ():
    #----------prueba----------------------
    #op_BD,tabla,tu_clave=(),seleccion="",op_producto=9,op_cliente=9,op_pedido=9
    op_BD=0
    tabla=1
    op_producto=7
    op_cliente=0
    op_pedido=7
    seleccion='5'
    tu_clave= ('a2',35,100,20)
    #----------prueba----------------------

    base_datos(op_BD,tabla,tu_clave,seleccion,op_producto,op_cliente,op_pedido)
main()