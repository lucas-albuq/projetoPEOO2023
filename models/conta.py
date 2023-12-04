import json

class Conta:
    def __init__(self, id, idC, saldo, limite, agencia, nConta, tConta):
        self.set_id(id)
        self.set_idCliente(idC)
        self.set_saldo(saldo)
        self.set_limite(limite)
        self.set_agencia(agencia)
        self.set_numeroConta(nConta)
        self.set_tipoConta(tConta)

    def __str__(self):
        return f"id - {self.__id}, id do Cliente - {self.__idCliente}, Saldo - {self.__saldo}, Limite - {self.__limite}, Agência - {self.__agencia}, Número da Conta - {self.__numeroConta},
        Tipo de Conta - {self.__tipoConta}"
    
    def to_json(self):
        return {"id": self.__id,
                "idCliente": self.__idCliente,
                "saldo": self.__saldo,
                "limite": self.__limite,
                "agencia": self.__agencia,
                "numeroConta": self.__numeroConta,
                "tipoConta": self.__tipoConta}
    
    def get_id(self):
        return self.__id
    def get_idCliente(self):
        return self.__idCliente
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def get_agencia(self):
        return self.__agencia
    def get_numeroConta(self):
        return self.__numeroConta
    def get_tipoConta(self):
        return self.__tipoConta
    
    def set_id(self, id):
        if isinstance(id, int): self.__id = id
        else: raise ValueError("O ID inserido não é um número inteiro.")
    def set_idCliente(self, id):
        if isinstance(id, int): self.__idCliente = id
        else: raise ValueError("O ID do Cliente inserido não é um número inteiro.")
    def set_saldo(self, saldo):
        if isinstance(saldo, float): self.__saldo = saldo
        else: raise ValueError("Valor do saldo inválido")
    def set_limite(self, limite):
        if isinstance(limite, float): self.__limite = limite
        else: raise ValueError("Valor do limite inválido")
    def set_agencia(self, agencia):
        if isinstance(agencia, int): self.__agencia = agencia
        else: raise ValueError("Agência inválida")
    def set_numeroConta(self, nConta):
        if len(nConta.split()) != 0: self.__numeroConta = nConta
        else: raise ValueError("Número da conta inválido")
    def set_tipoConta(self, tConta):
        if len(tConta.split()) != 0: self.__tipoConta = tConta
        else: raise ValueError("Tipo da conta inválido")

class NConta:
    __contas = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__contas:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__contas.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__contas
    
    @classmethod
    def listar_id(cls, obj):
        cls.abrir()
        for aux in cls.__contas:
            if aux.get_id() == obj.get_id():
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
            cls.__contas.remove(objeto)
            cls.salvar()


    @classmethod
    def salvar(cls):
        with open("contas.json", mode="w") as arquivo:
            json.dump(cls.__contas, arquivo, default=Conta.to_json)

    @classmethod
    def abrir(cls):
        cls.__agendas = []
        try:
            with open("contas.json", mode="r") as arquivo:
                contas_json = json.load(arquivo)
                for obj in contas_json:
                    aux = Conta(obj["id"], obj["idCliente"], obj["saldo"], obj["limite"], obj["agencia"], obj["numeroConta"], obj["tipoConta"])
                    cls.__contas.append(aux)
        except FileNotFoundError:
            pass