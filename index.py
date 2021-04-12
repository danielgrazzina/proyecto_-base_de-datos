from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sqlite3

class product:
    db_name = 'inventario.db'

    def __init__(self, wn):
        self.xe = 400
        self.ye = 15

        self.wind = wn
        self.wind.title("Aplicacion de Inventario")
        self.wind.resizable(width = 0, height = 0)
        self.wind.geometry("802x450")

        self.l1 = Label(self.wind, text = "Agregue un producto")
        self.l1.place(x = (self.xe - 55), y = self.ye)

        self.lid = Label(self.wind, text = "ID: ")
        self.lid.place(x = 356, y = 40)
        self.id = Entry(self.wind)
        self.id.focus()
        self.id.place(x = self.xe, y = (self.ye + 25))

        self.lprice_c = Label(self.wind, text = "Precio Costo: ")
        self.lprice_c.place(x = 300, y = 70)
        self.price_c = Entry(self.wind)
        self.price_c.place(x = self.xe, y = (self.ye + 55))

        self.lprice_v = Label(self.wind, text = "Precio Venta: ")
        self.lprice_v.place(x = 300, y = 100)
        self.price_v = Entry(self.wind)
        self.price_v.place(x = self.xe, y = (self.ye + 85))

        self.lamount = Label(self.wind, text = "Cantidad: ")
        self.lamount.place(x = 318, y = 130)
        self.amount = Entry(self.wind)
        self.amount.place(x = self.xe, y = (self.ye + 115))

        self.b1 = ttk.Button(self.wind, text = "Guardar producto", command = self.obt_productos())
        self.b1.place(x = (self.xe - 50), y = (self.ye + 145))

        self.tree = ttk.Treeview(height = 10, columns = ('#0', '#1', '#2', '#3'))
        self.tree.place(x = 0, y = 200)
        self.tree.heading('#0', text = 'ID', anchor = CENTER)
        self.tree.heading('#1', text = 'PRECIO COSTO', anchor = CENTER)
        self.tree.heading('#2', text = 'PRECIO VENTA', anchor = CENTER)
        self.tree.heading('#3', text = 'CANTIDAD', anchor = CENTER)

    def run_query(self, query, parametros = ()):
        with sqlite3.connect('inventario.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def conexDB(self):
        self.conn = sqlite3.connect('inventario.db')
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('''
                CREATE TABLE producto(
                    ID_PRODUCTO VARCHAR(15) PRIMARY KEY NOT NULL,
                    TIPO_PRODUCTO VARCHAR(50) NOT NULL,
                    PRECIO_COSTO FLOAT NOT NULL,
                    PRECIO_VENTA FLOAT NOT NUL,
                    CANTIDAD_PRODUCTO INTEGER NOT NULL)
                CREATE TABLE cliente(
                    CI VARCHAR(10) PRIMARY KEY NOT NULL,
                    NOMBRE VARCHAR(25) NOT NULL,
                    APELLIDO VARCHAR(25) NOT NULL,
                    TELEFONO VARCHAR(20) NOT NULL,
                    DIRECCION VARCHAR(100) NOT NULL,
                    DEUDA FLOAT NOT NULL)
                CREATE TABLE pedido(
                    ID_PEDIDO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    CI_CLIENTE VARCHAR(10) NOT NULL,
                    ID_PRODUCTO VARCHAR(15) NOT NULL)
                ''')
            messagebox.showinfo("BASE DE DATOS", "Se creo exitosamente la Base de Datos")
        except:
            messagebox.showinfo("BASE DE DATOS", "Se conecto exitosamente a la Base de Datos")

    def borrarDB(self):
        if messagebox.askyesno(message = "Se borraran todos los datos, ¿Desea continuar?", title = "ADVERTENCIA"):
            query = '''
                DROP TABLE producto,
                DROP TABLE cliente,
                DROP TABLE pedido
                '''
            db_rows = self.run_query(query)
            messagebox.showinfo("BASE DE DATOS", "Se elimino exitosamente la Base de Datos")

    def obt_productos(self):
        view = self.tree.get_children()
        for elementos in view:
            self.tree.delete(elementos)
        
        query = "SELECT * FROM producto ORDER BY ID_PRODUCTO DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("",0,text = row[0], values = (row[2], row[3], row[4]))


    def clean(self):
        self.id.set('')
        self.price_c.set('')
        self.price_v.set('')
        self.amount.set('')

if __name__ == "__main__":
    wn = Tk()
    app = product(wn)
    wn.mainloop()