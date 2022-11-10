import sqlite3
import os
from constantes import *

def conectar_db():

    os.chdir("C:\\Users\\paixela\\Desktop\\CursoPython\\CursoBackendPython\\SQL\\CineDU\\BasesDeDatos")
    conection = sqlite3.connect(DATABASE_NAME)

    cursor = conection.cursor()
    return conection,cursor

def agregar_pelicula_db(nombre,duracion,actor,critica,estrellas,genero,plataforma):

    conexion, cursor = conectar_db()
    pelicula = (nombre,
                duracion,
                actor,
                critica,
                estrellas,
                genero,
                plataforma)
    sql = f"INSERT INTO peliculas (nombre,duracion,actor,critica,estrellas,genero,plataforma) VALUES {pelicula}"
    conexion.execute(sql)

    conexion.commit()
    conexion.close()

def consultar_peliculasTODO_db():

    conection, cursor = conectar_db()

    sql = "SELECT * FROM peliculas"
    cursor.execute(sql)
    peliculas = cursor.fetchall()
    conection.close()
    return peliculas

def consultar_peliculaID_db(id):
    conection, cursor = conectar_db()

    sql = f"SELECT * FROM peliculas WHERE id={id}"
    cursor.execute(sql)
    pelicula = cursor.fetchone()
    conection.close()
    return pelicula

def borrar_peliculasTODO_db():

    conection, cursor = conectar_db()

    sql = "DELETE FROM peliculas"
    cursor.execute(sql)
    conection.commit()
    conection.close()

def borrar_peliculaID_db(id):

    conection, cursor = conectar_db()

    sql = f"DELETE FROM peliculas WHERE id={id}"
    cursor.execute(sql)
    conection.commit()
    conection.close()














