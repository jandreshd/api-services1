import pymongo
import random
from pymongo import errors as mongoerrors

clientMongo = pymongo.MongoClient("mongodb+srv://jandreshd:ValeIsa2405@clspython.klugh.mongodb.net/db2?retryWrites=true&w=majority")
db = clientMongo.db2

def consultarCollecionesBD():
    for i in db.list_collection_names():
        print (i)

def guardarFrase(body):
    try:
        nroFrase = db.misFrases.count_documents({})   
        datosFrase = db.misFrases.find_one({'frase': body["frase"]})
        if datosFrase is None:
            documentoJSON = {'id': nroFrase + 1, 'frase': body["frase"], 'votos': 0}
            db.misFrases.insert_one(documentoJSON)
            return "Frase Agregada"
        else:
            return "Frase ya existe", 404
    except:
        return "Error insertando registro en la BD", 404

def obtenerFraseAleatoria():
    try:
        totalFrases = db.misFrases.count_documents({})   
        query = {'id': random.randint(1, totalFrases)}
        datosFrase = db.misFrases.find_one(query)
        return datosFrase
    except:
        return "Error consultando la frase del dia", 404

def actualizarVoto(id, cantidad):
    try:
        query = {'id': id}
        datosFrase = db.misFrases.find_one(query)
        if datosFrase is None:
            return "Frase No Encontrada", 404
        else:
            datosFrase["votos"] += cantidad
            if datosFrase["votos"] > 0 :
                votos = { "$set": { "votos": datosFrase["votos"] } }
            else:
                votos = { "$set": { "votos": 0} }
            db.misFrases.update_one(query, votos)
            return "Actualizacion Frase Exitosa"
    except:
        return  "Error actualizando registro en la BD", 404

def eliminarFrase(id):
    try:
        query = {'id': id}
        datosFrase = db.misFrases.find_one(query)
        if datosFrase is None:
            return "Frase No Encontrada", 404
        else:
            db.misFrases.delete_one(query)
            return "Frase Eliminada"
    except:
        return "Error eliminando registro en la BD", 404