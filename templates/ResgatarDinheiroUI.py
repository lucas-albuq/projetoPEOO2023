from views import View
import streamlit as st
import time

class ResgatarDinheiroUI:
    def resgatar():
        valor = st.number_input("Insira o valor para resgatar")
        if st.button("Resgatar dinheiro"):
            View.Conta_listar_id_cliente(st.session_state["cliente_id"])
            