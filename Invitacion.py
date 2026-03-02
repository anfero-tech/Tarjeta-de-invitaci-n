import streamlit as st
from datetime import datetime
import urllib.parse

# 1. Configuración para móvil
st.set_page_config(page_title="Grado de Valentina", page_icon="⚖️", layout="centered")

# 2. CSS ACTUALIZADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cinzel:wght@400;700&family=Raleway:ital,wght@0,400;1,400&display=swap');

    .stApp {
        background-color: #fdfaf5;
        background-image: url("https://www.transparenttextures.com/patterns/gray-floral.png");
    }

    .header-azul {
        background-color: #243656;
        padding: 40px 10px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        border-bottom: 5px solid #D4AF37;
    }

    .titulo-mega {
        font-family: 'Great Vibes', cursive;
        font-size: 55px !important;
        color: #ffffff !important;
        margin: 0;
        line-height: 1;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    }

    .nombre-valentina {
        font-family: 'Cinzel', serif;
        font-size: 18px;
        color: #D4AF37;
        letter-spacing: 2px;
        margin-top: 15px;
        font-weight: 700;
        text-transform: uppercase;
    }

    .texto-emotivo {
        font-family: 'Raleway', sans-serif;
        font-size: 16px;
        text-align: center;
        color: #243656;
        padding: 25px;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        margin-bottom: 25px;
        line-height: 1.6;
    }

    .info-texto {
        font-family: 'Cinzel', serif;
        font-size: 15px;
        color: #243656;
        margin: 5px 0;
        text-align: center;
    }

    .dorado-sutil {
        color: #D4AF37;
        font-weight: bold;
    }

    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin: 20px 0;
    }
    .countdown-box {
        text-align: center;
        background: white;
        padding: 10px;
        border-radius: 8px;
        min-width: 55px;
        border: 1px solid #eee;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .countdown-val { font-size: 18px; font-weight: bold; color: #D4AF37; }
    .countdown-lab { font-size: 9px; text-transform: uppercase; color: #243656; }

    .stButton>button {
        width: 100%;
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 12px !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        font-family: 'Raleway', sans-serif !important;
        font-size: 16px !important;
    }
    
    .mensaje-final {
        text-align: center;
        font-family: 'Great Vibes', cursive;
        color: #243656;
        font-size: 30px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---

st.markdown("""
    <div class='header-azul'>
        <h1 class='titulo-mega'>Mi Graduación</h1>
        <div class='nombre-valentina'>Valentina Londoño Gonzalez</div>
    </div>
    """, unsafe_allow_html=True)

# Texto sin comillas
st.markdown("""
    <div class='texto-emotivo'>
        Después de años de esfuerzo, sacrificios y sueños que jamás abandoné, 
        hoy recojo el fruto de mi constancia. Nada de esto habría sido posible 
        sin el amor, el apoyo y la guía incondicional de mis padres. 
        Con el corazón lleno de gratitud, hoy me convierto en abogada.
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div style='text-align: center;'>
        <p class='info-texto'><span class='dorado-sutil'>DOMINGO 22 DE MARZO</span></p>
        <p class='info-texto'>07:00 P.M.</p>
        <hr style='border: 0.5px solid #eee; width: 40%; margin: 10px auto;'>
        <p class='info-texto'>Conjunto Residencial Altos del Moral</p>
        <p class='info-texto'>Cra. 8A #153 - 51</p>
        <p class='info-texto dorado-sutil'>✉️ Lluvia de Sobres</p>
    </div>
    """, unsafe_allow_html=True)

# Cuenta regresiva horizontal
fecha_evento = datetime(2026, 3, 21, 19, 0, 0)
faltan = fecha_evento - datetime.now()
d, h, m = max(0, faltan.days), max(0, (faltan.seconds // 3600)), max(0, (faltan.seconds // 60) % 60)

st.markdown(f"""
    <div class='countdown-container'>
        <div class='countdown-box'><div class='countdown-val'>{d}</div><div class='countdown-lab'>Días</div></div>
        <div class='countdown-box'><div class='countdown-val'>{h}</div><div class='countdown-lab'>Horas</div></div>
        <div class='countdown-box'><div class='countdown-val'>{m}</div><div class='countdown-lab'>Min</div></div>
    </div>
    """, unsafe_allow_html=True)

# Formulario de confirmación a WhatsApp
with st.form("confirmacion"):
    st.markdown("<p style='text-align:center; color:#243656; font-family:Raleway;'>¿Nos acompañas?</p>", unsafe_allow_html=True)
    nombre_invitado = st.text_input("Ingresa tu nombre")
    confirmar = st.form_submit_button("CONFIRMAR ASISTENCIA")
    
    if confirmar:
        if nombre_invitado:
            # Número de la mamá de Valentina
            numero_mama = "573196360231" 
            mensaje_wa = f"¡Hola! Confirmo mi asistencia al grado de Valentina. Atentamente: {nombre_invitado}"
            url_whatsapp = f"https://wa.me/{numero_mama}?text={urllib.parse.quote(mensaje_wa)}"
            
            st.markdown(f'<meta http-equiv="refresh" content="0;URL={url_whatsapp}">', unsafe_allow_html=True)
            st.info("Abriendo WhatsApp...")
        else:
            st.warning("Por favor, ingresa tu nombre antes de confirmar.")

st.markdown("""
    <div class='mensaje-final'>Con mucho amor...</div>
    <div style='text-align:center; font-size:12px; color:#999; font-family:Raleway; margin-bottom:40px;'>
        Familia Gonzalez Londoño y Novio ❤️
    </div>
    """, unsafe_allow_html=True)



