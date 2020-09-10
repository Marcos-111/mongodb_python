#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.persons.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.

    insert_one('Muriel', 12, 1, 'Castro')
    insert_one('Shoshana', 16, 5, 'Sonia')
    insert_one('Joan', 17, 6, 'Sonia')
    insert_one('Anne', 13, 2, 'Julio')
    insert_one('Dimitri', 12, 1, 'Castro' )

def insert_one(name, age, grade, tutor):
    
    conn = TinyMongoClient()
    db = conn[db_name]

    persona_json = {"name": name, "age": age, "grade": grade, "tutor": tutor}
    db.persons.insert_one(persona_json)


    conn.close()


def show():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la ssentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"


    # Conectarse a la base de datos
    conn = TinyMongoClient()
    db = conn[db_name]

    
    cursor = db.persons.find()
    data = list(cursor)
    json_string = json.dumps(data, indent=4)
    print(json_string)


def find_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    
    # Conectarse a la base de datos
    conn = TinyMongoClient()
    db = conn[db_name]

    # Leer todos los documentos y obtener los datos de a uno
    person_grade = db.persons.find({"grade": grade})
    
    for doc in person_grade:
        #print((person_grade['_id'], person_grade['name'], person_grade['age']))
        print('id:', doc['_id'], 'name:', doc['name'],'age:', doc['age'])
        
    
    
    
    conn.close()
    



def insert(student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db

    conn = TinyMongoClient()
    db = conn[db_name]

    persona_json = student
    db.persons.insert_one(persona_json)


    conn.close()


def count(c_grade):
    print('Contar estudiantes')
    

    conn = TinyMongoClient()
    db = conn[db_name]

    
    count = db.persons.find({"grade": c_grade}).count()
    print(count)
    
    conn.close()
    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill()
    show()

    student = {"name": "Celio", "age": 13, "grade": 2, "tutor": "Morty"}
    insert(student)
    student = {"name": "Carmelo", "age": 15, "grade": 4, "tutor": "Catalina"}
    insert(student)
    show()

    
    find_by_grade(1)

    
    count(1)
