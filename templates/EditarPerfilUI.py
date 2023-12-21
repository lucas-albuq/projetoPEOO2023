import streamlit as st
from views import View
import datetime
import time

class EditarPerfilUI:
    def main():
        st.header("Editar Perfil")
        tab1, tab2 = st.tabs(["Atualizar dados", "Gerenciar conta"])
        with tab1: EditarPerfilUI.atualizar()
        with tab2: EditarPerfilUI.dados_da_conta()

    def dados_da_conta():
        conta = View.Conta_listar_por_tipo(st.session_state["cliente_id"], st.session_state["tipo_conta"])
        st.title('Detalhes da Conta')
        st.write(f'Saldo: {conta.get_saldo()}')
        st.write(f'Limite: {conta.get_limite()}')
        st.write(f'Agência: {conta.get_agencia()}')
        st.write(f'Número da Conta: {conta.get_numero_conta()}')
        st.write(f'Tipo de Conta: {conta.get_tipo_conta()}')

        if st.button("Excluir conta"):
            View.Conta_excluir(conta.get_id())
            st.success("Conta excluída com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        cliente = View.Cliente_listar_id(st.session_state["cliente_id"])
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