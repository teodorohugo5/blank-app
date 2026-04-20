import streamlit as st
import pandas as pd
import os

st.markdown("""
    <style>
    .stApp { background-color: #84a6c6; }
    .title-font { font-family: 'Arial Black'; font-size: 30px; text-align: center; color: black; font-weight: bold; }
    .text-body { text-align: center; font-size: 16px; color: black; margin-bottom: 10px; }
    
    .link-box-azul {
        background-color: #1A5276;
        padding: 12px;
        border-radius: 5px;
        text-align: center;
        color: white;
        font-family: Arial;
        font-size: 16px;
        border: 2px solid white;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


def avanzar_nivel():
    if 'usuario_logueado' in st.session_state:
        usuario = st.session_state.usuario_logueado
        if os.path.exists("usuarios_tlearnet.csv"):
            df = pd.read_csv("usuarios_tlearnet.csv")
            df.loc[df['usuario'] == usuario, 'progreso'] += 1
            df.to_csv("usuarios_tlearnet.csv", index=False)

nivel = 0
if 'usuario_logueado' in st.session_state:
    try:
        df = pd.read_csv("usuarios_tlearnet.csv")
        nivel = int(df[df['usuario'] == st.session_state.usuario_logueado]['progreso'].iloc[0])
    except:
        nivel = 0

if 'ganaste_ciber' not in st.session_state:
    st.session_state.ganaste_ciber = False
#  LINKS
if nivel == 0:
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Links</h1>", unsafe_allow_html=True)
    st.markdown('<p class="text-body">Por lo general solo suelen cambiar una letra, número o símbolo en el link.</p>', unsafe_allow_html=True)
    
    # OPCIÓN 1 (CORRECTA)
    st.markdown('<div class="link-box-azul">www.tiendaoficial.com</div>', unsafe_allow_html=True)
    if st.button("Selecciona el correcto (Opción 1)", key="l1"):
        st.session_state.ganaste_ciber = True
        st.rerun()

    # OPCIÓN 2 (FALSA)
    st.markdown('<div class="link-box-azul">www.tienda0ficial.com</div>', unsafe_allow_html=True)
    if st.button("Selecciona el correcto (Opción 2)", key="l2"):
        st.error("¡Cuidado! Este tiene un cero '0' en lugar de la 'o'.")

    # OPCIÓN 3 (FALSA)
    st.markdown('<div class="link-box-azul">www.ti3nda0ficial.com</div>', unsafe_allow_html=True)
    if st.button("Selecciona el correcto (Opción 3)", key="l3"):
        st.error("¡Incorrecto! Este tiene un '3' y un '0'.")

    if st.session_state.ganaste_ciber:
        st.balloons()
        st.success("¡Excelente! Has detectado el link real. ✅")
        
        if st.button("Continuar al Inicio 🏠", key="btn_next_level"):
            avanzar_nivel()
            st.session_state.ganaste_ciber = False
            st.switch_page("pages/Pantalla Principal.py")
# CONTRASEÑA 
elif nivel >= 1:
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Usa una contraseña segura</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cuadro-morado'>Crea una contraseña segura con los siguientes elementos.</div>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("✅ Letras mayusculas y minusculas (A-z)")
        st.markdown("✅ Números (0-9)")
    with col_b:
        st.markdown("✅ Símbolos (!@#)")
        st.markdown("✅ +8 caracteres")

    pass_input = st.text_input("Escribe tu contraseña aquí:", type="password", key="pass_reto_2")
    
    if st.button("Verificar contraseña", key="check_pass_final"):
        if len(pass_input) >= 8:
            st.session_state.ganaste_ciber = True
            st.rerun()
        else:
            st.warning("⚠️ ¡Es muy corta! Intenta que tenga al menos 8 letras o números.")

    if st.session_state.ganaste_ciber:
        st.balloons()
        st.success("¡Increíble! Ahora tus datos están protegidos. 🏆")
        
        if st.button("Finalizar y Volver al Inicio 🏠", key="btn_final_total"):
            st.session_state.ganaste_ciber = False
            st.switch_page("pages/Pantalla Principal.py")