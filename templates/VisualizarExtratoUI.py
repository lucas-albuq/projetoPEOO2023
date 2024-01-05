import streamlit as st
import pandas as pd
from views import View
from datetime import datetime

class VisualizarExtratoUI:
    def main():
        st.header("Extrato da conta")
        VisualizarExtratoUI.abrir_extrato()

    def abrir_extrato():
        conta = View.Conta_listar_id(st.session_state["conta_id"])
        data_inicio_str = st.text_input("Data de início (dd/mm/aaaa)")
        data_fim_str = st.text_input("Data final (dd/mm/aaaa)")
        if st.button('Abrir extrato'):
            try:
                data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
                data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
                transferencias = View.Transferencia_abrir_extrato_do_dia(data_inicio, data_fim, conta.get_id())
                if transferencias is not None:
                    dic = []
                    for obj in transferencias: dic.append(obj.__dict__)
                    dataframe = pd.DataFrame(dic)
                    st.dataframe(dataframe)
                else:
                    st.write("Nenhuma transferência.")
            except ValueError as error:
                st.error(f"Erro ao abrir extrato: {error}")