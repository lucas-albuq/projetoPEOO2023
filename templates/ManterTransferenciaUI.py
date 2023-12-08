import streamlit as st
import pandas as pd
from views import View
import time

class ManterTransferenciaUI:
    def main():
        st.header("Manter Transferencia")
        tab1, tab2 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterTransferenciaUI.listar()
        with tab2: ManterTransferenciaUI.inserir()

    def listar():
        transferencias = View.Transferencia_listar()
        if len(transferencias) == 0:
            st.write("Nenhuma transferencia realizada.")
        else:
            dic = {}
            for obj in transferencias: 
                if obj.get_confirmado():
                    dic.append(obj.__dict__)
            dataframe = pd.DataFrame(dic)
            st.dataframe(dataframe)

    def inserir():
        contas = View.Conta_listar()
        opPagador = st.selectbox("Conta pagador", contas)
        opRecebedor = st.selectbox("Conta recebedor", contas)
        valor = st.number_input("Insira o valor da transferencia")
        if st.button("Inserir"):
            if opPagador.get_saldo() < valor:
                st.error("O pagador não possui saldo para essa transferência")
            else:
                View.Transferencia_inserir(opPagador.get_id(), opRecebedor.get_id(), float(valor), True)
                opPagador.set_saldo(opPagador.get_saldo()-float(valor))
                opRecebedor.set_saldo(opRecebedor.get_saldo()+float(valor))
                st.success("Trasnferência concluída com sucesso.")
                time.sleep(2)
                st.rerun()   