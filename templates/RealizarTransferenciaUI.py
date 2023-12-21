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
        del(clientes[0])
        cc = View.Conta_listar_id(st.session_state["conta_id"])
        st.write(f"Meu saldo: {cc.get_saldo()}")
        op = st.selectbox("Destinatário", clientes)
        valor = st.number_input("Valor da transferencia")
        if st.button("Realizar Transferência"):
            try:
                transf = View.Transferencia_inserir(st.session_state["cliente_id"], op.get_id(), datetime.now(), valor)
                if transf:
                    st.success("Transferência realizada com sucesso.")
                else:
                    st.success("Transferência acima do limite, aguardando aprovação.")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro: {error}")    

