import json

class Banco:
    def __init__(self, id, n):
        self.__id = id
        self.__nome = n

    def __str__(self):
        return f"Banco {self.__id} - {self.__nome}"
    
    def __eq__(self, obj):
        if self.__id == obj.__id and self.__nome == obj.__nome: return True
        return False
    
    def to_json(self):
        return {
            'id': self.__id,
            'nome': self.__nome
        }

    def get_id(self):
        return self.__id
    def set_id(self, id):
        if isinstance(id, int): self.__id = id
        else: raise ValueError("O id apresentado não é um número inteiro")
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        if len(nome.split()) != 0: self.__nome = nome
        else: raise ValueError("Insira um nome válido.")