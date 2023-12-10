from templates.AbrirContaUI import AbrirContaUI
from templates.AprovarContaUI import AprovarContaUI
from templates.EditarPerfilUI import EditarPerfilUI
from templates.LoginUI import LoginUI
from templates.ManterContaUI import ManterContaUI
from templates.RealizarTransferenciaUI import RealizarTransferenciaUI
from templates.ValidarTransferenciaUI import ValidarTransferenciaUI
from templates.VisualizarExtratoUI import VisualizarExtratoUI
from views import View
import streamlit as st

class IndexUI:
    def main():
        View.Cliente_admin()
        IndexUI.sidebar()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
        if op == "Login": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Contas", "Aprovar Contas", "Validar Transferências"])
        if op == "Manter Contas": ManterContaUI.main()
        if op == "Aprovar Contas": AprovarContaUI.main()
        if op == "Validar Transferências": ValidarTransferenciaUI.main()
        
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Realizar Transferência", "Visualizar Extrato", "Editar Perfil"])
        if op == "Realizar Transferência": RealizarTransferenciaUI.main()
        if op == "Visualizar Extrato": VisualizarExtratoUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()

    def btn_logout():
        if st.sidebar.button("Logout"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()   
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            clientes = View.Cliente_listar()
            if st.session_state["cliente_nome"] == clientes[0].get_nome(): IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.btn_logout()  
IndexUI.main()