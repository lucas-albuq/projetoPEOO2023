import json
from models.modelo import Modelo
class Conta:
    def __init__(self, id, id_cliente, saldo, limite, agencia, numero_conta, tipo_conta, confirmado):
        self.set_id(id)
        self.set_id_cliente(id_cliente)
        self.set_saldo(saldo)
        self.set_limite(limite)
        self.set_agencia(agencia)
        self.set_numero_conta(numero_conta)
        self.set_tipo_conta(tipo_conta)
        self.set_confirmado(confirmado)

    def __str__(self):
        return f"id - {self.__id}, id do Cliente - {self.__id_cliente}, Saldo - {self.__saldo}, Limite - {self.__limite}, Agência - {self.__agencia}, Número da Conta - {self.__numero_conta}, Tipo de Conta - {self.__tipo_conta}, Confirmado - {self.__confirmado}"

    def to_json(self):
        return {
            "id": self.__id,
            "id_cliente": self.__id_cliente,
            "saldo": self.__saldo,
            "limite": self.__limite,
            "agencia": self.__agencia,
            "numero_conta": self.__numero_conta,
            "tipo_conta": self.__tipo_conta,
            "confirmado": self.__confirmado
        }

    def get_id(self):
        return self.__id

    def get_id_cliente(self):
        return self.__id_cliente

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_agencia(self):
        return self.__agencia

    def get_numero_conta(self):
        return self.__numero_conta

    def get_tipo_conta(self):
        return self.__tipo_conta
    
    def get_confirmado(self):
        return self.__confirmado

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("O ID inserido não é um número inteiro.")

    def set_id_cliente(self, id_cliente):
        if isinstance(id_cliente, int):
            self.__id_cliente = id_cliente
        else:
            raise ValueError("O ID do Cliente inserido não é um número inteiro.")

    def set_saldo(self, saldo):
        if isinstance(saldo, float):
            self.__saldo = saldo
        else:
            raise ValueError("Valor do saldo inválido")

    def set_limite(self, limite):
        if isinstance(limite, float):
            self.__limite = limite
        else:
            raise ValueError("Valor do limite inválido")

    def set_agencia(self, agencia):
        if isinstance(agencia, str) and len(agencia.strip()) != 0:
            self.__agencia = agencia
        else:
            raise ValueError("Agência inválida")

    def set_numero_conta(self, numero_conta):
        if isinstance(numero_conta, str) and len(numero_conta.strip()) != 0:
            self.__numero_conta = numero_conta
        else:
            raise ValueError("Número da conta inválido")

    def set_tipo_conta(self, tipo_conta):
        if isinstance(tipo_conta, str) and len(tipo_conta.strip()) != 0:
            self.__tipo_conta = tipo_conta
        else:
            raise ValueError("Tipo da conta inválido")

    def set_confirmado(self, confirmado):
        if isinstance(confirmado, bool):
            self.__confirmado = confirmado
        else:
            raise ValueError("Confirmação inválida")
class NConta (Modelo):
   
    @classmethod
    def salvar(cls):
        with open("contas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Conta.to_json)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("contas.json", mode="r") as arquivo:
                contas_json = json.load(arquivo)
                for obj in contas_json:
                    acc = Conta(
                        obj["id"],
                        obj["id_cliente"],
                        obj["saldo"],
                        obj["limite"],
                        obj["agencia"],
                        obj["numero_conta"],
                        obj["tipo_conta"],
                        obj["confirmado"]
                    )
                    cls.objetos.append(acc)
        except FileNotFoundError:
            pass
