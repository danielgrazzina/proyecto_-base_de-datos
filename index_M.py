from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
from idlelib.tooltip import Hovertip
from datetime import datetime
import sqlite3



def main():
    wn = Tk()
    app=main(wn)
    xe = 400
    ye = 15

    wind = wn
    wind.title("Aplicacion de Inventario")
    wind.resizable(width = 0, height = 0)
    wind.geometry("802x500")
    wind.iconbitmap('archivo.ico')
    
    tree = ttk.Treeview(wn)
    tree['columns'] = ("ID", "PRECIO_COSTO", "PRECIO_VENTA", "CANTIDAD")
    tree.place(x = 0, y = 200)
    tree.bind("<Double-Button-1>", seleccionar_click)
    tree.column('#0', width = 0, stretch = NO)
    tree.column('#1', minwidth = 200, anchor = CENTER)
    tree.column('#2', minwidth = 200, anchor = CENTER)
    tree.column('#3', minwidth = 200, anchor = CENTER)
    tree.column('#4', minwidth = 200, anchor = CENTER)
    tree.heading('#1', text = 'ID', anchor = CENTER)
    tree.heading('#2', text = 'PRECIO COSTO', anchor = CENTER)
    tree.heading('#3', text = 'PRECIO VENTA', anchor = CENTER)
    tree.heading('#4', text = 'CANTIDAD', anchor = CENTER)
    obt_productos()

    l1 = Label(wind, text = "Agregue un producto")
    l1.place(x = (xe - 55), y = ye)

    lid = Label(wind, text = "ID: ")
    lid.place(x = 356, y = 40)
    id = Entry(wind, width = 30)
    id.focus()
    id.place(x = xe, y = (ye + 25))

    lprice_c = Label(wind, text = "Precio Costo: ")
    lprice_c.place(x = 300, y = 70)
    price_c = Entry(wind, width = 30)
    price_c.place(x = xe, y = (ye + 55))

    lprice_v = Label(wind, text = "Precio Venta: ")
    lprice_v.place(x = 300, y = 100)
    price_v = Entry(wind, width = 30)
    price_v.place(x = xe, y = (ye + 85))

    lamount = Label(wind, text = "Cantidad: ")
    lamount.place(x = 318, y = 130)
    amount = Entry(wind, width = 30)
    amount.place(x = xe, y = (ye + 115))

    b1 = ttk.Button(wind, text = "Guardar producto", width = 60, command =  agregar_producto)
    b1.place(x = (xe - 185), y = (ye + 145))

    b2 = ttk.Button(wind, text = "Eliminar Producto", width = 60, command =  eliminar_producto)
    b2.place(x = (xe), y = (ye + 435))
    b2['state'] = 'disable'

    b3 = ttk.Button(wind, text = "Actualizar Producto", width = 60, command =  editar_producto)
    b3.place(x = 30, y = (ye + 435))
    b3['state'] = 'disable'

    img = PhotoImage(file = 'lupa.png')
    bsearch = Button(wind, width = 35, height = 35, command = windbuscar)
    bsearch.config(image = img)
    bsearch.place(x = 15, y = 15)
    Hovertip(bsearch, text = "Buscar", hover_delay = 100)

    img1=PhotoImage(file='clientes.png')
    bclientes= Button(wind,width=35,height=35,command=windclientes)
    bclientes.config(image=img1)
    bclientes.place(x=15,y=65)
    Hovertip(bclientes, text = "Clientes", hover_delay = 100)

    "Acabo de agregar el boton MAS"
    img2 = PhotoImage(file = 'mas.png')
    bmas = Button(wind, width = 15, height = 15, command = suma_inventario)
    bmas.config(image = img2)
    bmas.place(x = 590, y = 130)

    "Acabo de agregar el boton MENOS"
    img3 = PhotoImage(file = 'menos.png')
    bmenos = Button(wind, width = 15, height = 15, command = resta_inventario)
    bmenos.config(image = img3)
    bmenos.place(x = 615, y = 130)

    "Acabo de agregar el boton actualizar"
    img4 = PhotoImage(file = 'actualizar.png')
    bactualizar = Button(wind, width = 18, height = 18, command = obt_productos)
    bactualizar.configure(image = img4)
    bactualizar.place(x = 590, y = 160)

    "Agrege el boton de pedido"
    img5 = PhotoImage(file = 'pedido.png')
    bpedido = Button(wind, width = 35, height = 35, command = windpedido1)
    bpedido.configure(image = img5)
    bpedido.place(x = 15, y = 115)
    Hovertip(bpedido, text = "PEDIDOS")

    menuvar = Menu(wind)
    menuDB = Menu(menuvar, tearoff = 0)
    menuDB.add_command(label = "Limpiar Base De Datos 'PRODUCTO'", command = borrarDB)
    menuvar.add_cascade(label = "Inicio", menu = menuDB)

    ayudamenu = Menu(menuvar, tearoff = 0)
    ayudamenu.add_command(label = "Resetear Campos", command = clean)
    ayudamenu.add_command(label = "Manual de Usuario")# command = manual_usuario)
    menuvar.add_cascade(label = "Ayuda", menu = ayudamenu)

    wind.config(menu = menuvar)

    wn.mainloop()

def run_query(self, query, parametros = ()):
    with sqlite3.connect('inventario.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parametros)
        conn.commit()
    return result

def borrarDB(self):
    try:
        if messagebox.askyesno(message = "Se borraran todos los PRODUCTOS, ¿Desea continuar?", title = "ADVERTENCIA"):
            query = 'DELETE FROM producto WHERE ID_PRODUCTO = ID_PRODUCTO'
            run_query(query)
            obt_productos()
            clean()
            messagebox.showinfo("BASE DE DATOS", "Se vacio exitosamente la tabla 'PRODUCTO'")
    except:
        messagebox.showerror("ERROR", "No se pudo vaciar la tabla 'PRODUCTO'")

def windbuscar(self):
    wind.iconify()
    wind2 = Toplevel()
    wind2.resizable(width = 0, height = 0)
    wind2.geometry("400x200+400+400")
    wind2.iconbitmap('archivo.ico')
    lbuscar = Label(wind2, text = "Selecciones lo que desea buscar")
    lbuscar.place(x = 10, y = 10)
    ebuscar = Entry(wind2, width = 30)
    ebuscar.place(x = 150, y = 65)
    bbuscar = ttk.Button(wind2, text = "Buscar", width = 29, command = buscar)
    bbuscar.place(x = 150, y = 100)
    linstruccion = Label(wind2, text = "")
    linstruccion.place(x = 120, y = 135)
    v = IntVar()
    rb_producto = Radiobutton(wind2, text = "PRODUCTO", value = 1, variable = v, command = prueba)
    rb_producto.place(x = 20, y = 50)
    rb_cliente = Radiobutton(wind2, text = "CLIENTE", value = 2, variable = v, command = prueba)
    rb_cliente.place(x = 20, y = 80)
    rb_pedido = Radiobutton(wind2, text = "PEDIDO", value = 3, variable = v, command = prueba)
    rb_pedido.place(x = 20, y = 110)
    
def windclientes (self):
    wind.iconify() 
    windclientes1 = Toplevel()
    windclientes1.resizable(width=0,height=0)
    windclientes1.geometry("900x550+200+50")
    windclientes1.iconbitmap('archivo.ico')
    windclientes1.title("Clientes")

    tree1 = ttk.Treeview(windclientes1)
    tree1['columns'] = ("CI_CLIENTE", "NONMBRE", "APELLIDO", "TELEFONO","DIRECCION", "DEUDA")
    tree1.place(x = 0, y = 270)
    tree1.bind("<Double-Button-1>", seleccionar1_click)
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
    obt_clientes()

    l_title = Label(windclientes1, text = "Agregue un cliente")
    l_title.place(x = (xe), y = ye)

    l_ci_cedula = Label(windclientes1, text = "Cedula: ")
    l_ci_cedula.place(x = 376, y = 40)
    ci_cliente = Entry(windclientes1, width = 30)
    ci_cliente.focus()
    ci_cliente.place(x = (xe + 60), y = (ye + 25))

    l_nombre = Label(windclientes1, text = "nombre: ")
    l_nombre.place(x = 370, y = 70)
    nombre = Entry(windclientes1, width = 30)
    nombre.place(x = (xe + 60), y = (ye + 55))

    l_apellido = Label(windclientes1, text = "apellido: ")
    l_apellido.place(x = 370, y = 100)
    apellido = Entry(windclientes1, width = 30)
    apellido.place(x = (xe + 60), y = (ye + 85))

    l_telefono = Label(windclientes1, text = "telefono: ")
    l_telefono.place(x = 370, y = 130)
    telefono = Entry(windclientes1, width = 30)
    telefono.place(x = (xe + 60), y = (ye + 115))

    l_direccion = Label(windclientes1, text = "direccion: ")
    l_direccion.place(x = 366, y = 160)
    direccion = Entry(windclientes1, width = 30)
    direccion.place(x = (xe + 60), y = (ye + 145))

    l_deuda = Label(windclientes1, text = "deuda: ")
    l_deuda.place(x = 382, y = 190)
    deuda = Entry(windclientes1, width = 30)
    deuda.place(x = (xe + 60), y = (ye + 175))

    b_guardar = ttk.Button(windclientes1, text = "Guardar cliente", width = 70, command =  agregar_cliente)
    b_guardar.place(x = (xe - 170), y = (ye + 210))

    b_eliminar = ttk.Button(windclientes1, text = "Eliminar cliente", width = 70, command =  eliminar_cliente)
    b_eliminar.place(x = (xe + 35), y = (ye + 500))
    b_eliminar['state'] = 'disable'

    b_actualizar = ttk.Button(windclientes1, text = "Actualizar cliente", width = 70, command =  editar_cliente)
    b_actualizar.place(x = 30, y = (ye + 500))
    b_actualizar['state'] = 'disable'

    bpsearch = Button(windclientes1, width = 35, height = 35, command = buscar_cliente)
    bpsearch.config(image = img)
    bpsearch.place(x = 15, y = 15)
    Hovertip(bsearch, text = "BUSCAR")

    img7 = PhotoImage(file = 'home.png')
    bprin_cliente = Button(windclientes1, width = 35, height = 35, command = principal_cliente)
    bprin_cliente.config(image = img7)
    bprin_cliente.place(x = 15, y = 65)
    Hovertip(bprin_cliente, text = "PANTALLA PRINCIPAL")

def windpedido1(self):
    wind.iconify()
    windpedido = Toplevel()
    windpedido.resizable(width = 0, height = 0)
    windpedido.geometry("800x500")
    windpedido.iconbitmap('archivo.ico')

    l2 = Label(windpedido, text = "Ingrese un pedido")
    l2.place(x = 345, y = 40)

    lci = Label(windpedido, text = "CI: ")
    lci.place(x = 356, y = 65)
    ci = Entry(windpedido, width = 30)
    ci.focus()
    ci.place(x = 400, y = 65)

    lid_pro = Label(windpedido, text = "ID Producto: ")
    lid_pro.place(x = 304, y = 95)
    id_pro = Entry(windpedido, width = 30)
    id_pro.place(x = 400, y = 95)

    lcant = Label(windpedido, text = "Cantidad Producto: ")
    lcant.place(x = 267, y = 125)
    cant = Entry(windpedido, width = 30)
    cant.place(x = 400, y = 125)

    bgpedido = ttk.Button(windpedido, text = "Guardar Pedido", width = 60, command = agregar_pedido)
    bgpedido.place(x = 215, y = 160)

    bepedido = ttk.Button(windpedido, text = "Eliminar Pedido", width = 60, command =  eliminar_producto)
    bepedido.place(x = 400, y = 450)
    bepedido['state'] = 'disable'

    bapedido = ttk.Button(windpedido, text = "Actualizar Pedido", width = 60, command =  editar_producto)
    bapedido.place(x = 30, y = 450)
    bapedido['state'] = 'disable'

    bpsearch = Button(windpedido, width = 35, height = 35, command = buscar_pedido)
    bpsearch.config(image = img)
    bpsearch.place(x = 15, y = 15)
    Hovertip(bsearch, text = "BUSCAR")

    img6 = PhotoImage(file = 'home.png')
    bprin_pedido = Button(windpedido, width = 35, height = 35, command = principal_pedido)
    bprin_pedido.config(image = img6)
    bprin_pedido.place(x = 15, y = 65)
    Hovertip(bprin_pedido, text = "PANTALLA PRINCIPAL")

    tree3 = ttk.Treeview(windpedido)
    tree3['columns'] = ("CI", "ID_PRODUCTO", "CANTIDAD_PRODUCTO", "FECHA")
    tree3.place(x = 0, y = 200)
    tree3.bind("<Double-Button-1>", seleccionar_click)
    tree3.column('#0', width = 0, stretch = NO)
    tree3.column('#1', minwidth = 200, anchor = CENTER)
    tree3.column('#2', minwidth = 200, anchor = CENTER)
    tree3.column('#3', minwidth = 200, anchor = CENTER)
    tree3.column('#4', minwidth = 200, anchor = CENTER)
    tree3.heading('#1', text = 'CI CLIENTE', anchor = CENTER)
    tree3.heading('#2', text = 'ID PRODUCTO', anchor = CENTER)
    tree3.heading('#3', text = 'CANTIDAD PRODUCTO', anchor = CENTER)
    tree3.heading('#4', text = 'FECHA', anchor = CENTER)
    obt_pedidos()

def buscar_cliente(self):
    windclientes1.destroy()
    windbuscar()

def principal_cliente(self):
    windclientes1.destroy()
    wind.deiconify()

def buscar_pedido(self):
    windpedido.destroy()
    windbuscar()

def principal_pedido(self):
    windpedido.destroy()
    wind.deiconify()

def prueba(self):
    if v.get() == 1:
        lbuscar['text'] = "Ha seleccionado la opcion PRODUCTO"
        linstruccion['text'] = "Ingrese el ID del PRODUCTO que desea buscar"
    elif v.get() == 2:
        lbuscar['text'] = "Ha seleccionado la opcion CLIENTE"
        linstruccion['text'] = "Ingrese la CI del CLIENTE que desea buscar"
    elif v.get() == 3:
        lbuscar['text'] = "Ha seleccionado la opcion PEDIDO"
        linstruccion['text'] = "Ingrese el ID del PEDIDO que desea buscar"

def buscar(self):
    if len(ebuscar.get()) != 0 and v.get() != 0:
        if v.get() == 1:
            query = "SELECT * FROM producto WHERE ID_PRODUCTO = ? ORDER BY ID_PRODUCTO DESC"
            parametros = (ebuscar.get())
            view = tree.get_children()
        
            for elementos in view:
                tree.delete(elementos)
            
            db_rows = run_query(query, (parametros, ))

            for row in db_rows:
                tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))
            
            wind.deiconify()
            wind2.destroy()

        elif v.get() == 2:
            query = "SELECT * FROM cliente WHERE CI_CLIENTE = ? ORDER BY NOMBRE DESC"
            parametros = (ebuscar.get())
            windclientes()
            view = tree1.get_children()

            for elementos in view:
                tree1.delete(elementos)
            
            db_rows = run_query(query, (parametros, ))

            for row in db_rows:
                tree1.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5]))
            
            wind.deiconify()
            wind2.destroy()
        elif v.get() == 3:
            query = "SELECT * FROM pedido WHERE ID = ? ORDER BY ID DESC"
            parametros = (ebuscar.get())
            windpedido1()
            view = tree3.get_children()

            for elementos in view:
                tree3.delete(elementos)
            
            db_rows = run_query(query, (parametros, ))

            for row in db_rows:
                tree3.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))
            
            wind.deiconify()
            wind2.destroy()
        
        
    else:
        messagebox.showwarning("ADVERTENCIA", "Debe elegir una opcion, y rellenar el campo con lo que seas buscar")

def clean(self):
    id.delete(0, END)
    price_c.delete(0, END)
    price_v.delete(0, END)
    amount.delete(0, END)

def clean1(self):
    ci_cliente.delete(0, END)
    nombre.delete(0, END)
    apellido.delete(0, END)
    telefono.delete(0, END)
    direccion.delete(0, END)
    deuda.delete(0, END)

def clean_pedido(self):
    ci.delete(0, END)
    id_pro.delete(0, END)
    cant.delete(0, END)

def obt_productos(self):
    view = tree.get_children()
    for elementos in view:
        tree.delete(elementos)
        
    query = "SELECT * FROM producto ORDER BY ID_PRODUCTO DESC"
    db_rows = run_query(query)
    for row in db_rows:
        tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))

def obt_clientes(self):
    view = tree1.get_children()
    for elementos in view:
        tree1.delete(elementos)
        
    query = "SELECT * FROM cliente ORDER BY NOMBRE DESC"
    db_rows = run_query(query) 
    for row in db_rows:
        tree1.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5]))

def obt_pedidos(self):
    view = tree3.get_children()
    for elementos in view:
        tree3.delete(elementos)

    query = "SELECT * FROM pedido ORDER BY CI_CLIENTE DESC"
    db_rows = run_query(query)
    for row in db_rows:
        tree3.insert("", 0, text = "", values = (row[1], row[2], row[3], row[4]))

def validacion(self):
    return len(id.get()) != 0 and len(price_c.get()) != 0 and len(price_v.get()) != 0 and len(amount.get()) != 0

def validacion1(self):
    return len(ci_cliente.get()) != 0 and len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(telefono.get()) != 0 and len(direccion.get()) != 0 and len(deuda.get()) != 0

def validacion_pedido(self):
    return len(ci.get()) != 0 and len(id_pro.get()) != 0 and len(cant.get()) != 0

def agregar_producto(self):
    if validacion():
        query = "INSERT INTO producto VALUES(?, ?, ?, ?)"
        parametros = (id.get(), price_c.get(), price_v.get(), amount.get())
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Datos guardados satisfactoriamente")
    else:
        messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
    obt_productos()
    clean()

def agregar_cliente(self):
    if validacion1():
        query = "INSERT INTO cliente VALUES(?, ?, ?, ?, ?, ?)"
        parametros = (ci_cliente.get(), nombre.get(), apellido.get(), telefono.get(), direccion.get(), deuda.get())
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Datos guardados satisfactoriamente")
    else:
        messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
    obt_clientes()
    clean1()

def agregar_pedido(self):
    if validacion_pedido():
        query = "INSERT INTO pedido VALUES(NULL, ?, ?, ?, ?)"
        parametros = (ci.get(), id_pro.get(), cant.get(), dia())
        run_query(query, parametros)
        deuda_fun()
        messagebox.showinfo("BASE DE DATOS", "Datos guardados satisfactoriamente")
        obt_pedidos()
    else:
        messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
    
    #clean_pedido()

def deuda_fun(self):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    query = ("SELECT PRECIO_VENTA FROM producto WHERE ID_PRODUCTO = ?")
    parametros = id_pro.get()
    cursor.execute(query, (parametros, ))
    precio = cursor.fetchone()
    valor_precio = precio[0]
    if precio:
        query = ("SELECT DEUDA FROM cliente WHERE CI_CLIENTE = ?")
        parametros = (ci.get())
        cursor.execute(query, (parametros, ))
        deuda1 = cursor.fetchone()
        valor_deuda = deuda1[0]
        if deuda1:
            cant_deuda = cant.get()
            total = (int(cant_deuda) * valor_precio) + valor_deuda
            query = "UPDATE cliente SET DEUDA = ? WHERE CI_CLIENTE = ?"
            parametros = (total, ci.get())
            run_query(query, parametros)
        else:
            messagebox.showerror("ERROR", "Debe ingresar un cliente y su deuda")
    else:
        messagebox.showerror("ERROR", "Debe ingresar un producto y su precio de venta")

def editar_producto(self):
    if validacion():
        parametros = (price_c.get(), price_v.get(), amount.get(), id.get())
        query = ("UPDATE producto SET PRECIO_COSTO = ? , PRECIO_VENTA = ?, CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?")
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Datos actualizados satisfactoriamente")
    else:
        messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
    obt_productos()
    id.configure(state = 'normal')  
    clean()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"

def editar_cliente(self):
    if validacion1():
        parametros = (nombre.get(), apellido.get(), telefono.get(), direccion.get(), deuda.get(), ci_cliente.get())
        query = ("UPDATE cliente SET NOMBRE = ? , APELLIDO = ?, TELEFONO = ?, DIRECCION = ?, DEUDA = ? WHERE CI_CLIENTE = ?")
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Datos actualizados satisfactoriamente")
    else:
        messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
    obt_clientes()
    ci_cliente.configure(state = 'normal')
    clean1()
    b_guardar["state"] = "normal"
    b_eliminar["state"] = "disable"
    b_actualizar["state"] = "disable"

def eliminar_producto(self):
    try:
        if messagebox.askyesno(message = "El registro se borrara permanentemente, ¿desea continuar?", title = "ADVERTENCIA"):
            query = "DELETE FROM producto WHERE ID_PRODUCTO = ?"
            parametros = id.get()
            run_query(query, (parametros, ))
            messagebox.showinfo("BASE DE DATOS", "Datos eliminados satisfactoriamente")
    except:
        messagebox.showerror("ERROR", "Algo ha salido mal al intentar borrar el registro")
        return
    obt_productos()
    id.configure(state = 'normal')
    clean()
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"

def eliminar_cliente(self):
    try:
        if messagebox.askyesno(message = "El registro se borrara permanentemente, ¿desea continuar?", title = "ADVERTENCIA"):
            query = "DELETE FROM cliente WHERE CI_CLIENTE = ?"
            parametros = ci_cliente.get()
            run_query(query, (parametros, ))
            messagebox.showinfo("BASE DE DATOS", "Datos eliminados satisfactoriamente")
    except:
        messagebox.showerror("ERROR", "Algo ha salido mal al intentar borrar el registro")
        return
    obt_clientes()
    ci_cliente.configure(state = 'normal')
    clean1()
    b_actualizar["state"] = "normal"
    b_eliminar["state"] = "disable"
    b_actualizar["state"] = "disable"

    "Acabo de agregar la funcion para la operacion de mas"
def suma_inventario(self):
    if len(amount.get()) != 0: 
        cant_n = int(amount.get())
        suma = int(cant_v) + cant_n
        query = "UPDATE producto SET CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?"
        parametros = (suma, Id_operacion)
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Se han sumado las cantidades al inventario")
    else:
        messagebox.showerror("BASE DE DATOS", "El campo cantidad no puede estar en blanco")
    id.configure(state = 'normal')
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    clean()
    obt_productos()

"Acabo de agregar la funcion para la operacion de menos"
def resta_inventario(self):
    if len(amount.get()) != 0: 
        cant_n = int(amount.get())
        resta = int(cant_v) - cant_n
        query = "UPDATE producto SET CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?"
        parametros = (resta, Id_operacion)
        run_query(query, parametros)
        messagebox.showinfo("BASE DE DATOS", "Se han restado las cantidades al inventario")
    else:
        messagebox.showerror("BASE DE DATOS", "El campo cantidad no puede estar en blanco")
    id.configure(state = 'normal')
    b1["state"] = "normal"
    b2["state"] = "disable"
    b3["state"] = "disable"
    clean()
    obt_productos()

def dia(self):
    now = datetime.now()
    return now

def seleccionar_click(self, event):
    clean()
    b1["state"] = "disable"
    b2["state"] = "normal"
    b3["state"] = "normal"
    selected = tree.focus()
    values = tree.item(selected, 'values')
    id.insert(0, values[0])
    price_c.insert(0, values[1])
    price_v.insert(0, values[2])
    amount.insert(0, values[3])
    cant_v = values[3]
    Id_operacion = values[0]
    id.configure(state = 'disable')
    Hovertip(id, text = "No puede actualizar el ID de los productos ya ingresados", hover_delay = 100)

def seleccionar1_click(self, event):
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
    Hovertip(ci_cliente, text = "No puede actualizar la cedula de un usuario existente", hover_delay = 100)

    