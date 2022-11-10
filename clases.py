import tkinter
from tkinter import *
from tkinter import ttk

import funciones

from funciones import *
class Ventana_añadir_pelicula:

    def __init__(self):
        self.añadirpelicula = Tk()
        self.añadirpelicula.title("Introduce la película")
        self.añadirpelicula.geometry("500x300")
        self.añadirpelicula.config(bg="#E0EAEE",)

        self.panel_principal = Frame(self.añadirpelicula,bd=1,relief="flat")
        self.panel_principal.pack()
        """Petición de nombre y valor"""
        self.nombre = tkinter.StringVar()
        self.infoNombre= Label(self.panel_principal,text="Introduce el nombre de la película:")
        self.infoNombre.grid(column=0,row=0)
        self.nombreGrid = ttk.Entry(self.panel_principal,textvariable=self.nombre)
        self.nombreGrid.grid(column=1,row=0)
        """Petición de duración y valor"""
        self.duracion = IntVar()
        self.infoDuracion = Label(self.panel_principal,text="Introduce la duración de la película:")
        self.infoDuracion.grid(column=0,row=1)
        self.duracionGrid = Entry(self.panel_principal,textvariable=self.duracion)
        self.duracionGrid.grid(column=1,row=1)
        """Petición de actor y valor"""
        self.actor = StringVar()
        self.infoActor = Label(self.panel_principal,text="Introduce el actor Principal de la película:")
        self.infoActor.grid(column=0,row=2)
        self.actorGrid = Entry(self.panel_principal,textvariable=self.actor)
        self.actorGrid.grid(column=1,row=2)
        """Petición de crítica y valor"""
        self.critica = StringVar()
        self.infoCritica = Label(self.panel_principal,text="Dinos tu opinión de la película:")
        self.infoCritica.grid(column=0,row=3)
        self.criticaGrid = Entry(self.panel_principal,textvariable=self.critica)
        self.criticaGrid.grid(column=1,row=3)
        """Peticion de Estrellas y valor"""
        self.estrellas = IntVar()
        self.infoEstrellas = Label(self.panel_principal,text="Puntua del 1 al 5 la película:")
        self.infoEstrellas.grid(column=0,row=4)
        self.estrellasGrid = Entry(self.panel_principal,textvariable=self.estrellas)
        self.estrellasGrid.grid(column=1,row=4)
        """Peticion de Genero y valor"""
        self.infoGenero = Label(self.panel_principal,text="Selecciona el Género:")
        self.infoGenero.grid(column=0,row=5)
        self.genero = ttk.Combobox(self.panel_principal,state="readonly",values=["Mafia","Amor"])
        self.genero.grid(column=1,row=5)
        """Peticion de plataforma y valor"""
        self.infoPlataforma = Label(self.panel_principal,text="Selecciona la plataforma:")
        self.infoPlataforma.grid(column=0,row=6)
        self.plataforma = ttk.Combobox(self.panel_principal,state="readonly",values=["Netflix","HBO","Amazon Video"])
        self.plataforma.grid(column=1,row=6)
        """Botón para enviar a Base de datos"""
        self.boton_enviar = Button(self.panel_principal,text="Enviar",command=self.enviar)
        self.boton_enviar.grid(column=3,row=8)

    def enviar(self):
        mensaje = f"Bienvenido {self.nombre.get()}"
        print(mensaje)










