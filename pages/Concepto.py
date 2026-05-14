import streamlit as st
import os
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
            text-aling: center;
            color: black;
            font-family: 'Comic Sans MS',
            cursive;
            font-size: 50px !important;
            text-aling: center;
            color:black;
            font-weight: bold;
            }
             </style>
             """, unsafe_allow_html=True)



biblioteca_conceptos = [
    {"Titulo": "Software","Texto": "Es el conjunto de programas e instrucciones que no se pueden tocar, pero permiten a los dispositivos realizar tareas."},
    {"Titulo": "Hardware","Texto": "Son los componentes físicos (como pantallas, teclados o circuitos) que conforman una computadora o celular."},
    {"Titulo": "IP (Dirección IP)","Texto": "Es como la dirección de tu casa, pero para tu dispositivo. Sin ella, el internet no sabría a dónde enviar la información que pediste."},
    {"Titulo": "La Nube (The Cloud)","Texto": "Es la computadora de alguien más. Cuando guardas algo en la nube, realmente se guarda en un disco duro gigante en un Centro de Datos."},
    {"Titulo": "Cookies","Texto": "Pequeños archivos que los sitios web guardan para recordarte, como cuando dejas productos en un carrito de compras."},
    {"Titulo": "Código Abierto (Open Source)", "Texto": "Es software cuyo 'plano de construcción' es público. Cualquiera puede verlo y mejorarlo para que la tecnología avance más rápido."}
]

st.title("Conceptos")


if 'usuario_logueado' in st.session_state:
    usuario = st.session_state.usuario_logueado
    # Limpiar el nombre para usarlo como clave en la DB
    usuario_key = usuario.replace(" ", "_").replace(".", "_")

    # Leer progreso
    data = db.child("usuarios").child(usuario_key).child("progreso").get()
    progreso = int(data.val()) if data.val() is not None else 0

    if progreso < len(biblioteca_conceptos):
        concepto = biblioteca_conceptos[progreso]

        st.markdown(f"""
        <div style="
            background-color: #FFF9C4; 
            padding: 25px; 
            border-radius: 20px; 
            border: 3px solid #FBC02D; 
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        ">
            <h2 style="color: black; font-family: 'Arial', sans-serif; margin-top: 0;">
                {concepto['Titulo']}
            </h2>
            <p style="color: black; font-size: 19px; font-family: 'Verdana', sans-serif; line-height: 1.5;">
                {concepto['Texto']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button("Continuar y regresar al inicio ➡️"):
            # Guardar nuevo progreso
            db.child("usuarios").child(usuario_key).child("progreso").set(progreso + 1)
            st.switch_page("pages/Pantalla Principal.py")
    else:
        st.balloons()
        st.success("¡Felicidades! Has terminado todos los conceptos por ahora.")
        if st.button("Volver al Inicio"):
            st.switch_page("pages/Pantalla Principal.py")

else:
    st.warning("Por favor, inicia sesión para ver tus conceptos.")
    if st.button("Ir al Login"):
        st.switch_page("app.py")
