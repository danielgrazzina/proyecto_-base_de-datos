from tkinter import ttk
from tkinter import *

import sqlite3

class productos:

    def __init__(self, ventana):
        self.wind = ventana
        self.wind.title("primera prueba") 

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = productos(ventana)
    ventana.mainloop()

