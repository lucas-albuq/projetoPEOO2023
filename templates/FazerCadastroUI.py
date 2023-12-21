import streamlit as st
from views import View
import time
from datetime import datetime

class FazerCadastroUI:
  def main():
    st.header("Abrir Conta no Banco")
    FazerCadastroUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    telefone = st.text_input("Informe o telefone")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("Informe o seu cpf")
    data_nascimento = st.text_input("Informe sua data de nascimento (dd/mm/aaaa)")
    tipo_conta = st.selectbox("Tipo de conta", ["Conta Corrente", "Conta Poupança"])
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
        try:
          data = datetime.strptime(data_nascimento, "%d/%m/%Y")
          View.Cliente_inserir(nome, telefone, email, cpf, data, senha)
          cliente = View.Cliente_listar_cpf(cpf)
          if cliente is not None:
              View.Conta_inserir(cliente.get_id(), 10000.0, 1000.0, tipo_conta, False)
          st.success("Cliente cadastrado, conta aguardando ser aprovada.")
          time.sleep(2)
          st.rerun()
        except ValueError as error:
           st.error(f"Erro ao fazer cadastro: {error}")