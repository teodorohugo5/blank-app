import streamlit as st

st.markdown("""
<style>
    .stApp {
        background-color: #ff6d4d;
    }
    .title-font {
        font-family: 'Arial';
        font-size: 70px !important;
        text-align: center;
        color: black;
        font-weight: bold;
        margin-bottom: -20px; 
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title-font">TLEARNET</p>', unsafe_allow_html=True)
st.image("dog.gif")
if st.button("Comenzar", use_container_width=True):
    st.switch_page("pages/Iniciar sesion.py")