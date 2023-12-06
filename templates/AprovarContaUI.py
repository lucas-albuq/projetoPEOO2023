import streamlit as st
import pandas as pd
from views import View
import time

class AprovarContaUI:
    def main():
        st.header("Aprovar Contas")
        tab1, tab2 = st.tabs(["Listar", "Atualizar"])
        with tab1: AprovarContaUI.listar()
        with tab2: AprovarContaUI.atualizar()

    def listar():
        contas_nao_aprovadas = []
        for conta in View.Conta_listar():
            if not conta.get_confirmado():
                contas_nao_aprovadas.append(conta)
        if len(contas_nao_aprovadas) == 0:
            st.write("Nenhuma conta para ser aprovada.")
        else:
            dic = {}
            for obj in contas_nao_aprovadas: dic.append(obj.__dict__)
            dataframe = pd.DataFrame(dic)
            st.dataframe(dataframe)
            
    def atualizar():
        contas_nao_aprovadas = []
        for conta in View.Conta_listar():
            if not conta.get_confirmado():
                contas_nao_aprovadas.append(conta)
        if len(contas_nao_aprovadas) == 0:
            st.write("Nenhuma conta para ser aprovada.")
        else:
            op = st.selectbox("Aprovação de contas", contas_nao_aprovadas)
            if st.button("Aprovar"):   
                View.Conta_atualizar(op.get_id(), op.get_id_cliente(), op.get_saldo(), op.get_limite(), op.get_agencia(), op.get_numero_conta(), op.get_tipo_conta(), True)
                time.sleep(2)
                st.rerun()
