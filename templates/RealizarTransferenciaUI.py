import streamlit as st
import pandas as pd
from views import View
from datetime import datetime
import time

class RealizarTransferenciaUI:
    def main():
        st.header("Realizar transferencia")
        RealizarTransferenciaUI.inserir()

    def inserir():
        clientes = View.Cliente_listar()
        cliente = View.Cliente_listar_id(st.session_state["cliente_id"])
        op = st.selectbox("Destinatário", clientes)
        valor = st.number_input("Valor da transferencia")
        if valor > View.Conta_listar_id_cliente(cliente.get_id()).get_saldo():
            st.error("Saldo insuficiente")
        elif valor > cliente.get_limite():
            View.Transferencia_inserir(st.session_state["cliente_id"], op.get_id(), datetime.now(), valor, False)
            st.success("Transferência aguardando aprovação do administrador.")
            time.sleep(2)
            st.rerun()
        else:
            View.Transferencia_inserir(st.session_state["cliente_id"], op.get_id(), datetime.now(), valor, True)
            op.set_saldo(op.get_saldo() + valor)
            cliente.set_saldo(op.get_saldo() - valor)
            st.sucess("Transferência realizada com sucesso.")
            time.sleep(2)
            st.rerun

