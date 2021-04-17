from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
from idlelib.tooltip import Hovertip
from datetime import datetime
import time
import sqlite3

tu_clave=[]
seleccion=""
op_producto=9
op_cliente=9
op_pedido=9
clean_total=0
resultado=[]
now = datetime.now()
str_now = now.strftime("%d/%m/%Y")
busqueda=0
op_busqueda=0
lista_pedido={}

def base_datos(op_BD, tabla, tu_clave = [], seleccion="", op_producto=9, op_cliente=9, op_pedido=9, clean_total=0):
    # conexion base de datos
    miconexion=sqlite3.connect("inventario.db")
    micursor=miconexion.cursor()
    
    if op_BD == 0:
        # consultar
        if tabla ==  0:
            # tabla producto
            if op_producto == 0:
                #id_producto
                micursor.execute("SELECT * FROM producto WHERE ID_PRODUCTO = ?",(seleccion, ))
                resultado=micursor.fetchone()
                return resultado   
            elif op_producto == 1:
                # precio_costo
                micursor.execute("SELECT * FROM producto WHERE PRECIO_COSTO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_producto == 2:
                # precio_venta
                micursor.execute("SELECT * FROM producto WHERE PRECIO_VENTA = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_producto == 3:
                # cantidad_pro
                micursor.execute("SELECT * FROM producto WHERE CANTIDAD_PRODUCTO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_producto == 4:
                micursor.execute("SELECT * FROM producto ORDER BY ID_PRODUCTO DESC")
                resultado=micursor.fetchall()
                return resultado
        elif tabla == 1:
            # tabla cliente
            if op_cliente == 0:
                # Cedula
                micursor.execute("SELECT * FROM cliente WHERE CI_CLIENTE = ?",(seleccion,))
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 1:
                # nombre
                micursor.execute("SELECT * FROM cliente WHERE NOMBRE = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 2:
                #apellido
                micursor.execute("SELECT * FROM cliente WHERE APELLIDO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 3:
                #telefono
                micursor.execute("SELECT * FROM cliente WHERE TELEFONO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 4:
                #direccion
                micursor.execute("SELECT * FROM cliente WHERE DIRECCION = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 5:
                #deuda
                micursor.execute("SELECT * FROM cliente WHERE DEUDA = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_cliente == 6:
                micursor.execute("SELECT * FROM cliente ORDER BY NOMBRE DESC")
                resultado=micursor.fetchall()
                return resultado
        elif tabla == 3:
            # tabla pedido
            if op_pedido == 0:
                # id_pedido
                micursor.execute("SELECT * FROM pedido WHERE ID_PEDIDO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_pedido == 1:
                # ci_cliente
                micursor.execute("SELECT * FROM pedido WHERE CI_CLIENTE = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_pedido == 2:
                # id_pedido
                micursor.execute("SELECT * FROM pedido WHERE ID_PRODUCTO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_pedido == 3:
                # cantidad_ped
                micursor.execute("SELECT * FROM pedido WHERE CANTIDAD_PEDIDO = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_pedido == 4:
                # fecha
                micursor.execute("SELECT * FROM pedido WHERE FECHA = ?",seleccion)
                resultado=micursor.fetchone()
                return resultado
            elif op_pedido == 5:
                micursor.execute("SELECT * FROM pedido ORDER BY FECHA DESC")
                resultado=micursor.fetchall()
                return resultado
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
            micursor.execute("INSERT INTO pedido VALUES(NULL, ?, ?, ?, ?)",tu_clave)
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
            
            micursor.execute("UPDATE producto SET CI_CLIENTE = ? , ID_PRODUCTO = ?, CANTIDAD_PEDIDO = ?, FECHA = ? WHERE ID_PEDIDO = ?",(row1,row2,row3,row0))
            miconexion.commit() 

    elif op_BD == 3:
        #eliminar
        if tabla == 0:
            # productos
            if clean_total == 0:
                row0=tu_clave[0]
                micursor.execute("DELETE FROM producto WHERE ID_PRODUCTO = ?",(row0,))
                miconexion.commit()
            else:
                micursor.execute("DELETE FROM producto WHERE ID_PRODUCTO = ID_PRODUCTO")
                miconexion.commit()
        elif tabla == 1:
            # cliente
            if clean_total == 0:
                row0=tu_clave[0]
                micursor.execute("DELETE FROM cliente WHERE CI_CLIENTE = ?",(row0,))
                miconexion.commit()
            else:
                micursor.execute("DELETE FROM cliente WHERE CI_CLIENTE = CI_CLIENTE")
                miconexion.commit()
        elif tabla == 2:
            # pedido
            if clean_total == 0:
                row0=tu_clave[0]
                micursor.execute("DELETE FROM pedido WHERE ID_PEDIDO = ?",(row0,))
                miconexion.commit()
            else:
                micursor.execute("DELETE FROM pedido WHERE ID_PEDIDO = ID_PEDIDO")
                miconexion.commit()
    miconexion.close()

def mostrar_busqueda():
    global lista_pedido
    op_busqueda = lista_pedido.get('busqueda')
    print(lista_pedido.get('busqueda'))
    op_busqueda = 1
    if op_busqueda == 1:
        res = lista_pedido.get(lista_pedido[:][:])
        print(res)
        for row in res:
            tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))
    else:
        obt_productos()
    
def borrarPRODUCTO():
    op_BD = 3
    tabla = 0
    clean_total = 1
    base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente, op_pedido, clean_total)
    clean()
    obt_productos()

def validacion():
    return len(eid.get()) != 0 and len(eprice_c.get()) != 0 and len(eprice_v.get()) != 0 and len(eamount.get()) != 0


def obt_productos():
    view = tree.get_children()
    for elementos in view:
         tree.delete(elementos)
    op_BD=0
    tabla=0
    op_producto=4
    resultado=(base_datos(op_BD,tabla,tu_clave,seleccion,op_producto))
    for row in resultado:
         tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))

def actualizar_tabla():
    view = tree.get_children()
    for elementos in view:
         tree.delete(elementos)
    op_BD=0
    tabla=0
    op_producto=4
    resultado=(base_datos(op_BD,tabla,tu_clave,seleccion,op_producto))
    for row in resultado:
         tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))

    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    bmas["state"] = "disable"
    bmenos["state"] = "disable"
    eid["state"] = "normal"
    clean()

def agregar_producto():
    tu_clave = []
    if validacion():
        if eprice_c.get().isdigit() and eprice_v.get().isdigit() and eamount.get().isdigit():
            tu_clave.append(eid.get())
            tu_clave.append(eprice_c.get())
            tu_clave.append(eprice_v.get())
            tu_clave.append(eamount.get())
            op_BD=1
            tabla=0
            base_datos(op_BD, tabla, tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se guardaron correctamente los campos")
        else:
            messagebox.showerror("ERROR", "PRECIO COSTO, PRECIO VENTA y CANTIDAD deben ser numericos")
    else:
        messagebox.showerror("ERROR", "No pueden haber campos en blanco")
    clean()
    obt_productos()

def editar_producto():
    tu_clave = []
    if validacion():
        if eprice_c.get().isdigit() and eprice_v.get().isdigit() and eamount.get().isdigit():
            tu_clave.append(eid.get())
            tu_clave.append(eprice_c.get())
            tu_clave.append(eprice_v.get())
            tu_clave.append(eamount.get())
            op_BD=2
            tabla=0
            base_datos(op_BD, tabla, tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se actualizaron correctamente los campos")
        else:
            messagebox.showerror("ERROR", "PRECIO COSTO, PRECIO VENTA y CANTIDAD deben ser numericos")
    else:
        messagebox.showerror("ERROR", "No puede haber campos en blanco")
    eid.configure(state = 'normal')
    clean()
    obt_productos()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    bmas["state"] = "disable"
    bmenos["state"] = "disable"

def eliminar_producto():
    tu_clave = []
    if len(eid.get()) != 0:
        tu_clave.append(eid.get())
        op_BD=3
        tabla=0
        base_datos(op_BD, tabla, tu_clave)
        messagebox.showinfo("BASE DE DATOS", "Se eliminaron correctamente los campos")
    else:
        messagebox.showerror("ERROR", "El ID Producto no puede estar vacio")
    eid.configure(state = 'normal')
    clean()
    obt_productos()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    bmas["state"] = "disable"
    bmenos["state"] = "disable"

    "Acabo de agregar la funcion para la operacion de mas"
def suma_inventario():
    if validacion():
        if eprice_c.get().isdigit() and eprice_v.get().isdigit() and eamount.get().isdigit():
            tu_clave = []
            cant_n = int(eamount.get())
            seleccion = eid.get()
            op_BD=0
            tabla=0
            op_producto = 0
            resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto))
            tu_clave = []
            suma = cant_n + int(resultado[3])
            tu_clave.append(eid.get())
            tu_clave.append(eprice_c.get())
            tu_clave.append(eprice_v.get())
            tu_clave.append(suma)
            op_BD = 2
            tabla = 0
            base_datos(op_BD, tabla, tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se aumento correctamente el inventario")
        else:
            messagebox.showerror("ERROR", "PRECIO COSTO, PRECIO VENTA y CANTIDAD deben ser numericos")
    else:
        messagebox.showerror("ERROR", "No puede haber campos en blanco")
    eid.configure(state = 'normal')
    clean()
    obt_productos()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    bmas["state"] = "disable"
    bmenos["state"] = "disable"

"Acabo de agregar la funcion para la operacion de menos"
def resta_inventario():
    if validacion():
        if eprice_c.get().isdigit() and eprice_v.get().isdigit() and eamount.get().isdigit():
            tu_clave = []
            cant_n = int(eamount.get())
            seleccion = eid.get()
            op_BD=0
            tabla=0
            op_producto = 0
            resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto))
            if cant_n <= int(resultado[3]):
                resta = int(resultado[3]) - cant_n
                tu_clave.append(eid.get())
                tu_clave.append(eprice_c.get())
                tu_clave.append(eprice_v.get())
                tu_clave.append(resta)
                op_BD = 2
                tabla = 0
                base_datos(op_BD, tabla, tu_clave)
            else:
                tu_clave = []
                tu_clave.append(eid.get())
                tu_clave.append(eprice_c.get())
                tu_clave.append(eprice_v.get())
                tu_clave.append(0)
                print(tu_clave)
                op_BD = 2
                tabla = 0
                base_datos(op_BD, tabla, tu_clave)
                messagebox.showwarning("ADVERTENCIA", "Habian "+ str(resultado[3]) +" repuestos de "+ str(seleccion) +" y usted ha restado " +
                str(cant_n) + " asi que se ha colocado la cantidad en 0")
                messagebox.showinfo("BASE DE DATOS", "Se disminuyo correctamente el inventario")
        else:
            messagebox.showerror("ERROR", "PRECIO COSTO, PRECIO VENTA y CANTIDAD deben ser numericos")
    else:
        messagebox.showerror("ERROR", "No puede haber campos en blanco")
    eid.configure(state = 'normal')
    clean()
    obt_productos()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    bmas["state"] = "disable"
    bmenos["state"] = "disable"
            

def clean():
    eid.delete(0, END)
    eprice_c.delete(0, END)
    eprice_v.delete(0, END)
    eamount.delete(0, END)

def seleccionar_click(event):
    clean()
    b1["state"] = "disable"
    b2["state"] = "normal"
    b3["state"] = "normal"
    bmas["state"] = "normal"
    bmenos["state"] = "normal"
    selected = tree.focus()
    values = tree.item(selected, 'values')
    eid.insert(0, values[0])
    eprice_c.insert(0, values[1])
    eprice_v.insert(0, values[2])
    eamount.insert(0, values[3])
    eid.configure(state = 'disable')
    Hovertip(eid, text = "No puede actualizar el ID de los productos ya ingresados", hover_delay = 100)

def windbuscar():

    def buscar():
        if len(ebuscar.get()) != 0 and v.get() != 0:
            if v.get() == 1:
                op_BD=0
                tabla=0
                seleccion=ebuscar.get()
                op_producto=0
                resultado=base_datos(op_BD,tabla,tu_clave,seleccion,op_producto)
                op_busqueda = v.get()
                buscar_pedido()
                global lista_pedido
                lista_pedido = {'busqueda': op_busqueda, 'resultado': resultado}
                print(lista_pedido['resultado'][:])
                print(lista_pedido['busqueda'])
            elif v.get() == 2:
                pass
            elif v.get() == 3:
                pass
            elif v.get() == 4:
                pass
            elif v.get() == 5:
                pass
        else:
            messagebox.showinfo("BUSCAR", "debe colocar la opcion y la palabra clave a buscar")

    def buscar_pedido():
        mostrar_busqueda()
        wind2.destroy()
        wind.deiconify()
        return op_busqueda,resultado
       

    def label_buscar():
        if v.get() == 1:
            lbuscar['text'] = "Ha seleccionado la opcion ID PRODUCTO"
            linstruccion['text'] = "Ingrese el ID del PRODUCTO que desea buscar"
        elif v.get() == 2:
            lbuscar['text'] = "Ha seleccionado la opcion CEDULA CLIENTE"
            linstruccion['text'] = "Ingrese la CI del CLIENTE que desea buscar"
        elif v.get() == 3:
            lbuscar['text'] = "Ha seleccionado la opcion NUMERO FACTURA"
            linstruccion['text'] = "Ingrese el NUMERO de la FACTURA que desea buscar"
        elif v.get() == 4:
            lbuscar['text'] = "Ha seleccionado la opcion NOMBRE CLIENTE"
            linstruccion['text'] = "Ingrese el NOMBRE del CLIENTE que desea buscar"
        elif v.get() == 5:
            lbuscar['text'] = "Ha seleccionado la opcion FECHA"
            linstruccion['text'] = "Ingrese la FECHA del PEDIDO que desea buscar"

    wind2 = Toplevel()
    wind2.resizable(width = 0, height = 0)
    wind2.geometry("450x250")
    wind2.iconbitmap('archivo.ico')
    wind2.title("Aplicacion de Inventario (BUSCAR)")
    lbuscar = Label(wind2, text = "Selecciones lo que desea buscar")
    lbuscar.place(x = 10, y = 10)
    ebuscar = Entry(wind2, width = 30)
    ebuscar.place(x = 200, y = 65)
    bbuscar = ttk.Button(wind2, text = "Buscar", width = 29, command = lambda: buscar())
    bbuscar.place(x = 200, y = 100)
    linstruccion = Label(wind2, text = "")
    linstruccion.place(x = 120, y = 135)
    v = IntVar()
    rb_producto = Radiobutton(wind2, text = "ID PRODUCTO", value = 1, variable = v, command = lambda: label_buscar())
    rb_producto.place(x = 20, y = 50)
    rb_cliente = Radiobutton(wind2, text = "CEDULA CLIENTE", value = 2, variable = v, command = lambda: label_buscar())
    rb_cliente.place(x = 20, y = 80)
    rb_pedido = Radiobutton(wind2, text = "NUMERO FACTURA", value = 3, variable = v, command = lambda: label_buscar())
    rb_pedido.place(x = 20, y = 110)
    rb_nombre = Radiobutton(wind2, text = "NOMBRE CLIENTE", value = 4, variable = v, command = lambda: label_buscar())
    rb_nombre.place(x = 20, y = 140)
    rb_fecha = Radiobutton(wind2, text = "FECHA", value = 5, variable = v, command = lambda: label_buscar())
    rb_fecha.place(x = 20, y = 170)
    wind.iconify()

def windclientes():

    def borrarCLIENTES():
        op_BD = 3
        tabla = 1
        clean_total = 1
        base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente, op_pedido, clean_total)
        clean1()
        obt_clientes()

    def validacion1():
        return len(ci_cliente.get()) != 0 and len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(telefono.get()) != 0 and len(direccion.get()) != 0 and len(deuda.get()) != 0

    def obt_clientes():
        view = tree1.get_children()
        for elementos in view:
            tree1.delete(elementos)
        op_BD=0
        tabla=1
        tu_clave=[]
        seleccion=""
        op_cliente=6
        resultado=(base_datos(op_BD,tabla,tu_clave,seleccion,op_producto,op_cliente))
          
        for row in resultado:
            tree1.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5]))
    
    def actualizar_tabla2():
        view = tree1.get_children()
        for elementos in view:
            tree1.delete(elementos)
        op_BD=0
        tabla=1
        tu_clave=[]
        seleccion=""
        op_cliente=6
        resultado=(base_datos(op_BD,tabla,tu_clave,seleccion,op_producto,op_cliente))
          
        for row in resultado:
            tree1.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5]))
        b_guardar["state"] = "normal"
        b_actualizar["state"] = "disable"
        b_eliminar["state"] = "disable"
        ci_cliente["state"] = "normal"
        clean1()
        
    def agregar_cliente():
        tu_clave=[]
        if validacion1():
            if ci_cliente.get()[0] == 'V' or ci_cliente.get()[0] == 'E' or ci_cliente.get()[0] == 'J':
                if ci_cliente.get()[1:10].isdigit() and nombre.get().isalpha() and apellido.get().isalpha() and direccion.get().isalpha() and deuda.get().isdigit():
                    if len(ci_cliente.get()) <= 11 and len(ci_cliente.get()) >= 3 and len(nombre.get()) < 20 and len(apellido.get()) < 20 and len(telefono.get()) <= 15 and len(direccion.get()) < 50:
                        if telefono.get()[0] == '+' and telefono.get()[1:14].isdigit() or telefono.get()[0:14].isdigit(): 
                            tu_clave.append(ci_cliente.get())
                            tu_clave.append(nombre.get())
                            tu_clave.append(apellido.get())
                            tu_clave.append(telefono.get())
                            tu_clave.append(direccion.get())
                            tu_clave.append(deuda.get())
                            op_BD=1
                            tabla=1
                            base_datos(op_BD,tabla,tu_clave)
                            messagebox.showinfo("BASE DE DATOS", "Se guardaron correctamente los campos")
                        else:
                            messagebox.showerror("ERROR", "La TELEFONO puede comenzar con un numero o un +")
                    else:
                       messagebox.showerror("ERROR", "La CEDULA debe tener entre 3 y 10 numeros, el NOMBRE y el APELLIDO 20 caracteres, el TELEFONO maximo 15 y la DIRECCION maximo 50")     
                else:
                  messagebox.showerror("ERROR", "La CEDULA debe comenzar con V, E o J y continuar con numeros, la DEUDA debe ser numerica, y los demas campos textos")  
            else:
                messagebox.showerror("ERROR", "La CEDULA debe comenzar con V, E o J")
        else:
            messagebox.showerror("ERROR", "No puede haber campos en blanco")
        clean1()
        obt_clientes()      

    def editar_cliente():
        tu_clave=[]
        if validacion1():
            tu_clave.append(ci_cliente.get())
            tu_clave.append(nombre.get())
            tu_clave.append(apellido.get())
            tu_clave.append(telefono.get())
            tu_clave.append(direccion.get())
            tu_clave.append(deuda.get())
            op_BD=2
            tabla=1
            base_datos(op_BD,tabla,tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se actualizaron correctamente los campos")
        else:
            messagebox.showerror("ERROR", "No pueden haber campos en blanco")
        ci_cliente.configure(state = 'normal')
        clean1()
        obt_clientes()
        b_guardar["state"] = "normal"
        b_actualizar["state"] = "disable"
        b_eliminar["state"] = "disable"

    def eliminar_cliente():
        tu_clave=[]
        if len(ci_cliente.get()) != 0:
            tu_clave.append(ci_cliente.get())
            op_BD=3
            tabla=1
            base_datos(op_BD,tabla,tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se eliminaron correctamente los campos")
        else:
            ci_cliente.configure(state = 'normal')
            clean1()
            obt_clientes()
            b_guardar["state"] = "normal"
            b_actualizar["state"] = "disable"
            b_eliminar["state"] = "disable"

    def clean1():
        ci_cliente.delete(0, END)
        nombre.delete(0, END)
        apellido.delete(0, END)
        telefono.delete(0, END)
        direccion.delete(0, END)
        deuda.delete(0, END)

    def buscar_cliente():
        windclientes1.destroy()
        windbuscar()

    def principal_cliente():
        windclientes1.destroy()
        wind.deiconify()
    
    def pedido_cliente():
        windclientes1.destroy()
        windpedido1()

    def seleccionar1_click(event):
        clean1()
        b_guardar["state"] = "disable"
        b_actualizar["state"] = "normal"
        b_eliminar["state"] = "normal"
        selected = tree1.focus()
        values = tree1.item(selected, 'values')
        ci_cliente.insert(0, values[0])
        nombre.insert(0, values[1])
        apellido.insert(0, values[2])
        telefono.insert(0, values[3])
        direccion.insert(0, values[4])
        deuda.insert(0, values[5])
        ci_cliente.configure(state = 'disable')
        Hovertip(ci_cliente, text = "No puede actualizar la cedula de un usuario existente, elimine y cree uno nuevo", hover_delay = 100)

    wind.iconify() 
    windclientes1 = Toplevel()
    windclientes1.resizable(width=0,height=0)
    windclientes1.geometry("900x570")
    windclientes1.iconbitmap('archivo.ico')
    windclientes1.title("Aplicacion de Inventario (CLIENTES)")

    tree1 = ttk.Treeview(windclientes1)
    tree1['columns'] = ("CI_CLIENTE", "NONMBRE", "APELLIDO", "TELEFONO","DIRECCION", "DEUDA")
    tree1.place(x = 0, y = 270)
    tree1.column('#0', width = 0, stretch = NO)
    tree1.column('#1', minwidth = 150, width=150,  anchor = CENTER)
    tree1.column('#2', minwidth = 150, width=150, anchor = CENTER)
    tree1.column('#3', minwidth = 150, width=150, anchor = CENTER)
    tree1.column('#4', minwidth = 150, width=150, anchor = CENTER)
    tree1.column('#5', minwidth = 150, width=150, anchor = CENTER)
    tree1.column('#6', minwidth = 150, width=150, anchor = CENTER)
    tree1.heading('#1', text = 'CEDULA', anchor = CENTER)
    tree1.heading('#2', text = 'NOMBRE', anchor = CENTER)
    tree1.heading('#3', text = 'APELLIDO', anchor = CENTER)
    tree1.heading('#4', text = 'TELEFONO', anchor = CENTER)
    tree1.heading('#5', text = 'DIRECCION', anchor = CENTER)
    tree1.heading('#6', text = 'DEUDA', anchor = CENTER)
    tree1.bind("<Double-Button-1>", seleccionar1_click)
    obt_clientes()

    l_title = Label(windclientes1, text = "Agregue un cliente")
    l_title.place(x = 400, y = 10)

    l_ci_cedula = Label(windclientes1, text = "Cedula Cliente:")
    l_ci_cedula.place(x = 290, y = 40)
    ci_cliente = Entry(windclientes1, width = 40)
    ci_cliente.focus()
    ci_cliente.place(x = 390, y = 40)

    l_nombre = Label(windclientes1, text = "Nombre Cliente:")
    l_nombre.place(x = 282, y = 70)
    nombre = Entry(windclientes1, width = 40)
    nombre.place(x = 390, y = 70)

    l_apellido = Label(windclientes1, text = "Apellido Cliente:")
    l_apellido.place(x = 282, y = 100)
    apellido = Entry(windclientes1, width = 40)
    apellido.place(x = 390, y = 100)

    l_telefono = Label(windclientes1, text = "Telefono Cliente:")
    l_telefono.place(x = 280, y = 130)
    telefono = Entry(windclientes1, width = 40)
    telefono.place(x = 390, y = 130)

    l_direccion = Label(windclientes1, text = "Direccion Cliente:")
    l_direccion.place(x = 276, y = 160)
    direccion = Entry(windclientes1, width = 40)
    direccion.place(x = 390, y = 160)

    l_deuda = Label(windclientes1, text = "Deuda Cliente:")
    l_deuda.place(x = 291, y = 190)
    deuda = Entry(windclientes1, width = 40)
    deuda.place(x = 390, y = 190)

    b_guardar = ttk.Button(windclientes1, text = "Guardar cliente", width = 70, command = lambda: agregar_cliente())
    b_guardar.place(x = 205, y = 225)

    b_eliminar = ttk.Button(windclientes1, text = "Eliminar cliente", width = 70, command = lambda: eliminar_cliente())
    b_eliminar.place(x = 435, y = 510)
    b_eliminar['state'] = 'disable'

    b_actualizar = ttk.Button(windclientes1, text = "Actualizar cliente", width = 70, command = lambda: editar_cliente())
    b_actualizar.place(x = 30, y = 510)
    b_actualizar['state'] = 'disable'

    bpsearch = Button(windclientes1, width = 35, height = 35, command = lambda: buscar_cliente())
    bpsearch.config(image = img)
    bpsearch.place(x = 15, y = 15)
    Hovertip(bsearch, text = "Buscar")
    Hovertip(bpsearch, text = "buscar", hover_delay = 100)

    img6 = PhotoImage(file = 'principal.png')
    bprin_cliente = Button(windclientes1, width = 35, height = 35, command = lambda: principal_cliente())
    bprin_cliente.image_names = img6
    bprin_cliente.config(image = img6)
    bprin_cliente.place(x = 15, y = 65)
    Hovertip(bprin_cliente, text = "Pantalla Principal", hover_delay = 100)

    "Agrege el boton de pedido"
    img7 = PhotoImage(file = 'pedidos.png')
    bpedido1 = Button(windclientes1, width = 35, height = 35, command = lambda: pedido_cliente())
    bpedido1.image_names = img7
    bpedido1.configure(image = img7)
    bpedido1.place(x = 15, y = 115)
    Hovertip(bpedido1, text = "Pedidos", hover_delay = 100)

    "Acabo de agregar el boton actualizar"
    img4 = PhotoImage(file = 'actualizar_tree.png')
    bactualizar_cliente = Button(windclientes1, image = img4, width = 18, height = 18, command = lambda: actualizar_tabla2())
    bactualizar_cliente.place(x = 640, y = 225)
    bactualizar_cliente.image_names = img4
    bactualizar_cliente.config(image = img4)
    Hovertip(bactualizar_cliente, text = "Actualizar Lista", hover_delay = 100)

    menuvar = Menu(windclientes1)
    menuDB = Menu(menuvar, tearoff = 0)
    menuDB.add_command(label = "Limpiar Base De Datos 'CLIENTES'", command = lambda: borrarCLIENTES())
    menuvar.add_cascade(label = "Inicio", menu = menuDB)

    ayudamenu = Menu(menuvar, tearoff = 0)
    ayudamenu.add_command(label = "Resetear Campos", command = lambda: clean1())
    ayudamenu.add_command(label = "Manual de Usuario")
    menuvar.add_cascade(label = "Ayuda", menu = ayudamenu)

    windclientes1.config(menu = menuvar)

def windpedido1():

    def borrarPEDIDO():
            op_BD = 3
            tabla = 2
            clean_total = 1
            base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente, op_pedido, clean_total)
            clean_pedido()
            obt_pedidos()

    def cliente_pedido():
        windpedido.destroy()
        windclientes()

    #def buscar_pedido():
    #     windpedido.destroy()
    #     windbuscar()

    def principal_pedido():
        windpedido.destroy()
        wind.deiconify()

    def validacion_pedido():
        return len(eci.get()) != 0 and len(eid_pro.get()) != 0 and len(ecant.get()) != 0

    def obt_pedidos():
        view = tree3.get_children()
        for elementos in view:
            tree3.delete(elementos)
        op_BD=0
        tabla=3
        op_pedido=5
        resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente, op_pedido))
        for row in resultado:
            tree3.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4]))

    def actualizar_tabla1():
        view = tree3.get_children()
        for elementos in view:
            tree3.delete(elementos)
        op_BD=0
        tabla=3
        op_pedido=5
        resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente, op_pedido))
        for row in resultado:
            tree3.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4]))
        eci.configure(state = 'normal')
        eid_pro.configure(state = 'normal')
        ecant.configure(state = 'normal')
        bgpedido["state"] = "normal"
        bepedido["state"] = "disable"
        clean_pedido()

    def agregar_pedido():
        if validacion_pedido():
            tu_clave = []
            seleccion = eid_pro.get()
            op_BD=0
            tabla=0
            op_producto = 0
            resultado1 = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto))
            if int(ecant.get()) <= int(resultado1[3]):
                disminuir_inventario = int(resultado1[3]) - int(ecant.get())
                tu_clave = []
                tu_clave.append(resultado1[0])
                tu_clave.append(resultado1[1])
                tu_clave.append(resultado1[2])
                tu_clave.append(disminuir_inventario)
                op_BD = 2
                tabla = 0
                seleccion = eid_pro.get()
                base_datos(op_BD, tabla, tu_clave, seleccion)
                tu_clave = []
                op_producto = 9
                seleccion = eci.get()
                op_BD=0
                tabla=1
                op_cliente = 0
                resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente))
                sumar_deuda = (int(ecant.get()) * int(resultado1[2])) + resultado[5]
                tu_clave = []
                tu_clave.append(resultado[0])
                tu_clave.append(resultado[1])
                tu_clave.append(resultado[2])
                tu_clave.append(resultado[3])
                tu_clave.append(resultado[4])
                tu_clave.append(resultado[5])
                tu_clave.remove(resultado[5])
                tu_clave.append(sumar_deuda)
                op_BD=2
                tabla=1
                base_datos(op_BD, tabla, tu_clave)
                tu_clave = []
                tu_clave.append(eci.get())
                tu_clave.append(eid_pro.get())
                tu_clave.append(ecant.get())
                tu_clave.append(str_now)
                op_BD = 1
                tabla = 2
                base_datos(op_BD, tabla, tu_clave)
                messagebox.showinfo("BASE DE DATOS", "Se guardo correctamente el pedido y se actualizaron los campos inventario y deuda")
            else:
                messagebox.showerror("ERROR", "No pueden haber pedidos que la Cantidad Pedido exceda la Cantidad disponible en el inventario")
        else:
            messagebox.showerror("ERROR", "No pueden haber campos en blanco")
        obt_pedidos()
        obt_productos()
        clean_pedido()

    def clean_pedido():
        eci.delete(0, END)
        eid_pro.delete(0, END)
        ecant.delete(0, END)
        enumero_factura.delete(0, END)

    def eliminar_pedido():
        enumero_factura.configure(state = 'normal')
        if validacion_pedido():
            tu_clave = []
            seleccion = eid_pro.get()
            op_BD=0
            tabla=0
            op_producto = 0
            resultado1 = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto))
            disminuir_inventario = int(resultado1[3]) + int(ecant.get())
            tu_clave = []
            tu_clave.append(resultado1[0])
            tu_clave.append(resultado1[1])
            tu_clave.append(resultado1[2])
            tu_clave.append(disminuir_inventario)
            op_BD = 2
            tabla = 0
            seleccion = eid_pro.get()
            base_datos(op_BD, tabla, tu_clave, seleccion)
            tu_clave = []
            op_producto = 9
            seleccion = eci.get()
            op_BD=0
            tabla=1
            op_cliente = 0
            resultado = (base_datos(op_BD, tabla, tu_clave, seleccion, op_producto, op_cliente))
            if (int(ecant.get()) * int(resultado1[2])) < resultado[5]:
                sumar_deuda = resultado[5] - (int(ecant.get()) * int(resultado1[2])) 
                tu_clave = []
                tu_clave.append(resultado[0])
                tu_clave.append(resultado[1])
                tu_clave.append(resultado[2])
                tu_clave.append(resultado[3])
                tu_clave.append(resultado[4])
                tu_clave.append(resultado[5])
                tu_clave.remove(resultado[5])
                tu_clave.append(sumar_deuda)
            else:
                messagebox.showerror("ERROR", "Hubo un error al eliminar datos datos")
            op_BD=2
            tabla=1
            base_datos(op_BD, tabla, tu_clave)
            tu_clave = []
            tu_clave.append(enumero_factura.get())
            op_BD = 3
            tabla = 2
            base_datos(op_BD, tabla, tu_clave)
            messagebox.showinfo("BASE DE DATOS", "Se elimino correctamente el pedido y se actualizaron los campos inventario y deuda")
        else:
            messagebox.showerror("ERROR", "No pueden haber campos en blanco")
        eci.configure(state = 'normal')
        eid_pro.configure(state = 'normal')
        ecant.configure(state = 'normal')
        bgpedido["state"] = "normal"
        bepedido["state"] = "disable"
        obt_pedidos()
        obt_productos()
        clean_pedido()
        enumero_factura.configure(state = 'disable')

    def seleccionar_click2(event):
        clean()
        enumero_factura.configure(state = 'normal')
        bgpedido["state"] = "disable"
        bepedido["state"] = "normal"
        selected = tree3.focus()
        values = tree3.item(selected, 'values')
        enumero_factura.insert(0, values[0])
        eci.insert(0, values[1])
        eid_pro.insert(0, values[2])
        ecant.insert(0, values[3])
        eci.configure(state = 'disable')
        if messagebox.askyesno(message="¿Desea usar la funcion eliminar pedido?", title="CONFIRMACION"):
            eid_pro.configure(state = 'disable')
            ecant.configure(state = 'disable')
        Hovertip(eci, text = "No puede actualizar la CI Cliente de los pedidos ya ingresados", hover_delay = 100)
        enumero_factura.configure(state = 'disable')
       
    wind.iconify()
    windpedido = Toplevel()
    windpedido.resizable(width = 0, height = 0)
    windpedido.geometry("1000x500")
    windpedido.iconbitmap('archivo.ico')
    windpedido.title("Aplicacion de Inventario (PEDIDOS)")

    tree3 = ttk.Treeview(windpedido)
    tree3['columns'] = ("N_FACTURA", "CI_CLIENTE", "ID_PRODUCTO", "CANTIDAD_PRODUCTO", "FECHA")
    tree3.place(x = 0, y = 200)
    tree3.bind("<Double-Button-1>", seleccionar_click2)
    tree3.column('#0', width = 0, stretch = NO)
    tree3.column('#1', minwidth = 200, anchor = CENTER)
    tree3.column('#2', minwidth = 200, anchor = CENTER)
    tree3.column('#3', minwidth = 200, anchor = CENTER)
    tree3.column('#4', minwidth = 200, anchor = CENTER)
    tree3.column('#5', minwidth = 200, anchor = CENTER)
    tree3.heading('#1', text = 'NUMERO FACTURA', anchor = CENTER)
    tree3.heading('#2', text = 'CI CLIENTE', anchor = CENTER)
    tree3.heading('#3', text = 'ID PRODUCTO', anchor = CENTER)
    tree3.heading('#4', text = 'CANTIDAD PRODUCTO', anchor = CENTER)
    tree3.heading('#5', text = 'FECHA', anchor = CENTER)
    obt_pedidos()

    l2 = Label(windpedido, text = "Ingrese un pedido")
    l2.place(x = 445, y = 5)

    lnumero_factura = Label(windpedido, text = "Numero Factura: ")
    lnumero_factura.place(x = 383, y = 35)
    enumero_factura = Entry(windpedido, width = 30)
    enumero_factura.place(x = 500, y = 35)
    enumero_factura.configure(state = 'disable')

    lci = Label(windpedido, text = "CI Cliente: ")
    lci.place(x = 416, y = 65)
    eci = Entry(windpedido, width = 30)
    eci.focus()
    eci.place(x = 500, y = 65)

    lid_pro = Label(windpedido, text = "ID Producto: ")
    lid_pro.place(x = 404, y = 95)
    eid_pro = Entry(windpedido, width = 30)
    eid_pro.place(x = 500, y = 95)

    lcant = Label(windpedido, text = "Cantidad Producto: ")
    lcant.place(x = 367, y = 125)
    ecant = Entry(windpedido, width = 30)
    ecant.place(x = 500, y = 125)

    bgpedido = ttk.Button(windpedido, text = "Guardar Pedido", width = 60, command =  lambda: agregar_pedido())
    bgpedido.place(x = 315, y = 160)

    bepedido = ttk.Button(windpedido, text = "Eliminar Pedido", width = 60, command = lambda: eliminar_pedido())
    bepedido.place(x = 315, y = 450)
    bepedido['state'] = 'disable'

    bpsearch = Button(windpedido, width = 35, height = 35, command = lambda: buscar_pedido())
    bpsearch.config(image = img)
    bpsearch.place(x = 15, y = 15)
    Hovertip(bpsearch, text = "buscar", hover_delay = 100)

    img6 = PhotoImage(file = 'principal.png')
    bprin_pedido = Button(windpedido, width = 35, height = 35, command = lambda: principal_pedido())
    bprin_pedido.image_names = img6
    bprin_pedido.config(image = img6)
    bprin_pedido.place(x = 15, y = 65)
    Hovertip(bprin_pedido, text = "Pantalla Principal", hover_delay = 100)

    img7 = PhotoImage(file = 'cliente.png')
    bpedido = Button(windpedido, width = 35, height = 35, command = lambda: cliente_pedido())
    bpedido.image_names = img7
    bpedido.configure(image = img7)
    bpedido.place(x = 15, y = 115)
    Hovertip(bpedido, text = "Clientes", hover_delay = 100)

    "Acabo de agregar el boton actualizar"
    img4 = PhotoImage(file = 'actualizar_tree.png')
    bactualizar_cliente = Button(windpedido, image = img4, width = 18, height = 18, command = lambda: actualizar_tabla1())
    bactualizar_cliente.place(x = 690, y = 160)
    bactualizar_cliente.image_names = img4
    bactualizar_cliente.config(image = img4)
    Hovertip(bactualizar_cliente, text = "Actualizar Lista", hover_delay = 100)

    menuvar = Menu(windpedido)
    menuDB = Menu(menuvar, tearoff = 0)
    menuDB.add_command(label = "Limpiar Base De Datos 'PEDIDOS'", command = lambda: borrarPEDIDO())
    menuvar.add_cascade(label = "Inicio", menu = menuDB)

    ayudamenu = Menu(menuvar, tearoff = 0)
    ayudamenu.add_command(label = "Resetear Campos", command = lambda: clean_pedido())
    ayudamenu.add_command(label = "Manual de Usuario")
    menuvar.add_cascade(label = "Ayuda", menu = ayudamenu)
    
    windpedido.config(menu = menuvar)

wn = Tk()
wind = wn

wind = wn
wind.title("Aplicacion de Inventario (PRODUCTOS)")
wind.resizable(width = 0, height = 0)
wind.geometry("802x500")
wind.iconbitmap('archivo.ico')
    
tree = ttk.Treeview(wn)
tree['columns'] = ("ID_PRODUCTO", "PRECIO_COSTO", "PRECIO_VENTA", "CANTIDAD")
tree.place(x = 0, y = 200)
tree.column('#0', width = 0, stretch = NO)
tree.column('#1', minwidth = 200, anchor = CENTER)
tree.column('#2', minwidth = 200, anchor = CENTER)
tree.column('#3', minwidth = 200, anchor = CENTER)
tree.column('#4', minwidth = 200, anchor = CENTER)
tree.heading('#1', text = 'ID PRODUCTO', anchor = CENTER)
tree.heading('#2', text = 'PRECIO COSTO', anchor = CENTER)
tree.heading('#3', text = 'PRECIO VENTA', anchor = CENTER)
tree.heading('#4', text = 'CANTIDAD', anchor = CENTER)
tree.bind("<Double-Button-1>", seleccionar_click)

l1 = Label(wind, text = "Agregue un producto")
l1.place(x = 345, y = 15)

lid = Label(wind, text = "ID Producto: ")
lid.place(x = 305, y = 40)
eid = Entry(wind, width = 30)
eid.focus()
eid.place(x = 400, y = 40)

lprice_c = Label(wind, text = "Precio Costo: ")
lprice_c.place(x = 300, y = 70)
eprice_c = Entry(wind, width = 30)
eprice_c.place(x = 400, y = 70)

lprice_v = Label(wind, text = "Precio Venta: ")
lprice_v.place(x = 300, y = 100)
eprice_v = Entry(wind, width = 30)
eprice_v.place(x = 400, y = 100)

lamount = Label(wind, text = "Cantidad: ")
lamount.place(x = 318, y = 130)
eamount = Entry(wind, width = 30)
eamount.place(x = 400, y = 130)

b1 = ttk.Button(wind, text = "Guardar producto", width = 60, command = lambda: agregar_producto())
b1.place(x = 215, y = 160)

b2 = ttk.Button(wind, text = "Eliminar Producto", width = 60, command = lambda: eliminar_producto())
b2.place(x = 400, y = 440)
b2['state'] = 'disable'

b3 = ttk.Button(wind, text = "Actualizar Producto", width = 60, command = lambda: editar_producto())
b3.place(x = 30, y = 440)
b3['state'] = 'disable'

img = PhotoImage(file = 'buscar.png')
bsearch = Button(wind, width = 35, height = 35, command = lambda: windbuscar())
bsearch.image_names = img
bsearch.config(image = img)
bsearch.place(x = 15, y = 15)
Hovertip(bsearch, text = "Buscar", hover_delay = 100)

img1=PhotoImage(file='cliente.png')
bclientes= Button(wind,width=35,height=35, command = lambda: windclientes())
bclientes.image_names = img1
bclientes.config(image=img1)
bclientes.place(x=15,y=65)
Hovertip(bclientes, text = "Clientes", hover_delay = 100)

"Acabo de agregar el boton MAS"
img2 = PhotoImage(file = 'sumar_inventario.png')
bmas = Button(wind, width = 15, height = 15, command = lambda: suma_inventario())
bmas.image_names = img2
bmas.config(image = img2)
bmas.place(x = 590, y = 130)
bmas['state'] = 'disable'

"Acabo de agregar el boton MENOS"
img3 = PhotoImage(file = 'restar_inventario.png')
bmenos = Button(wind, width = 15, height = 15, command = lambda: resta_inventario())
bmenos.image_names = img3
bmenos.config(image = img3)
bmenos.place(x = 615, y = 130)
bmenos['state'] = 'disable'

"Acabo de agregar el boton actualizar"
img4 = PhotoImage(file = 'actualizar_tree.png')
bactualizar = Button(wind, image = img4, width = 18, height = 18, command = lambda: actualizar_tabla())
bactualizar.place(x = 590, y = 160)
bactualizar.image_names = img4
bactualizar.config(image = img4)
Hovertip(bactualizar, text = "Actualizar Lista", hover_delay = 100)

"Agrege el boton de pedido"
img5 = PhotoImage(file = 'pedidos.png')
bpedido = Button(wind, width = 35, height = 35, command = lambda: windpedido1())
bpedido.image_names = img5
bpedido.configure(image = img5)
bpedido.place(x = 15, y = 115)
Hovertip(bpedido, text = "Pedidos", hover_delay = 100)

menuvar = Menu(wind)
menuDB = Menu(menuvar, tearoff = 0)
menuDB.add_command(label = "Limpiar Base De Datos 'PRODUCTO'", command = lambda: borrarPRODUCTO())
menuvar.add_cascade(label = "Inicio", menu = menuDB)

ayudamenu = Menu(menuvar, tearoff = 0)
ayudamenu.add_command(label = "Resetear Campos", command = lambda: clean())
ayudamenu.add_command(label = "Manual de Usuario")
menuvar.add_cascade(label = "Ayuda", menu = ayudamenu)

wind.config(menu = menuvar)

app = wind
wn.mainloop()