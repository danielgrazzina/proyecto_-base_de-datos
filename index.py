from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
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
        self.wind2 = Toplevel()
        self.wind2.resizable(width = 0, height = 0)
        self.wind2.geometry("400x200+400+400")
        self.wind2.iconbitmap('archivo.ico')
        self.lbuscar = Label(self.wind2, text = "Selecciones lo que desea buscar")
        self.lbuscar.place(x = 10, y = 10)
        self.ebuscar = Entry(self.wind2, width = 30)
        self.ebuscar.place(x = 150, y = 65)
        self.bbuscar = ttk.Button(self.wind2, text = "Buscar", width = 29)
        self.bbuscar.place(x = 150, y = 100)
        self.v = IntVar()
        self.rb_producto = Radiobutton(self.wind2, text = "PRODUCTO", value = 1, variable = self.v, command = self.prueba)
        self.rb_producto.place(x = 20, y = 50)
        self.rb_cliente = Radiobutton(self.wind2, text = "CLIENTE", value = 2, variable = self.v, command = self.prueba)
        self.rb_cliente.place(x = 20, y = 80)
        self.rb_pedido = Radiobutton(self.wind2, text = "PEDIDO", value = 3, variable = self.v, command = self.prueba)
        self.rb_pedido.place(x = 20, y = 110)
    
    def prueba(self):

        self.lbuscar = Label(self.wind2, text = "Selecciones lo que desea buscar")
        self.lbuscar.place(x = 10, y = 10)



    def clean(self):
        self.id.delete(0, END)
        self.price_c.delete(0, END)
        self.price_v.delete(0, END)
        self.amount.delete(0, END)

    def obt_productos(self):
        view = self.tree.get_children()
        for elementos in view:
            self.tree.delete(elementos)
            
        query = "SELECT * FROM producto ORDER BY ID_PRODUCTO DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("", 0, text = "", values = (row[0], row[1], row[2], row[3]))

    def validacion(self):
        return len(self.id.get()) != 0 and len(self.price_c.get()) != 0 and len(self.price_v.get()) != 0 and len(self.amount.get()) != 0

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

    def editar_producto(self):
        if self.validacion():
            query = '''UPDATE producto SET ID_PRODUCTO = ?, PRECIO_COSTO = ?, PRECIO_VENTA = ?, CANTIDAD_PRODUCTO = ?'''
            parametros = (self.id.get(), self.price_c.get(), self.price_v.get(), self.amount.get())
            self.run_query(query, parametros)
            messagebox.showinfo("BASE DE DATOS", "Datos actualizados satisfactoriamente")
        else:
            messagebox.showerror("ADVERTENCIA", "No pueden haber campos en blanco")
        self.obt_productos()
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
        self.clean()
        self.b1["state"] = "normal"
        self.b2["state"] = "disable"
        self.b3["state"] = "disable"


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

if __name__ == "__main__":
    wn = Tk()
    app = product(wn)
    wn.mainloop()
