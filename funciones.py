import sql

def consultar_peliculasTODO():

    peliculas = sql.consultar_peliculasTODO_db()
    for pelicula in peliculas:
        print(pelicula)

def consultar_peliculaID(id):

    pelicula = sql.consultar_peliculaID_db(id)
    print(pelicula)

