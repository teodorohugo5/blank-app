import streamlit as st
import pandas as pd
import os
import pyrebase

#Iniciar el firebase
firebase_config = {
    "apiKey": st.secrets["firebase"]["apiKey"],
    "authDomain": st.secrets["firebase"]["authDomain"],
    "projectId": st.secrets["firebase"]["projectId"],
    "storageBucket": st.secrets["firebase"]["storageBucket"],
    "messagingSenderId": st.secrets["firebase"]["messagingSenderId"],
    "appId": st.secrets["firebase"]["appId"],
    "databaseURL": ""
}


firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

st.set_page_config(page_title="Login Tlearnet", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #8ebbe6; }
    .title-font { font-family: 'Arial Black'; font-size: 30px; text-align: center; color: black; font-weight: bold; }
    .text-body { text-align: center; font-size: 16px; color: black; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Bienvenido a Tlearnet 🌐</h1>", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["📝 Registrarme", "🚀 Iniciar Sesión"])


with tab1:
    st.subheader("Crea tu cuenta")
    nuevo_usuario = st.text_input("¿Cómo te llamas?", key="reg_user")
    nueva_clave = st.text_input("Crea una contraseña (mínimo 6 caracteres)", type="password", key="reg_pass")
    
    if st.button("Crear mi cuenta"):
        if nuevo_usuario and nueva_clave:
            try:
               
                email = f"{nuevo_usuario.replace(' ', '_')}@tlearnet.com"
                
             
                auth.create_user_with_email_and_password(email, nueva_clave)
                
            
                st.session_state.usuario_logueado = nuevo_usuario
                st.success(f"¡Todo listo, {nuevo_usuario}! Entrando...")
                st.balloons()
                
                st.switch_page("pages/Pantalla Principal.py")
                
            except Exception as e:
                st.error("No se pudo crear la cuenta. Verifica que la contraseña tenga 6+ caracteres o que el nombre no esté repetido.")
        else:
            st.error("Por favor, llena todos los campos.")

with tab2:
    st.subheader("¡Hola de nuevo! Entra a jugar")
    usuario_login = st.text_input("Tu nombre de usuario", key="log_user")
    clave_login = st.text_input("Tu contraseña", type="password", key="log_pass")
    
    if st.button("¡Entrar a Tlearnet! 🚀"):
        if usuario_login and clave_login:
            try:
               
                email_login = f"{usuario_login.replace(' ', '_')}@tlearnet.com"
                auth.sign_in_with_email_and_password(email_login, clave_login)
                
    
                st.session_state.usuario_logueado = usuario_login
                st.success(f"¡Hola de nuevo, {usuario_login}!")
                st.switch_page("pages/Pantalla Principal.py")
                
            except Exception as e:
                st.error("Usuario o contraseña incorrectos. ❌")
        else:
            st.error("Por favor, escribe tus datos.")