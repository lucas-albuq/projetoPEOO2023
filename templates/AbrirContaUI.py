import streamlit as st
from views import View
import time
from datetime import datetime

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Banco")
    AbrirContaUI.inserir()
  
  def inserir():
    lista = ["Conta Corrente", "Conta Poupança"]
    listaCliente = View.Conta_listar_tipos_por_id_cliente(st.session_state["cliente_id"])
    lista = [tipo_conta for tipo_conta in lista if tipo_conta not in listaCliente]
    
    tipo_conta = st.selectbox("Tipo de conta", lista)

    if st.button("Inserir"):
        try:
          View.Conta_inserir(st.session_state["cliente_id"], 10000.0, 1000.0, tipo_conta, False)
          st.success("Conta aguardando aprovação do admin.")
          time.sleep(2)
          st.rerun()
        except ValueError as error:
           st.error(f"Erro ao abrir conta: {error}")