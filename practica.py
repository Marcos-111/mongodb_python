#!/usr/bin/env python

import requests
import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'practica'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    db.persons.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    insert_grupo(data)


def insert_grupo(group):
    conn = TinyMongoClient()
    db = conn[db_name]

    # Insertar varios documentos, una lista de JSON
    db.persons.insert_many(group)

    # Cerrar la conexión con la base de datos
    conn.close()

def title_completed_count(userId, completed):
    # Conectarse a la base de datos
    conn = TinyMongoClient()
    db = conn[db_name]

    # Contar cuantos docuemtnos poseen el campo de nacionalidad indicado
    users_id = db.persons.find({"userId": userId, "completed": completed}).count()
    #count_completed = users_id.persons.find({"completed": true}).count()

    # Cerrar la conexión con la base de datos
    conn.close()
    return users_id













if __name__ == "__main__":
  # Borrar DB
  clear()

  # Completar la DB con el JSON request
  fill()

  completed = True
  userId = 5
  print(title_completed_count(userId, completed))