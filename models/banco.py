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

class NBanco:
    __bancos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__bancos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__bancos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__bancos
    
    @classmethod
    def listar_id(cls, obj):
        cls.abrir()
        for aux in cls.__bancos:
            if aux.get_id() == obj.get_id:
                return aux
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj)
        if aux is not None:
            aux.set_nome(obj.get_nome())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        objeto = cls.listar_id(obj)
        if objeto is not None:
            cls.__bancos.remove(objeto)
            cls.salvar()


    @classmethod
    def salvar(cls):
        with open("bancos.json", mode="w") as arquivo:
            json.dump(cls.__bancos, arquivo, default=Banco.to_json)

    @classmethod
    def abrir(cls):
        cls.__agendas = []
        try:
            with open("bancos.json", mode="r") as arquivo:
                bancos_json = json.load(arquivo)
                for obj in bancos_json:
                    aux = Banco(obj['id'], obj['nome'])
                    cls.__bancos.append(aux)
        except FileNotFoundError:
            pass