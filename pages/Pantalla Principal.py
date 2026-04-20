import streamlit as st
st.markdown("""
    <style>
    .stApp {
        background-color: #93b9dd;
    }
.title-font {
        font-family: 'Comic Sans MS', cursive;
        font-size: 50px !important;
        text-align: center;
        color: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Qué quieres aprender hoy?</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image("Logo ciberseguridad.jpg")
    if st.button("Ir a Ciberseguridad", use_container_width=True):
        st.switch_page("pages/Ciberseguridad.py")

    st.image("Conceptos.jpg")
    if st.button("Ir a Conceptos", use_container_width=True):
        st.switch_page("pages/Concepto.py")

    st.image("Programacion.jpg")
    if st.button("Ir a Programacion", use_container_width=True):
        st.switch_page("pages/Programacion.py")

with col2:
    st.image("Densi.jpg")
    if st.button("Ir a Desinformacion", use_container_width=True):
        st.switch_page("pages/Desinformacion.py")

    st.image("Datoscuriosos.jpg")
    if st.button("Ir a Datos curiosos", use_container_width=True):
        st.switch_page("pages/Datos cueriosos.py")

    st.image("Tlearnai.jpg")
    if st.button("Ir a Tlearbot", use_container_width=True):
        st.switch_page("pages/Tlearnia.py")

