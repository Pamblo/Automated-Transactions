import tkinter

import graficos
from sql import *
from funciones import *
from tkinter import *
from tkinter import ttk



"""CONFIGURACIÓN DE LA VENTANA TKINTER"""
cineDU = Tk()
cineDU.title("CINEDU")
cineDU.geometry("1080x800")
cineDU.config(bg="#E0EAEE")

"""CREAMOS PANEL SUPERIOR CON TITULO Y DESCRIPCIÓN DEL PROGRAMA"""

panelsuperior = Frame(cineDU,border=5,relief="groove")
panelsuperior.pack(side=TOP)

tituloSuperior = Label(panelsuperior,text="CINEDU",bg="#F3C3B8",font=("Arial",25),width=60)
tituloSuperior.grid(column=0,row=0)

mensajeBienvenida = Label(panelsuperior,text=f"{mensaje_app_titulo}",font=("Arial",15))
mensajeBienvenida.grid(column=0,row=1)

"""MENU DE BOTONES PARA FUNCIONES DE LA WEB"""

panelCentral = Frame(cineDU,border=5,relief="flat")
panelCentral.pack(side=TOP)

botonPeliculasVistas = Button(panelCentral,text="¡Consulta tus películas Vistas!",command=consultar_peliculasTODO)
botonPeliculasVistas.grid(column=0,row=0)





cineDU.mainloop()
