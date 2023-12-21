import streamlit as st
from views import View
import time

class LoginUI:
  def main():
    st.header("Entrar no Sistema")
    LoginUI.entrar()
  def entrar():
    cpf = st.text_input("Informe o cpf")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      cliente = View.Cliente_login(cpf, senha) 
      if cliente is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + cliente.get_nome())
        st.session_state["cliente_id"] = cliente.get_id()
        st.session_state["cliente_nome"] = cliente.get_nome()
      else:
        st.error("Usuário ou senha inválido(s)!")
      time.sleep(2)
      st.rerun()      
