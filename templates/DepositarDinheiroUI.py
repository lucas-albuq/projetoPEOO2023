from views import View
import streamlit as st
from datetime import datetime
import time

class DepositarDinheiroUI:
    def main():
        st.header("depositar Dinheiro")
        DepositarDinheiroUI.depositar()
    def depositar():
        cc = View.Conta_listar_por_tipo(st.session_state["cliente_id"], "Conta Poupança")
        cp = View.Conta_listar_id(st.session_state["conta_id"])
        st.write(f"Meu saldo: {cp.get_saldo()}")
        valor = st.number_input("Insira o valor para depositar")
        if st.button("depositar dinheiro"):
            try:
                st.write(View.Transferencia_inserir(cp.get_id(), cc.get_id(), datetime.now(), valor))
                st.success("Dinheiro depositado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro ao depositar dinheiro: {error}")
            
            