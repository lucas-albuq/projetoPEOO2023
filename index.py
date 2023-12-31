from templates.AbrirContaUI import AbrirContaUI
from templates.AprovarContaUI import AprovarContaUI
from templates.DepositarDinheiroUI import DepositarDinheiroUI
from templates.EditarPerfilUI import EditarPerfilUI
from templates.FazerCadastroUI import FazerCadastroUI
from templates.LoginUI import LoginUI
from templates.ManterContaUI import ManterContaUI
from templates.RealizarTransferenciaUI import RealizarTransferenciaUI
from templates.ResgatarDinheiroUI import ResgatarDinheiroUI
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
        if op == "Abrir Conta": FazerCadastroUI.main()
    
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Contas", "Aprovar Contas", "Validar Transferências"])
        if op == "Manter Contas": ManterContaUI.main()
        if op == "Aprovar Contas": AprovarContaUI.main()
        if op == "Validar Transferências": ValidarTransferenciaUI.main()
        
    def menu_cliente():
        tipos = View.Conta_listar_tipos_por_id_cliente(st.session_state["cliente_id"])
        if len(tipos) < 2:
            tipos.append("Abrir Conta")
        op = st.sidebar.selectbox("Conta", tipos)
        if op == "Conta Corrente": IndexUI.menu_cc()
        if op == "Conta Poupança": IndexUI.menu_cp()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cc():
        st.session_state["tipo_conta"] = "Conta Corrente"
        st.session_state["conta_id"] = View.Conta_listar_por_tipo(st.session_state["cliente_id"], "Conta Corrente").get_id()
        
        op = st.sidebar.selectbox("Menu", ["Realizar Transferência", "Visualizar Extrato", "Depositar Dinheiro", "Editar Perfil"])
        if op == "Realizar Transferência": RealizarTransferenciaUI.main()
        if op == "Visualizar Extrato": VisualizarExtratoUI.main()
        if op == "Depositar Dinheiro": DepositarDinheiroUI.main()
        if op == "Editar Perfil": EditarPerfilUI.main()

    def menu_cp():
        st.session_state["tipo_conta"] = "Conta Poupança"
        st.session_state["conta_id"] = View.Conta_listar_por_tipo(st.session_state["cliente_id"], "Conta Poupança").get_id()

        op = st.sidebar.selectbox("Menu", ["Resgatar Dinheiro", "Visualizar Extrato", "Editar Perfil"]) 
        if op == "Resgatar Dinheiro": ResgatarDinheiroUI.main()
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