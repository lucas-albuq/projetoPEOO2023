import json
from datetime import datetime

class Cliente:
    def __init__(self, id: int, nome: str, telefone: str, email: str, cpf: str, data_nascimento: datetime, senha: str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_cpf(cpf)
        self.set_data_nascimento(data_nascimento)
        self.set_senha(senha)

    def __str__(self):
        return f"id - {self.__id}, Nome - {self.__nome}, Telefone - {self.__telefone}, Email - {self.__email}, CPF - {self.__cpf}, Data de Nascimento - {self.__data_nascimento}, Senha - {self.__senha}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "telefone": self.__telefone,
            "email": self.__email,
            "cpf": self.__cpf,
            "data_nascimento": self.__data_nascimento.strftime("%Y-%m-%d"),
            "senha": self.__senha
        }

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_cpf(self):
        return self.__cpf

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_senha(self):
        return self.__senha

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("O ID inserido não é um número inteiro.")

    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) != 0:
            self.__nome = nome
        else:
            raise ValueError("Nome inválido")

    def set_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone.strip()) != 0:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido")

    def set_email(self, email):
        if isinstance(email, str) and len(email.strip()) != 0:
            self.__email = email
        else:
            raise ValueError("Email inválido")

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and len(cpf.strip()) != 0:
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def set_data_nascimento(self, data_nascimento):
        if isinstance(data_nascimento, datetime):
            self.__data_nascimento = data_nascimento
        else:
            raise ValueError("Data de nascimento inválida")

    def set_senha(self, senha):
        if isinstance(senha, str) and len(senha.strip()) != 0:
            self.__senha = senha
        else:
            raise ValueError("Senha inválida")

class NCliente:
    __clientes = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = max(cliente.get_id() for cliente in cls.__clientes) + 1
        obj.set_id(id)
        cls.__clientes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__clientes

    @classmethod
    def listar_id(cls, obj):
        cls.abrir()
        for cliente in cls.__clientes:
            if cliente.get_id() == obj.get_id():
                return cliente
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        cliente = cls.listar_id(obj)
        if cliente is not None:
            cliente.set_nome(obj.get_nome())
            # Adicione outras atualizações conforme necessário
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cliente = cls.listar_id(obj)
        if cliente is not None:
            cls.__clientes.remove(cliente)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__clientes, arquivo, default=Cliente.to_json)

    @classmethod
    def abrir(cls):
        cls.__clientes = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    cliente = Cliente(
                        obj["id"],
                        obj["nome"],
                        obj["telefone"],
                        obj["email"],
                        obj["cpf"],
                        datetime.strptime(obj["data_nascimento"], "%Y-%m-%d"),
                        obj["senha"]
                    )
                    cls.__clientes.append(cliente)
        except FileNotFoundError:
            pass
