from views import View
import streamlit as st
from datetime import datetime
import time

class ResgatarDinheiroUI:
    def main():
        st.header("Resgatar Dinheiro")
        ResgatarDinheiroUI.resgatar()
    def resgatar():
        cc = View.Conta_listar_por_tipo(st.session_state["cliente_id"], "Conta Corrente")
        cp = View.Conta_listar_id(st.session_state["conta_id"])
        st.write(f"Meu saldo: {cp.get_saldo()}")
        valor = st.number_input("Insira o valor para resgatar")
        if st.button("Resgatar dinheiro"):
            try:
                View.Transferencia_inserir(cp.get_id(), cc.get_id(), datetime.now(), valor)
                st.success("Dinheiro resgatado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro ao resgatar dinheiro: {error}")
            
            