import streamlit as st

# 1. Ícono de página dinámico y título fiestero en la pestaña
st.set_page_config(
    page_title="🥳 ¡FIESTA CRISS!",
    page_icon="🎂",
    layout="centered"
)

# 2. Festejo automático al abrir la página (Globos + Nieve instantáneos)
st.balloons()
st.snow()

# 3. Estilos visuales con fondo celeste pastel
st.markdown("""
    <style>
    /* Fondo celeste/azul pastel */
    .stApp {
        background-color: #EBF4F6;
    }
    
    /* Botón personalizado con tono azul */
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.divider()

# 4. Encabezado principal
st.title("🎉 ¡Feliz Cumpleaños Criss! 🎂")
st.write("Un regalo especial preparado con código ❤️")

st.divider()

# 5. Canción de Feliz Cumpleaños (Tu archivo MP3 local)
st.subheader("🎵 ¡Música maestro!")
try:
    st.audio("cumple.mp3", autoplay=True)
    st.caption("🔊 *(Si el navegador bloquea el inicio automático, dale Play)*")
except FileNotFoundError:
    st.error("⚠️ No se encontró el archivo 'cumple.mp3'. Verificá que esté guardado en la misma carpeta.")

st.divider()

# 6. Botón de festejo con notificación "Toast"
st.subheader("🥂 ¡A festejar!")
if st.button("🎈 ¡Hacé clic acá para celebrar!"):
    st.balloons()
    # Notificación emergente (Toast)
    st.toast("🔥 ¡VAMOOOO! ¡A festejar con todo!", icon="🥳")
    st.success("✨ ¡Por muchos años más juntos! ¡Salud y muy feliz cumpleaños! 🥂✨")

st.divider()

# 7. Carta o mensaje principal
st.subheader("✉️ Un mensaje para vos")
st.markdown("""
Hoy es un día súper especial y quería prepararte un detalle distinto para decirte **lo mucho que te quiero**.

Gracias por tu paciencia, por acompañarme siempre en cada paso, por enseñarme y por estar en los momentos más importantes.

¡Que tengas un año increíble, lleno de salud, alegrías, buena comida y muchos momentos compartidos!
""")

st.divider()

# 8. Cierre especial
st.markdown("<h2 style='text-align: center;'>❤️ Te amamossss!!!! ❤️</h2>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>💖 💕 💗 💓 💖</h1>", unsafe_allow_html=True)