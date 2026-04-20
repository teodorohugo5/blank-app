import streamlit as st
st.markdown("""
    <style>
    .stApp {
        background-color: #84a6c6;
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

if "paso_desinfo" not in st.session_state:
    st.session_state.paso_desinfo = 1

if "gano_reto" not in st.session_state:
    st.session_state.gano_reto = False

st.set_page_config(page_title="Tlearnet - Desinformación", layout="centered")

# NIVEL 1: FAKE NEWS
if st.session_state.paso_desinfo == 1:
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>¿Qué son las Fake News?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: black; font-weight: bold; font-size: 20px;'>Información falsa que se hace pasar por noticias con el propósito de engañar personas.</p>", unsafe_allow_html=True)        
    st.warning("🔎 ¿Cuál es la noticia REAL?")
    col_a, col_sep, col_b = st.columns([10, 1, 10])
    with col_a:
        st.image("Noticia Falsa .jpg", caption="Opción 1")
    with col_sep:
        st.markdown("<div style='background-color: white; width: 2px; height: 300px; margin: auto;'></div>", unsafe_allow_html=True)
    with col_b:
        st.image("Noticias segura.jpg", caption="Opción 2")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Elegir Opción 1", key="f1", use_container_width=True):
            st.error("❌ ¡Incorrecto!")
    with c2:
        if st.button("Elegir Opción 2", key="f2", use_container_width=True):
            st.session_state.gano_reto = True

#NIVEL 2: PHISHING 
elif st.session_state.paso_desinfo == 2:
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>¿Qué es phishing?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: black; font-weight: bold; font-size: 20px;'>Es cuando personas fingen ser paginas web de confianza y aprovechan para engañar y robar datos</p>", unsafe_allow_html=True)        
    
    st.subheader("🎣 Reto 2: ¿Página Real?")
    st.image("pishing.jpg", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("¡Es una trampa! 🚫", key="p1", use_container_width=True):
            st.session_state.gano_reto = True
    with col2:
        if st.button("Iniciar Sesión ✅", key="p2", use_container_width=True):
            st.error("❌ ¡Es un sitio falso!")

# NIVEL 3: EL OSO 
elif st.session_state.paso_desinfo == 3:
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Publicidad engañosa</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: black; font-weight: bold; font-size: 20px;'>Es cuando un anuncio de internet te dice una mentira o te presume algo que no es cierto para que lo quieras comprar algo, ejemplo un juguete.</p>", unsafe_allow_html=True) 
    
    st.subheader("🧸 Reto Final: El Oso")
    st.image("Oso.jpg", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("¡Lo quiero adquirir!", key="o1", use_container_width=True):
            st.error("❌ ¡Cuidado!")
    with col2:
        if st.button("Es Falso", key="o2", use_container_width=True):
            st.session_state.gano_reto = True

if st.session_state.gano_reto:
    st.balloons()
    st.success("🎉 ¡Felicidades! Has superado este reto.")
    if st.button("🏠 Volver al Inicio para continuar", use_container_width=True):
        if st.session_state.paso_desinfo < 3:
            st.session_state.paso_desinfo += 1
        else:
            st.session_state.paso_desinfo = 1
        st.session_state.gano_reto = False
        st.switch_page("pages/Pantalla Principal.py")

elif st.session_state.paso_desinfo == "finalizado":
    st.markdown("<div class='cuadro-morado'>Haz terminado todos los juegos de esta sección, espera próximamente</div>", unsafe_allow_html=True)
    if st.button("🏠 Inicio"):
        st.switch_page("pages/Pantalla Principal.py")