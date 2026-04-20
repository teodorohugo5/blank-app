import streamlit as st

st.set_page_config(page_title="Tlearnet - Programación", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #c8ddfa; }
    .cuadro-morado {
        background-color: #9b59b6;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        font-size: 20px;
        font-weight: bold;
    }
    .cuadro-blanco {
        background-color: rgba(255, 255, 255, 0.8);
        color: #333;
        padding: 20px;
        border: 3px dashed #9b59b6;
        border-radius: 15px;
        min-height: 60px;
        text-align: center;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'fase' not in st.session_state:
    st.session_state.fase = "algoritmos"
if 'pasos_cereal' not in st.session_state:
    st.session_state.pasos_cereal = []
if 'victoria' not in st.session_state:
    st.session_state.victoria = False

#  ALGORITMOS 
if st.session_state.fase == "algoritmos":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Algoritmos</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cuadro-morado'>Los algoritmos son una serie de pasos que lograr algo.Un ejemplo es servir un cereal. En la programación es la forma en que le damos indicaciones a la computadora.</div>", unsafe_allow_html=True)  
    st.markdown("<p style='color: #000000; font-size: 22px; font-weight: 400; text-align: left;'>Primero seleccionas el plato hondo, despues el cereal y al último la leche.</p>", unsafe_allow_html=True)  
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("Leche.png", width=100)
        if st.button("Leche", key="l1"): 
            st.session_state.pasos_cereal.append("leche")
            st.rerun()
        st.image("Papas.png", width=100)
        if st.button("Papas", key="p1"): 
            st.session_state.pasos_cereal.append("papas")
            st.rerun()
    with col2:
        st.image("Plato P.png", width=100)
        if st.button("Plato plano", key="pp1"): 
            st.session_state.pasos_cereal.append("plato plano")
            st.rerun()
        st.image("Plato ondo.png", width=100)
        if st.button("Plato hondo", key="ph1"): 
            st.session_state.pasos_cereal.append("plato hondo")
            st.rerun()
    with col3:
        st.image("Cereal.png", width=100)
        if st.button("Cereal", key="c1"): 
            st.session_state.pasos_cereal.append("cereal")
            st.rerun()
        st.image("Jugo.png", width=100)
        if st.button("Jugo", key="j1"): 
            st.session_state.pasos_cereal.append("jugo")
            st.rerun()

    texto = " , ".join(st.session_state.pasos_cereal)
    st.markdown(f"<div class='cuadro-blanco'>{texto}</div>", unsafe_allow_html=True)

    if not st.session_state.victoria:
        if st.button("Enviar ✅", use_container_width=True):
            if st.session_state.pasos_cereal == ["plato hondo", "cereal", "leche"]:
                st.session_state.victoria = True
                st.rerun()
            else:
                st.error("Orden incorrecto.")
                st.session_state.pasos_cereal = []
    else:
        st.balloons()
        st.success("¡Muy bien!")
        if st.button("Regresar al Inicio 🏠", use_container_width=True):
            st.session_state.victoria = False
            st.session_state.fase = "listas"
            st.session_state.pasos_cereal = []
            st.switch_page("pages/Pantalla Principal.py")

#  LISTAS
elif st.session_state.fase == "listas":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📊 Reto: Listas</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cuadro-morado'>Selecciona el elemento 1 (Índice 1)</div>", unsafe_allow_html=True)
    
    col_l1, col_l2, col_l3 = st.columns(3)
    with col_l1:
        if st.button("Bloques", use_container_width=True): st.error("¡Error! Este es el 0")
    with col_l2:
        if st.button("Pelota", use_container_width=True):
            st.session_state.victoria = True
            st.rerun()
    with col_l3:
        if st.button("Robot", use_container_width=True): st.error("¡Error! Este es el 2")

    if st.session_state.victoria:
        st.balloons()
        st.success("¡Muy bien!")
        if st.button("Regresar al Inicio 🏠", use_container_width=True):
            st.session_state.victoria = False
            st.session_state.fase = "variables"
            st.switch_page("pages/Pantalla Principal.py")

elif st.session_state.fase == "variables":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📦 Variables</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cuadro-morado'>Las variables es un espacio de memoria (como una caja) que tiene un nombre para identificarse y sirve para almacena datos, como número, texto o booleanos. Puedes guardar y recuperar información, algo muy útil al momento de programar.</div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<p style='color: #000000; font-size: 22px; font-weight: 400; text-align: left;'>Caja de animales</p>", unsafe_allow_html=True)  
        animal = st.selectbox("Selecciona", ["...", "Perro", "Rojo", "1"])
    with c2:
        st.markdown("<p style='color: #000000; font-size: 22px; font-weight: 400; text-align: left;'>Caja de colores</p>", unsafe_allow_html=True)  
        color = st.selectbox("Selecciona", ["...", "Gato", "Azul", "3"])
    with c3:
        st.markdown("<p style='color: #000000; font-size: 22px; font-weight: 400; text-align: left;'>Caja de números</p>", unsafe_allow_html=True)  
        numero = st.selectbox("Selecciona", ["...", "Conejo", "Amarillo", "2"])

    if not st.session_state.victoria:
        if st.button("Validar ✅", use_container_width=True):
            if animal == "Perro" and color == "Azul" and numero == "2":
                st.session_state.victoria = True
                st.rerun()
            else:
                st.error("Revisa las cajas.")
    else:
        st.balloons()
        st.success("¡Muy bien!")
        if st.button("Regresar al Inicio 🏠", use_container_width=True):
            st.session_state.victoria = False
            st.session_state.fase = "finalizado" 
            st.switch_page("pages/Pantalla Principal.py")

elif st.session_state.fase == "finalizado":
    st.markdown("<div class='cuadro-morado'>Haz terminado todos los juegos de esta sección, espera próximamente</div>", unsafe_allow_html=True)
    if st.button("🏠 Inicio"):
        st.switch_page("pages/Pantalla Principal.py")