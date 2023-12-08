import streamlit as st
import pandas as pd
from views import View
import time

class ValidarTransferenciaUI:
    def main():
        st.header("Validar Transferências")
        tab1, tab2 = st.tabs(["Listar", "Validar"])
        with tab1: ValidarTransferenciaUI.listar()
        with tab2: ValidarTransferenciaUI.atualizar()
    
    def listar():
        transferencias_nao_validadas = View.Transferencia_listar_nao_confirmadas()
        if transferencias_nao_validadas is not None:
            dic = {}
            for obj in transferencias_nao_validadas: dic.append(obj.__dict__)
            dataframe = pd.DataFrame(dic)
            st.dataframe(dataframe)
        else:
            st.write("Nenhuma transferência para ser validada.")
        
    def atualizar():
        transferencias_nao_validadas = View.Transferencia_listar_nao_confirmadas()
        op  = st.selectbox("Transferencias", transferencias_nao_validadas)
        if st.button("Autorizar"):
            View.Transferencia_aprovar(op.get_id())
            st.success("Transferência aprovada com sucesso.")
            time.sleep(2)
            st.rerun()
        elif st.button("Não autorizar"):
            View.Transferencia_excluir(op.get_id())
            st.success("Transferência recusada com sucesso")
            time.sleep(2)
            st.rerun()