import streamlit as st
import pyrebase

firebase_config = {
    "apiKey": st.secrets["firebase"]["apiKey"],
    "authDomain": st.secrets["firebase"]["authDomain"],
    "projectId": st.secrets["firebase"]["projectId"],
    "storageBucket": st.secrets["firebase"]["storageBucket"],
    "messagingSenderId": st.secrets["firebase"]["messagingSenderId"],
    "appId": st.secrets["firebase"]["appId"],
    "databaseURL": st.secrets["firebase"]["databaseURL"]
}
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


st.markdown("""
    <style>
    .stApp {
        background-color: #93b9dd;
    }
    .custom-box {
        background-color: #f1d031;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        color: black;
        font-family: 'Comic Sans MS', cursive;
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


biblioteca_curiosidades = [
    {"Titulo": "El primer lenguaje de programación fue creado por una mujer","Texto": "En la década de 1840, Ada Lovelace escribió el primer algoritmo destinado a ser procesado por una máquina."},
    {"Titulo": "El primer 'bug' fue un insecto","Texto": "Grace Hopper encontró una polilla atrapada en una computadora que causaba errores. De ahí viene el término 'bug'."},
    {"Titulo": "¿Por qué los links son azules?","Texto": "Se eligió el azul porque en los monitores antiguos era el color con mejor contraste después del negro."},
    {"Titulo": "El Internet viaja por el mar","Texto": "El 99% del tráfico de internet mundial se transmite a través de cables submarinos de fibra óptica."},
    {"Titulo": "El primer mensaje de texto (SMS)","Texto": "Se envió el 3 de diciembre de 1992 y decía 'Merry Christmas'. Se envió desde una computadora porque los celulares no tenían teclado de letras."}
    ]
st.title("¿Sabías que...? 💡")
if 'usuario_logueado' in st.session_state:
    usuario = st.session_state.usuario_logueado
    usuario_key = usuario.replace(" ", "_").replace(".", "_")
 
    # --- Leer progreso desde Realtime Database ---
    data = db.child("usuarios").child(usuario_key).child("progreso_curioso").get()
    progreso = int(data.val()) if data.val() is not None else 0
 
    if progreso < len(biblioteca_curiosidades):
        dato = biblioteca_curiosidades[progreso]
 
        st.markdown(f"""
        <div style="background-color: #E0F7FA; padding: 25px; border-radius: 20px; border: 3px solid #4DD0E1; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h2 style="color: black; font-family: 'Arial', sans-serif; margin-top: 0; font-weight: bold;">{dato['Titulo']}</h2>
            <p style="color: black; font-size: 19px; font-family: 'Verdana', sans-serif; line-height: 1.5;">{dato['Texto']}</p>
        </div>
        """, unsafe_allow_html=True)
 
        st.write("")
 
        if st.button("¡Qué increíble! Ver más después ➡️"):
            # --- Guardar progreso en Realtime Database ---
            db.child("usuarios").child(usuario_key).child("progreso_curioso").set(progreso + 1)
            st.success("¡Dato guardado en tu memoria de héroe!")
            st.switch_page("pages/Pantalla Principal.py")
 
    else:
        st.balloons()
        st.subheader("¡Vaya! Eres un experto en historia digital.")
        st.write("Ya conoces todos los datos curiosos que tenemos por ahora.")
        if st.button("Volver al Inicio"):
            st.switch_page("pages/Pantalla Principal.py")
 
else:
    st.warning("Héroe, primero debes iniciar sesión para descubrir secretos.")
    if st.button("Ir al Login"):
        st.switch_page("app.py")
 
