from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
from idlelib.tooltip import Hovertip
import sqlite3

class product:

    def __init__(self, wn):
        self.xe = 400
        self.ye = 15

        self.wind = wn
        self.wind.title("Aplicacion de Inventario")
        self.wind.resizable(width = 0, height = 0)
        self.wind.geometry("802x500")
        self.wind.iconbitmap('archivo.ico')
        
        self.tree = ttk.Treeview(wn)
        self.tree['columns'] = ("ID", "PRECIO_COSTO", "PRECIO_VENTA", "CANTIDAD")
        self.tree.place(x = 0, y = 200)
        self.tree.bind("<Double-Button-1>", self.seleccionar_click)
        self.tree.column('#0', width = 0, stretch = NO)
        self.tree.column('#1', minwidth = 200, anchor = CENTER)
        self.tree.column('#2', minwidth = 200, anchor = CENTER)
        self.tree.column('#3', minwidth = 200, anchor = CENTER)
        self.tree.column('#4', minwidth = 200, anchor = CENTER)
        self.tree.heading('#1', text = 'ID', anchor = CENTER)
        self.tree.heading('#2', text = 'PRECIO COSTO', anchor = CENTER)
        self.tree.heading('#3', text = 'PRECIO VENTA', anchor = CENTER)
        self.tree.heading('#4', text = 'CANTIDAD', anchor = CENTER)
        self.obt_productos()

        self.l1 = Label(self.wind, text = "Agregue un producto")
        self.l1.place(x = (self.xe - 55), y = self.ye)

        self.lid = Label(self.wind, text = "ID: ")
        self.lid.place(x = 356, y = 40)
        self.id = Entry(self.wind, width = 30)
        self.id.focus()
        self.id.place(x = self.xe, y = (self.ye + 25))

        self.lprice_c = Label(self.wind, text = "Precio Costo: ")
        self.lprice_c.place(x = 300, y = 70)
        self.price_c = Entry(self.wind, width = 30)
        self.price_c.place(x = self.xe, y = (self.ye + 55))

        self.lprice_v = Label(self.wind, text = "Precio Venta: ")
        self.lprice_v.place(x = 300, y = 100)
        self.price_v = Entry(self.wind, width = 30)
        self.price_v.place(x = self.xe, y = (self.ye + 85))

        self.lamount = Label(self.wind, text = "Cantidad: ")
        self.lamount.place(x = 318, y = 130)
        self.amount = Entry(self.wind, width = 30)
        self.amount.place(x = self.xe, y = (self.ye + 115))

        self.b1 = ttk.Button(self.wind, text = "Guardar producto", width = 60, command =  self.agregar_producto)
        self.b1.place(x = (self.xe - 185), y = (self.ye + 145))

        self.b2 = ttk.Button(self.wind, text = "Eliminar Producto", width = 60, command =  self.eliminar_producto)
        self.b2.place(x = (self.xe), y = (self.ye + 435))
        self.b2['state'] = 'disable'

        self.b3 = ttk.Button(self.wind, text = "Actualizar Producto", width = 60, command =  self.editar_producto)
        self.b3.place(x = 30, y = (self.ye + 435))
        self.b3['state'] = 'disable'

        self.img = PhotoImage(file = 'lupa.png')
        self.bsearch = Button(self.wind, width = 35, height = 35, command = self.wind2)
        self.bsearch.config(image = self.img)
        self.bsearch.place(x = 15, y = 15)
        Hovertip(self.bsearch, text = "Buscar", hover_delay = 100)

        self.img1=PhotoImage(file='clientes.png')
        self.bclientes= Button(self.wind,width=35,height=35,command=self.windclientes)
        self.bclientes.config(image=self.img1)
        self.bclientes.place(x=15,y=65)
        Hovertip(self.bclientes, text = "Clientes", hover_delay = 100)

        "Acabo de agregar el boton MAS"
        self.img2 = PhotoImage(file = 'mas.png')
        self.bmas = Button(self.wind, width = 15, height = 15, command = self.suma_inventario)
        self.bmas.config(image = self.img2)
        self.bmas.place(x = 590, y = 130)

        "Acabo de agregar el boton MENOS"
        self.img3 = PhotoImage(file = 'menos.png')
        self.bmenos = Button(self.wind, width = 15, height = 15, command = self.resta_inventario)
        self.bmenos.config(image = self.img3)
        self.bmenos.place(x = 615, y = 130)

        "Acabo de agregar el boton actualizar"
        self.img4 = PhotoImage(file = 'actualizar.png')
        self.bactualizar = Button(self.wind, width = 18, height = 18, command = self.obt_productos)
        self.bactualizar.configure(image = self.img4)
        self.bactualizar.place(x = 590, y = 160)

        "Agrege el boton de pedido"
        self.img5 = PhotoImage(file = 'pedido.png')
        self.bpedido = Button(self.wind, width = 35, height = 35, command = self.windpedido)
        self.bpedido.configure(image = self.img5)
        self.bpedido.place(x = 15, y = 115)
        Hovertip(self.bpedido, text = "PEDIDOS")

        self.menuvar = Menu(self.wind)
        self.menuDB = Menu(self.menuvar, tearoff = 0)
        self.menuDB.add_command(label = "Limpiar Base De Datos 'PRODUCTO'", command = self.borrarDB)
        self.menuvar.add_cascade(label = "Inicio", menu = self.menuDB)

        self.ayudamenu = Menu(self.menuvar, tearoff = 0)
        self.ayudamenu.add_command(label = "Resetear Campos", command = self.clean)
        self.ayudamenu.add_command(label = "Manual de Usuario")# command = self.manual_usuario)
        self.menuvar.add_cascade(label = "Ayuda", menu = self.ayudamenu)

        self.wind.config(menu = self.menuvar)

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
                self.run_query(query)
                self.obt_productos()
                self.clean()
                messagebox.showinfo("BASE DE DATOS", "Se vacio exitosamente la tabla 'PRODUCTO'")
        except:
            messagebox.showerror("ERROR", "No se pudo vaciar la tabla 'PRODUCTO'")

    def wind2(self):
        self.wind.iconify()
        self.wind2 = Toplevel()
        self.wind2.resizable(width = 0, height = 0)
        self.wind2.geometry("400x200+400+400")
        self.wind2.iconbitmap('archivo.ico')
        self.lbuscar = Label(self.wind2, text = "Selecciones lo que desea buscar")
        self.lbuscar.place(x = 10, y = 10)
        self.ebuscar = Entry(self.wind2, width = 30)
        self.ebuscar.place(x = 150, y = 65)
        self.bbuscar = ttk.Button(self.wind2, text = "Buscar", width = 29, command = self.buscar)
        self.bbuscar.place(x = 150, y = 100)
        self.linstruccion = Label(self.wind2, text = "")
        self.linstruccion.place(x = 120, y = 135)
        self.v = IntVar()
        self.rb_producto = Radiobutton(self.wind2, text = "PRODUCTO", value = 1, variable = self.v, command = self.prueba)
        self.rb_producto.place(x = 20, y = 50)
        self.rb_cliente = Radiobutton(self.wind2, text = "CLIENTE", value = 2, variable = self.v, command = self.prueba)
        self.rb_cliente.place(x = 20, y = 80)
        self.rb_pedido = Radiobutton(self.wind2, text = "PEDIDO", value = 3, variable = self.v, command = self.prueba)
        self.rb_pedido.place(x = 20, y = 110)
        
    def windclientes (self):
        #self.wind.iconify() 
        self.windclientes = Toplevel()
        self.windclientes.resizable(width=0,height=0)
        self.windclientes.geometry("900x550+200+50")
        self.windclientes.iconbitmap('archivo.ico')
        self.windclientes.title("Clientes")

        self.tree = ttk.Treeview(self.windclientes)
        self.tree['columns'] = ("CI_CLIENTE", "NONMBRE", "APELLIDO ", "TELEFONO","DIRECCION", "DEUDA")
        self.tree.place(x = 0, y = 270)
        self.tree.bind("<Double-Button-1>", self.seleccionar1_click)
        self.tree.column('#0', width = 0, stretch = NO)
        self.tree.column('#1', minwidth = 150, width=150,  anchor = CENTER)
        self.tree.column('#2', minwidth = 150, width=150, anchor = CENTER)
        self.tree.column('#3', minwidth = 150, width=150, anchor = CENTER)
        self.tree.column('#4', minwidth = 150, width=150, anchor = CENTER)
        self.tree.column('#5', minwidth = 150, width=150, anchor = CENTER)
        self.tree.column('#6', minwidth = 150, width=150, anchor = CENTER)
        self.tree.heading('#1', text = 'CI_CLIENTE', anchor = CENTER)
        self.tree.heading('#2', text = 'NOMBRE', anchor = CENTER)
        self.tree.heading('#3', text = 'APELLIDO', anchor = CENTER)
        self.tree.heading('#4', text = 'TELEFONO', anchor = CENTER)
        self.tree.heading('#5', text = 'DIRECCION', anchor = CENTER)
        self.tree.heading('#6', text = 'DEUDA', anchor = CENTER)
        self.obt_productos1()

        self.l_title = Label(self.windclientes, text = "Agregue un cliente")
        self.l_title.place(x = (self.xe), y = self.ye)

        self.l_ci_cedula = Label(self.windclientes, text = "Cedula: ")
        self.l_ci_cedula.place(x = 376, y = 40)
        self.ci_cedula = Entry(self.windclientes, width = 30)
        self.ci_cedula.focus()
        self.ci_cedula.place(x = (self.xe + 60), y = (self.ye + 25))

        self.l_nombre = Label(self.windclientes, text = "nombre: ")
        self.l_nombre.place(x = 370, y = 70)
        self.nombre = Entry(self.windclientes, width = 30)
        self.nombre.place(x = (self.xe + 60), y = (self.ye + 55))

        self.l_apellido = Label(self.windclientes, text = "apellido: ")
        self.l_apellido.place(x = 370, y = 100)
        self.apellido = Entry(self.windclientes, width = 30)
        self.apellido.place(x = (self.xe + 60), y = (self.ye + 85))

        self.l_telefono = Label(self.windclientes, text = "telefono: ")
        self.l_telefono.place(x = 370, y = 130)
        self.telefono = Entry(self.windclientes, width = 30)
        self.telefono.place(x = (self.xe + 60), y = (self.ye + 115))

        self.l_direccion = Label(self.windclientes, text = "direccion: ")
        self.l_direccion.place(x = 366, y = 160)
        self.direccion = Entry(self.windclientes, width = 30)
        self.direccion.place(x = (self.xe + 60), y = (self.ye + 145))

        self.l_deuda = Label(self.windclientes, text = "deuda: ")
        self.l_deuda.place(x = 382, y = 190)
        self.deuda = Entry(self.windclientes, width = 30)
        self.deuda.place(x = (self.xe + 60), y = (self.ye + 175))

        self.b_guardar = ttk.Button(self.windclientes, text = "Guardar cliente", width = 70, command =  self.agregar_cliente)
        self.b_guardar.place(x = (self.xe - 170), y = (self.ye + 210))

        self.b_eliminar = ttk.Button(self.windclientes, text = "Eliminar cliente", width = 70, command =  self.eliminar_cliente)
        self.b_eliminar.place(x = (self.xe + 35), y = (self.ye + 500))
        self.b_eliminar['state'] = 'disable'

        self.b_actualizar = ttk.Button(self.windclientes, text = "Actualizar cliente", width = 70, command =  self.editar_cliente)
        self.b_actualizar.place(x = 30, y = (self.ye + 500))
        self.b_actualizar['state'] = 'disable'


    def prueba(self):
        if self.v.get() == 1:
            self.lbuscar['text'] = "Ha seleccionado la opcion PRODUCTO"
            self.linstruccion['text'] = "Ingrese el ID del PRODUCTO que desea buscar"
        elif self.v.get() == 2:
            self.lbuscar['text'] = "Ha seleccionado la opcion CLIENTE"
            self.linstruccion['text'] = "Ingrese la CI del CLIENTE que desea buscar"
        elif self.v.get() == 3:
            self.lbuscar['text'] = "Ha seleccionado la opcion PEDIDO"
            self.linstruccion['text'] = "Ingrese el ID del PEDIDO que desea buscar"

    def buscar(self):
        if len(self.ebuscar.get()) != 0 and self.v.get() != 0:
            if self.v.get() == 1:
                query = "SELECT * FROM producto WHERE ID_PRODUCTO = ? ORDER BY ID_PRODUCTO DESC"
                parametros = (self.ebuscar.get())
            elif self.v.get() == 2:
                query = "SELECT * FROM cliente WHERE CI_CLIENTE = ? ORDER BY NOMBRE DESC"
                parametros = (self.ebuscar.get())
            elif self.v.get() == 3:
                query = "SELECT * FROM pedido WHERE ID_PEDIDO = ? ORDER BY ID_PEDIDO DESC"
                parametros = (self.ebuscar.get())
            
            view = self.tree.get_children()
            
            for elementos in view:
                self.tree.delete(elementos)
            
            db_rows = self.run_query(query, (parametros, ))

            for row in db_rows:
                self.tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))
            
            self.wind.deiconify()
            self.wind2.destroy()
        else:
            messagebox.showwarning("ADVERTENCIA", "Debe elegir una opcion, y rellenar el campo con lo que seas buscar")

    def clean(self):
        self.id.delete(0, END)
        self.price_c.delete(0, END)
        self.price_v.delete(0, END)
        self.amount.delete(0, END)

    def clean1(self):
        self.ci_cliente.delete(0, END)
        self.nombre.delete(0, END)
        self.apellido.delete(0, END)
        self.telefono.delete(0, END)
        self.direccion.delete(0, END)
        self.direccion.delete(0, END)

    def obt_productos(self):
        view = self.tree.get_children()
        for elementos in view:
            self.tree.delete(elementos)
            
        query = "SELECT * FROM producto ORDER BY ID_PRODUCTO DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))
    
    def obt_productos1(self):
        view = self.tree.get_children()
        for elementos in view:
            self.tree.delete(elementos)
            
        query = "SELECT * FROM cliente ORDER BY CI_CLIENTE DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]), row[4], row[5]))

    def validacion(self):
        return len(self.id.get()) != 0 and len(self.price_c.get()) != 0 and len(self.price_v.get()) != 0 and len(self.amount.get()) != 0

    def validacion1(self):
        return len(self.ci_cedula.get()) != 0 and len(self.nombre.get()) != 0 and len(self.apellido.get()) != 0 and len(self.telefono.get()) != 0 and len(self.direccion.get()) != 0 and len(self.deuda.get()) != 0

    def agregar_producto(self):
        if self.validacion():
            query = "INSERT INTO producto VALUES(?, ?, ?, ?)"
            parametros = (self.id.get(), self.price_c.get(), self.price_v.get(), self.amount.get())
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Datos guardados satisfactoriamente")
        else:
            messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
        self.obt_productos()
        self.clean()

        def agregar_cliente(self):
        if self.validacion1():
            query = "INSERT INTO cliente VALUES(?, ?, ?, ?, ?, ?)"
            parametros = (self.ci_cedula.get(), self.nombre.get(), self.apellido.get(), self.telefono.get(), self.direccion.get(), self.deuda.get())
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Datos guardados satisfactoriamente")
        else:
            messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
        self.obt_productos1()
        self.clean1()

    def editar_producto(self):
        if self.validacion():
            parametros = (self.price_c.get(), self.price_v.get(), self.amount.get(), self.id.get())
            query = ("UPDATE producto SET PRECIO_COSTO = ? , PRECIO_VENTA = ?, CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?")
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Datos actualizados satisfactoriamente")
        else:
            messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
        self.obt_productos()
        self.id.configure(state = 'normal')
        self.clean()
        self.b1["state"] = "normal"
        self.b2["state"] = "disable"
        self.b3["state"] = "disable"

    def eliminar_producto(self):
        try:
            if messagebox.askyesno(message = "El registro se borrara permanentemente, ¿desea continuar?", title = "ADVERTENCIA"):
                query = "DELETE FROM producto WHERE ID_PRODUCTO = ?"
                parametros = self.id.get()
                self.run_query(query, (parametros, ))
                messagebox.showinfo("BASE DE DATOS", "Datos eliminados satisfactoriamente")
        except:
            messagebox.showerror("ERROR", "Algo ha salido mal al intentar borrar el registro")
            return
        self.obt_productos()
        self.id.configure(state = 'normal')
        self.clean()
        self.b1["state"] = "normal"
        self.b2["state"] = "disable"
        self.b3["state"] = "disable"

        "Acabo de agregar la funcion para la operacion de mas"
    def suma_inventario(self):
        if len(self.amount.get()) != 0: 
            cant_n = int(self.amount.get())
            self.suma = int(self.cant_v) + cant_n
            query = "UPDATE producto SET CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?"
            parametros = (self.suma, self.Id_operacion)
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Se han sumado las cantidades al inventario")
        else:
            messagebox.showerror("BASE DE DATOS", "El campo cantidad no puede estar en blanco")
        self.id.configure(state = 'normal')
        self.b1["state"] = "normal"
        self.b2["state"] = "disable"
        self.b3["state"] = "disable"
        self.clean()
        self.obt_productos()

    "Acabo de agregar la funcion para la operacion de menos"
    def resta_inventario(self):
        if len(self.amount.get()) != 0: 
            cant_n = int(self.amount.get())
            self.resta = int(self.cant_v) - cant_n
            query = "UPDATE producto SET CANTIDAD_PRODUCTO = ? WHERE ID_PRODUCTO = ?"
            parametros = (self.resta, self.Id_operacion)
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Se han restado las cantidades al inventario")
        else:
            messagebox.showerror("BASE DE DATOS", "El campo cantidad no puede estar en blanco")
        self.id.configure(state = 'normal')
        self.b1["state"] = "normal"
        self.b2["state"] = "disable"
        self.b3["state"] = "disable"
        self.clean()
        self.obt_productos()

    def seleccionar_click(self, event):
        self.clean()
        self.b1["state"] = "disable"
        self.b2["state"] = "normal"
        self.b3["state"] = "normal"
        self.selected = self.tree.focus()
        self.values = self.tree.item(self.selected, 'values')
        self.id.insert(0, self.values[0])
        self.price_c.insert(0, self.values[1])
        self.price_v.insert(0, self.values[2])
        self.amount.insert(0, self.values[3])
        self.cant_v = self.values[3]
        self.Id_operacion = self.values[0]
        self.id.configure(state = 'disable')
        Hovertip(self.id, text = "No puede actualizar el ID de los productos ya ingresados", hover_delay = 100)

    def seleccionar1_click(self, event):
        self.clean1()
        self.b_guardar["state"] = "disable"
        self.b_actualizar["state"] = "normal"
        self.b_eliminar["state"] = "normal"
        self.selected = self.tree.focus()
        self.values = self.tree.item(self.selected, 'values')
        self.ci_cliente.insert(0, self.values[0])
        self.nombre.insert(0, self.values[1])
        self.apellido.insert(0, self.values[2])
        self.telefono.insert(0, self.values[3])
        self.direccion.insert(0, self.values[4])
        self.deuda.insert(0, self.values[5])
        self.ci_cliente.configure(state = 'disable')
        Hovertip(self.ci_cliente, text = "No puede actualizar la cedula de un usuario existente", hover_delay = 100)

if __name__ == "__main__":
    wn = Tk()
    app = product(wn)
    wn.mainloop()