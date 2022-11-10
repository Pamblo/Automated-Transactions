import sql
from tkinter import *
from tkinter import ttk

def consultar_peliculasTODO():

    peliculas = sql.consultar_peliculasTODO_db()
    for pelicula in peliculas:
        print(pelicula)

def consultar_peliculaID(id):

    pelicula = sql.consultar_peliculaID_db(id)
    print(pelicula)

def añadir_pelicula():

    añadirpelicula = Tk()
    añadirpelicula.title("Introduce la película")
    añadirpelicula.geometry("500x300")
    añadirpelicula.config(bg="#E0EAEE",)

    panel_principal = Frame(añadirpelicula,bd=1,relief="flat")
    panel_principal.pack()
    """Petición de nombre y valor"""
    infoNombre= Label(panel_principal,text="Introduce el nombre de la película:")
    infoNombre.grid(column=0,row=0)
    nombre = Entry(panel_principal)
    nombre.grid(column=1,row=0)
    """Petición de duración y valor"""
    infoDuracion = Label(panel_principal,text="Introduce la duración de la película:")
    infoDuracion.grid(column=0,row=1)
    duracion = Entry(panel_principal)
    duracion.grid(column=1,row=1)
    """Petición de actor y valor"""
    infoActor = Label(panel_principal,text="Introduce el actor Principal de la película:")
    infoActor.grid(column=0,row=2)
    actor = Entry(panel_principal)
    actor.grid(column=1,row=2)
    """Petición de crítica y valor"""
    infoCritica = Label(panel_principal,text="Dinos tu opinión de la película:")
    infoCritica.grid(column=0,row=3)
    critica = Entry(panel_principal)
    critica.grid(column=1,row=3)
    """Peticion de Estrellas y valor"""
    infoEstrellas = Label(panel_principal,text="Puntua del 1 al 5 la película:")
    infoEstrellas.grid(column=0,row=4)
    Estrellas = Entry(panel_principal)
    Estrellas.grid(column=1,row=4)
    """Peticion de Genero y valor"""
    infoGenero = Label(panel_principal,text="Selecciona el Género:")
    infoGenero.grid(column=0,row=5)
    genero = ttk.Combobox(panel_principal,state="readonly",values=["Mafia","Amor"])
    genero.grid(column=1,row=5)
    """Peticion de plataforma y valor"""
    infoPlataforma = Label(panel_principal,text="Selecciona la plataforma:")
    infoPlataforma.grid(column=0,row=6)
    plataforma = ttk.Combobox(panel_principal,state="readonly",values=["Netflix","HBO","Amazon Video"])
    plataforma.grid(column=1,row=6)







