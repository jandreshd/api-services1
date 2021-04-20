from conexionBD import *

def ping():
    print("pong!")

#agregar frase
def add_quote(body):
    return guardarFrase(body)

#obtener frase aleatoria
def get_random_quote():
    return obtenerFraseAleatoria()

#Para lo sgtes 2 metodos crear en lbd mongodb la estrctura 
#para acumular la cantidad de votos
#Voto me gusta = Sumar un voto
def up_vote(id):
    return actualizarVoto(id, 1)

#Voto me gusta = Restar un voto
def down_vote(id):
    return actualizarVoto(id, -1)

#Eliminar frase
def delete_quote_by_id(id):
    return eliminarFrase(id)
