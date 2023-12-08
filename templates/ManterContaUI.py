import streamlit as st
import pandas as pd
from views import View
import time

class ManterContaUI:
    def main():
        st.header("Manter conta")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterContaUI.listar()
        with tab2: ManterContaUI.inserir()
        with tab3: ManterContaUI.atualizar()
        with tab4: ManterContaUI.excluir()

    def listar():
        contas = View.Conta_listar()
        if len(contas) == 0:
            st.write("Nenhuma conta cadastrada.")
        else:
            dic = {}
            for obj in contas: dic.append(obj.__dict__)
            dataframe = pd.DataFrame(dic)
            st.dataframe(dataframe)

    def inserir():
        clientes = View.Cliente_listar()
        opCliente = st.selectbox("Cliente", clientes)
        saldo = st.text_input("Saldo inicial")
        limite = st.text_input("Limite da conta")
        agencia = st.text_input("Insira a agencia")
        numero_conta = st.text_input("Insira o número da conta")
        tipo_conta = st.text_input("Insira o tipo de conta")
        if st.button("Inserir"):
            try:
                View.Conta_inserir(opCliente.get_id(), float(saldo), float(limite), int(agencia), numero_conta, tipo_conta, True)
                st.success("Conta inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro ao criar conta: {error}")
    def atualizar():
        contas = View.Conta_listar()
        if len(contas) == 0:
            st.write("Nenhuma conta cadastrada.")
        else:
            op = st.selectbox("Aprovação de contas", contas)
            saldo = st.text_input("Saldo inicial", op.get_saldo())
            limite = st.text_input("Limite da conta", op.get_limite())
            agencia = st.text_input("Insira a agencia", op.get_agencia())
            numero_conta = st.text_input("Insira o número da conta", op.get_numero_conta())
            tipo_conta = st.text_input("Insira o tipo de conta", op.get_tipo_conta())
            if st.button("Atualizar"):
                try:
                    View.Conta_atualizar(op.get_id(), op.get_id_cliente(), float(saldo), float(limite), int(agencia), numero_conta, tipo_conta, True)
                    st.success("Conta atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as error:
                    st.error(f"Erro ao atualizar conta: {error}")
    def excluir():
        contas = View.Conta_listar()
        if len(contas) == 0:
            st.write("Nenhuma conta cadastrada.")
        else:
            op = st.selectbox("Excluir conta", contas)
            if st.button("Excluir"):
                View.Conta_excluir(op.get_id())
                st.success("Conta excluída com sucesso")
                time.sleep(2)
                st.rerun()
                               