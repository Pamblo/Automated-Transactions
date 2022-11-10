import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import ttk

import clases
from constantes import *
from funciones import *

class Aplicacion():
    def __init__(self):
        """CONFIGURACIÓN DE LA VENTANA TKINTER"""
        self.cineDU = Tk()
        self.cineDU.title("CINEDU")
        self.cineDU.geometry("1080x800")
        self.cineDU.config(bg="#E0EAEE")
        self.cineDU.resizable(width= False,height=False)

        """CREAMOS PANEL SUPERIOR CON TITULO Y DESCRIPCIÓN DEL PROGRAMA"""

        self.panelsuperior = Frame(self.cineDU, border=5, relief="groove")
        self.panelsuperior.pack(side=TOP)

        self.tituloSuperior = Label(self.panelsuperior, text="CINEDU", bg="#F3C3B8", font=("Arial", 25), width=60)
        self.tituloSuperior.grid(column=0, row=0)

        self.mensajeBienvenida = Label(self.panelsuperior, text=f"{mensaje_app_titulo}", font=("Arial", 15))
        self.mensajeBienvenida.grid(column=0, row=1)

        """MENU DE BOTONES PARA FUNCIONES DE LA WEB"""

        self.panelCentral = Frame(self.cineDU, border=5, relief="flat")
        self.panelCentral.pack(side=TOP)

        self.botonPeliculasVistas = Button(self.panelCentral, text="¡Consulta tus películas Vistas!",
                                  command=consultar_peliculasTODO)
        self.botonPeliculasVistas.grid(column=0, row=0)

        self.añadirPelicula = Button(self.panelCentral, text="¡Añade una nueva película!", command=clases.Ventana_añadir_pelicula)
        self.añadirPelicula.grid(column=0, row=1)

        self.cineDU.mainloop()
class Ventana_añadir_pelicula:

    def __init__(self):

        self.añadirpelicula = Tk()
        self.añadirpelicula.title("Introduce la película")
        self.añadirpelicula.geometry("500x300")
        self.añadirpelicula.config(bg="#E0EAEE",)

        self.panel_principal = Frame(self.añadirpelicula,bd=1,relief="flat")
        self.panel_principal.pack()
        """Petición de nombre y valor"""

        self.infoNombre= Label(self.panel_principal,text="Introduce el nombre de la película:")
        self.infoNombre.grid(column=0,row=0)
        self.txt_nombre = tkinter.Entry(self.panel_principal)
        self.txt_nombre.grid(column=1,row=0)

        """Petición de duración y valor"""

        self.infoDuracion = Label(self.panel_principal,text="Introduce la duración de la película:")
        self.infoDuracion.grid(column=0,row=1)
        self.txt_duracion = Entry(self.panel_principal)
        self.txt_duracion.grid(column=1,row=1)
        
        """Petición de actor y valor"""

        self.infoActor = Label(self.panel_principal,text="Introduce el actor Principal de la película:")
        self.infoActor.grid(column=0,row=2)
        self.txt_actor = Entry(self.panel_principal)
        self.txt_actor.grid(column=1,row=2)
        """Petición de crítica y valor"""

        self.infoCritica = Label(self.panel_principal,text="Dinos tu opinión de la película:")
        self.infoCritica.grid(column=0,row=3)
        self.txt_critica = Entry(self.panel_principal)
        self.txt_critica.grid(column=1,row=3)
        """Peticion de Estrellas y valor"""

        self.infoEstrellas = Label(self.panel_principal,text="Puntua del 1 al 5 la película:")
        self.infoEstrellas.grid(column=0,row=4)
        self.txt_estrellas = Entry(self.panel_principal)
        self.txt_estrellas.grid(column=1,row=4)
        """Peticion de Genero y valor"""
        self.infoGenero = Label(self.panel_principal,text="Selecciona el Género:")
        self.infoGenero.grid(column=0,row=5)
        self.txt_genero = ttk.Combobox(self.panel_principal,state="readonly",values=["Mafia","Amor"])
        self.txt_genero.grid(column=1,row=5)
        """Peticion de plataforma y valor"""
        self.infoPlataforma = Label(self.panel_principal,text="Selecciona la plataforma:")
        self.infoPlataforma.grid(column=0,row=6)
        self.txt_plataforma = ttk.Combobox(self.panel_principal,state="readonly",values=["Netflix","HBO","Amazon Video"])
        self.txt_plataforma.grid(column=1,row=6)
        """Botón para enviar a Base de datos"""
        self.boton_enviar = Button(self.panel_principal,text="Enviar",command=self.enviar)
        self.boton_enviar.grid(column=3,row=8)
    def enviar(self):

        nombre = self.txt_nombre.get()
        duracion = self.txt_duracion.get()
        estrellas = self.txt_estrellas.get()
        actor = self.txt_actor.get()
        critica = self.txt_critica.get()
        genero = self.txt_genero.get()
        plataforma = self.txt_plataforma.get()

        añadir_pelicula(nombre,duracion,actor,critica,estrellas,genero,plataforma)


        self.añadirpelicula.destroy()

