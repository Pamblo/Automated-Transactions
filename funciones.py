

import sql
def consultar_peliculasTODO():

    peliculas = sql.consultar_peliculasTODO_db()
    for pelicula in peliculas:
        print(pelicula)

def consultar_peliculaID(id):

    pelicula = sql.consultar_peliculaID_db(id)
    print(pelicula)

def añadir_pelicula(nombre,duracion,actor,critica,estrellas,genero,plataforma):

    sql.agregar_pelicula_db(nombre,duracion,actor,critica,estrellas,genero,plataforma)



















