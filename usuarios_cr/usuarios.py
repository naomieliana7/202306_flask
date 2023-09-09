import os
from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data)-> None:
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM usuarios"
        resultados = connectToMySQL('esquema_usuarios').query_db(query)
        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"

        # comes back as the new row id
        result = connectToMySQL('esquema_usuarios').query_db(query,data)
        return result
