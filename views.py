from models.cliente import Cliente, NCliente
from models.conta import Conta, NConta
from models.transferencia import Transferencia, NTransferencia
from datetime import datetime
from datetime import timedelta

class View:
    def Cliente_inserir(nome, telefone, email, cpf, data_nascimento, senha):
        cliente = Cliente(0, nome, telefone, email, cpf, data_nascimento, senha)
        for obj in View.Cliente_listar():
            if obj.get_cpf() == cpf:
                raise ValueError("Cliente já cadastrado")
        NCliente.inserir(Cliente)
        #validação dos outros dados já é feita dentro da classe Cliente
        #ver com Gilbert se também precisa fazer aqui

    def Cliente_listar():
        NCliente.listar()

    def Cliente_listar_id(id):
        NCliente.listar_id(id)

    def Cliente_atualizar(id, nome, telefone, email, cpf, data_nascimento, senha):
        cliente = Cliente(id, nome, telefone, email, cpf, data_nascimento, senha)
        NCliente.atualizar(cliente)

    def Cliente_excluir(id):
        cliente = View.Cliente_listar_id(id)
        NCliente.excluir(cliente)

    def Cliente_admin():
        for cliente in View.Cliente_listar():
            if cliente.get_nome() == "admin":
                return
        View.Cliente_inserir("admin", "admin", "admin", "000000000-00", datetime.today(), "0000")

    def Conta_inserir(obj):
        NConta.inserir(obj)

    def Conta_listar():
        NConta.listar()

    def Conta_listar_id(id):
        NConta.listar_id(id)

    def Conta_atualizar(obj):
        NConta.atualizar(obj)

    def Conta_excluir(obj):
        NConta.excluir(obj)

    def Transferencia_inserir(obj):
        NTransferencia.inserir(obj)

    def Transferencia_listar():
        NTransferencia.listar()

    def Transferencia_listar_id(id):
        NTransferencia.listar_id(id)

    def Transferencia_abrir_extrato_do_dia(data_inicio, data_fim):
        extrato = []
        for Transferencia in NTransferencia.listar():
            if data_fim >= Transferencia.get_data_transferencia() >= data_inicio:
                extrato.append(Transferencia)
        return extrato


    def Transferencia_atualizar(obj):
        NTransferencia.atualizar(obj)

    def Transferencia_excluir(obj):
        NTransferencia.excluir(obj)