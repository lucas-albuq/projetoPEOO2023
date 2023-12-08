import streamlit as st
from views import View
import datetime
import time

class EditarPerfilUI:
    def main():
        st.header("Editar Perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        cliente = View.Cliente_listar_id(st.session_state["Cliente_id"])
        nome = st.text_input("Informe o nome", cliente.get_nome())
        telefone = st.text_input("Informe o telefone", cliente.get_telefone())
        email = st.text_input("Informe o e-mail", cliente.get_email())
        cpf = st.text_input("Informe o seu cpf", cliente.get_cpf())
        data_nascimento = st.text_input("Informe sua data de nascimento (dd/mm/aaaa)", cliente.get_data_nascimento())
        senha = st.text_input("Informe a senha", cliente.get_senha())
        if st.button("Atualizar dados"):
            try:
                data = datetime.strptime(data_nascimento, "%d/%m/%Y")
                View.Cliente_atualizar(cliente.get_id(), nome, telefone, email, cpf, data, senha)
                st.success("Perfil atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro: {error}")