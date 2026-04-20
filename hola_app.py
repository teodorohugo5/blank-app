import pyrebase

# --- 1. CONFIGURACIÓN DE FIREBASE (Vía Secrets) ---
firebase_config = {
    "apiKey": st.secrets["firebase"]["apiKey"],
    "authDomain": st.secrets["firebase"]["authDomain"],
    "projectId": st.secrets["firebase"]["projectId"],
    "storageBucket": st.secrets["firebase"]["storageBucket"],
    "messagingSenderId": st.secrets["firebase"]["messagingSenderId"],
    "appId": st.secrets["firebase"]["appId"],
    "databaseURL": ""
}


# Inicialización de Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()