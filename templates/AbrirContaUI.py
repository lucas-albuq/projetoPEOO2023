import streamlit as st
from views import View
import time
from datetime import datetime
import random

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Banco")
    AbrirContaUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    telefone = st.text_input("Informe o telefone")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("Informe o seu cpf")
    data_nascimento = st.text_input("Informe sua data de nascimento (dd/mm/aaaa)")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        while True:
                numero_conta = str(random.randint(10000, 99999))

                # Verificar se o número de conta já existe
                if not View.Conta_existe(numero_conta):
                    break
                    
        View.Cliente_inserir(nome, telefone, email, cpf, data, senha)
        cliente = View.Cliente_listar_cpf(cpf)
        if cliente is not None:
            View.Conta_inserir(cliente.get_id(), 10000.0, 1000.0, 1, str(numero_conta)+"-0", "Conta Corrente", False)
        st.success("Conta criada com sucesso")
        time.sleep(2)
        st.rerun()