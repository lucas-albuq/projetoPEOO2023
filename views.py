from models.cliente import Cliente, NCliente
from models.conta import Conta, NConta
from models.transferencia import Transferencia, NTransferencia
from datetime import datetime
import random

class View:
    def Cliente_inserir(nome, telefone, email, cpf, data_nascimento, senha):
        cliente = Cliente(0, nome, telefone, email, cpf, data_nascimento, senha)
        for obj in View.Cliente_listar():
            if obj.get_cpf() == cpf:
                raise ValueError("Cliente já cadastrado")
        NCliente.inserir(cliente)
        #validação dos outros dados já é feita dentro das classes
        #ver com Gilbert se também precisa fazer aqui

    def Cliente_listar():
        return NCliente.listar()

    def Cliente_listar_id(id):
        return NCliente.listar_id(id)

    def Cliente_listar_cpf(cpf):
        for cliente in View.Cliente_listar():
            if cliente.get_cpf() == cpf:
                return cliente
        return None

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
        View.Cliente_inserir("admin", "admin", "admin", "admin", datetime.today(), "admin")
        View.Conta_inserir(1, 10000.00, 10000.00, "Conta Admin", True)
    
    def Cliente_login(cpf, senha):
        for cliente in View.Cliente_listar():
            if cliente.get_cpf() == cpf and cliente.get_senha() == senha:
                conta = View.Conta_listar_id_cliente(cliente.get_id())
                if conta.get_confirmado():
                    return cliente
        return None
        
    def Conta_inserir(id_cliente, saldo, limite, tipo_conta, confirmado):
        while True:
                numero_conta = str(random.randint(10000, 99999))

                # Verificar se o número de conta já existe
                if not View.Conta_existe(numero_conta):
                    break
        conta = Conta(0, id_cliente, saldo, limite, "0001", str(numero_conta)+"-0", tipo_conta, confirmado)
        for obj in View.Conta_listar():
            if obj.get_id_cliente() == id_cliente:
                raise ValueError("Esse cliente já possui uma conta")
        NConta.inserir(conta)

    def Conta_listar():
        return NConta.listar()

    def Conta_listar_id(id):
        return NConta.listar_id(id)

    def Conta_listar_id_cliente(id):
        for conta in View.Conta_listar():
            if conta.get_id_cliente() == id:
                return conta
        return None
    
    def Conta_listar_nao_aprovadas():
        contas_nao_aprovadas = []
        for conta in View.Conta_listar():
            if not conta.get_confirmado():
                contas_nao_aprovadas.append(conta)
        return contas_nao_aprovadas

    def Conta_existe(numero_conta):
        for conta in NConta.listar():
            if conta.get_numero_conta() == numero_conta:
                return True
        return False
    
    def Conta_atualizar(id, id_cliente, saldo, limite, agencia, numero_conta, tipo_conta, confirmado):
        conta = Conta(id, id_cliente, saldo, limite, agencia, numero_conta, tipo_conta, confirmado)
        NConta.atualizar(conta)

    def Conta_excluir(id):
        conta = View.Conta_listar_id(id)
        NConta.excluir(conta)

    def Transferencia_inserir(id_conta, id_conta_do_recebedor, data_transferencia, valor):
        conta_pagador = View.Conta_listar_id(id_conta)
        conta_recebedor = View.Conta_listar_id(id_conta_do_recebedor)
        if valor > conta_pagador.get_saldo():
            raise ValueError("Saldo insuficiente")
        elif valor > conta_pagador.get_limite():
            transferencia = Transferencia(0, id_conta, id_conta_do_recebedor, data_transferencia, valor, False)
            NTransferencia.inserir(transferencia)
        else:
            transferencia = Transferencia(0, id_conta, id_conta_do_recebedor, data_transferencia, valor, True)
            conta_recebedor.set_saldo(conta_recebedor.get_saldo()+valor)
            conta_pagador.set_saldo(conta_pagador.get_saldo()-valor)
            NTransferencia.inserir(transferencia)
            return True

    def Transferencia_aprovar(id):
        transferencia = View.Transferencia_listar_id(id)
        View.Transferencia_atualizar()
        View.Transferencia_atualizar(transferencia.get_id(), transferencia.get_id_conta(), transferencia.get_id_conta_do_recebedor(), transferencia.get_data_transferencia(), transferencia.get_valor(), True)

    def Transferencia_listar():
        return NTransferencia.listar()

    def Transferencia_listar_id(id):
        return NTransferencia.listar_id(id)

    def Transferencia_listar_nao_confirmadas():
        transferencias = []
        for transferencia in View.Transferencia_listar():
            if not transferencia.get_confirmado():
                transferencias.append(transferencia)
        if len(transferencias) == 0:
            return None
        return transferencias

    def Transferencia_abrir_extrato_do_dia(data_inicio, data_fim, id_conta):
        extrato = []
        conta = View.Conta_listar_id(id_conta)
        for transferencia in NTransferencia.listar():
            if (data_fim >= transferencia.get_data_transferencia() >= data_inicio) and (conta.get_id() == transferencia.get_id_conta() or conta.get_id() == transferencia.get_id_conta_do_recebedor()):
                extrato.append(transferencia)
        if len(extrato) == 0:
            return None
        return extrato


    def Transferencia_atualizar(id, id_conta, id_conta_do_recebedor, data_transferencia, valor, confirmado: bool):
        transferencia = Transferencia(id, id_conta, id_conta_do_recebedor, data_transferencia, valor, confirmado)
        NTransferencia.atualizar(transferencia)

    def Transferencia_excluir(id):
        transferencia = View.Transferencia_listar_id(id)
        NTransferencia.excluir(transferencia)