from tkinter import ttk
from tkinter import *

import sqlite3

class productos:

    nombre_BD = 'pruebaBD.db'

    def __init__(self, ventana):
        self.wind = ventana
        self.wind.title("primera prueba")
        self.wind.geometry("400x250")
        self.wind.config(bg= "red")
    
        #----------crear un contenedor frame-----------------   
        frame= LabelFrame(self.wind,text='Registrar nuevo producto')
        frame.grid(row=0,column=0, columnspan=3,pady=20)
        frame.config(bg= "#3498DB")   
        #----------input nombre----------------------
        Label(frame,text='Nombre: ').grid(row=1,column=0)
        self.nombre=Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row= 1, column=1)

        #----------input precio---------------------
        Label(frame,text='Precio: ').grid(row=2,column=0)
        self.precio=Entry(frame)
        self.precio.grid(row= 2, column=1)
        
        #-----------boton añadir productos----------
        ttk.Button(frame, text='Guardar producto').grid(row=3, columnspan =2, sticky= W + E)

        #-----------tabla--------------------------
        self.tree=ttk.Treeview(height= 10, columns =2)
        self.tree.grid(row=4, column=0,columnspan=2)
        self.tree.heading('#0',text='Nombre', anchor = CENTER)
        self.tree.heading('#1',text='Precio', anchor = CENTER)

        self.get_productos()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.nombre_BD)  as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parameters)
            conn.commit()
        return resultado
    
    def get_productos(self):
        query ='SELECT * FROM productos ORDER BY nombre DESC'
        fila_BD= self.run_query(query)
        print(fila_BD)  
        

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = productos(ventana)
    ventana.mainloop()

