import json
from datetime import datetime

class Transferencia:
    def __init__(self, id, id_conta, id_conta_do_recebedor, data_transferencia, valor, confirmado):
        self.set_id(id)
        self.set_id_conta(id_conta)
        self.set_id_conta_do_recebedor(id_conta_do_recebedor)
        self.set_data_transferencia(data_transferencia)
        self.set_valor(valor)
        self.set_confirmado(confirmado)

    def __str__(self):
        return f"id - {self.__id}, id da Conta - {self.__id_conta}, id da Conta do Recebedor - {self.__id_conta_do_recebedor}, Valor - {self.__valor}, Confirmado - {self.__confirmado}"
    
    def to_json(self):
        return {"id": self.__id,
                "id_conta": self.__id_conta,
                "id_conta_do_recebedor": self.__id_conta_do_recebedor,
                "data_transferencia":  self.__data_transferencia.strftime("%d-%m-%Y %H:%M"),
                "valor": self.__valor,
                "confirmado": self.__confirmado}
    
    def get_id(self):
        return self.__id
    
    def get_id_conta(self):
        return self.__id_conta
    
    def get_id_conta_do_recebedor(self):
        return self.__id_conta_do_recebedor
    
    def get_data_transferencia(self):
        return self.__data_transferencia
    
    def get_valor(self):
        return self.__valor
    
    def get_confirmado(self):
        return self.__confirmado
    
    def set_id(self, id):
        if isinstance(id, int): 
            self.__id = id
        else: 
            raise ValueError("O id informado não é um número inteiro")

    def set_id_conta(self, id_conta):
        if isinstance(id_conta, int): 
            self.__id_conta = id_conta
        else: 
            raise ValueError("O id da conta informado não é um número inteiro")

    def set_id_conta_do_recebedor(self, id_conta_do_recebedor):
        if isinstance(id_conta_do_recebedor, int): 
            self.__id_conta_do_recebedor = id_conta_do_recebedor
        else: 
            raise ValueError("O id da conta do recebedor informado não é um número inteiro")
        
    def set_data_transferencia(self, data_transferencia):
        if isinstance(data_transferencia, datetime):
            self.__data_transferencia = data_transferencia
        else:
            raise ValueError("Data da transferência inválida.")

    def set_valor(self, valor):
        if isinstance(valor, float) and valor > 0: 
            self.__valor = valor
        else: 
            raise ValueError("O valor informado é inválido")

    def set_confirmado(self, confirmado):
        if isinstance(confirmado, bool): 
            self.__confirmado = confirmado
        else: 
            raise ValueError("Confirmação inválida")

class NTransferencia:
    __transferencias = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for trasnferencia in cls.listar():
            if trasnferencia.get_id() > id: id = trasnferencia.get_id()
        obj.set_id(id + 1)
        cls.__transferencias.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__transferencias
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for transferencia in cls.__transferencias:
            if transferencia.get_id() == id:
                return transferencia
        return None
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        transferencia = cls.listar_id(obj.get_id())
        if transferencia is not None:
            transferencia.set_id_conta(obj.get_id_conta())
            transferencia.set_id_conta_do_recebedor(obj.get_id_conta_do_recebedor())
            transferencia.set_valor(obj.get_valor())
            transferencia.set_confirmado(obj.get_confirmado())
        cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("transferencias.json", mode="w") as arquivo:
            json.dump(cls.__transferencias, arquivo, default=Transferencia.to_json)

    @classmethod
    def abrir(cls):
        cls.__transferencias = []
        try:
            with open("transferencias.json", mode="r") as arquivo:
                transferencias_json = json.load(arquivo)
                for obj in transferencias_json:
                    transferencia = Transferencia(
                        obj["id"],
                        obj["id_conta"],
                        obj["id_conta_do_recebedor"],
                        datetime.strptime(obj["data_transferencia"], "%d-%m-%Y %H:%M"),
                        obj["valor"],
                        obj["confirmado"]
                        )
                    cls.__transferencias.append(transferencia)
        except FileNotFoundError:
            pass