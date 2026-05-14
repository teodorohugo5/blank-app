import streamlit as st
import google.generativeai as genai
from PIL import Image
try:
    # Busca 'GEMINI_KEY' en tus Secrets de Streamlit Cloud
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Error: No se encontró la API Key en los Secrets.")
    st.stop() # Detiene la ejecución si no hay llave

# Usar el nombre de modelo estándar
model = genai.GenerativeModel('gemini-1.5-flash')
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


if "historial_chat" not in st.session_state:
    st.session_state.historial_chat = []

prompt_sistema = """
Eres Tlearnbot, la mascota y asistente amigable de Tlearnet. Tu misión es enseñar ciberseguridad a niños de forma divertida y segura.
- Usa un tono alegre, entusiasta y muchos emojis (🤖, 🛡️, ✨).
- Explica conceptos complejos con analogías sencillas (ej: una contraseña es como la llave de tu casa).
- Siempre prioriza la seguridad. Si detectas algo peligroso, advierte amablemente.
- Inicia la conversación saludando con entusiasmo y presentándote.
- Mantén la conversación fluida, reaccionando a lo que el niño te dice.
"""

if not st.session_state.historial_chat:
    st.session_state.historial_chat.append({"role": "user", "parts": [prompt_sistema]})
    try:
        response = model.generate_content(st.session_state.historial_chat)
        st.session_state.historial_chat.append({"role": "model", "parts": [response.text]})
    except Exception as e:
        st.error(f"Error al iniciar T-Bot: {e}")

st.title("Chat con Tlearnbot")
try:
    imagen_mascota = Image.open("dog.gif") 
    st.image(imagen_mascota, width=200)
except FileNotFoundError:
    st.warning("No se encontró la imagen 'dog.gif'.")

for mensaje in st.session_state.historial_chat[1:]:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["parts"][0])

if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    st.session_state.historial_chat.append({"role": "user", "parts": [prompt]})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("model"):
        with st.spinner("🤖 T-Bot está pensando..."):
            try:
                response = model.generate_content(st.session_state.historial_chat)
                st.session_state.historial_chat.append({"role": "model", "parts": [response.text]})
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Ocurrió un error al hablar con T-Bot: {e}")


if st.button("Ir a Pantalla Principal", use_container_width=True):
        st.switch_page("pages/Pantalla Principal.py")
