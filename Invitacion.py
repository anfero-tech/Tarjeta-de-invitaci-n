import streamlit as st
from datetime import datetime
import urllib.parse

# 1. Configuración para móvil
st.set_page_config(page_title="Grado de Valentina", page_icon="⚖️", layout="centered")

# 2. CSS PARA COPOS Y DISEÑO HORIZONTAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cinzel:wght@400;700&family=Raleway:wght@400;700&display=swap');

    .stApp {
        background-color: #fdfaf5;
        background-image: url("https://www.transparenttextures.com/patterns/gray-floral.png");
    }

    /* EFECTO DE COPOS / NIEVE */
    .snowflake {
      color: #fff;
      font-size: 1em;
      font-family: Arial;
      text-shadow: 0 0 1px #000;
    }

    @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}
    @-webkit-keyframes snowflakes-shake{0%{-webkit-transform:translateX(0px);transform:translateX(0px)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}100%{-webkit-transform:translateX(0px);transform:translateX(0px)}}
    @keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}
    @keyframes snowflakes-shake{0%{transform:translateX(0px)}50%{transform:translateX(80px)}100%{transform:translateX(0px)}}
    .snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}
    .snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}
    .snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}
    .snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}
    .snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}
    .snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}
    .snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}
    .snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}

    .header-azul {
        background-color: #243656;
        padding: 30px 10px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        border-bottom: 5px solid #D4AF37;
    }

    .titulo-mega {
        font-family: 'Great Vibes', cursive;
        font-size: 50px !important;
        color: #ffffff !important;
        margin: 0;
    }

    .texto-emotivo {
        font-family: 'Raleway', sans-serif;
        font-size: 15px;
        text-align: center;
        color: #243656;
        padding: 20px;
        line-height: 1.5;
    }

    /* CUENTA REGRESIVA MINI HORIZONTAL */
    .timer-container {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin: 15px 0;
    }
    .timer-box {
        background: white;
        padding: 8px;
        border-radius: 5px;
        min-width: 50px;
        text-align: center;
        border: 1px solid #D4AF37;
    }
    .timer-num { font-size: 16px; font-weight: bold; color: #243656; }
    .timer-lab { font-size: 9px; text-transform: uppercase; color: #D4AF37; }

    .info-texto {
        font-family: 'Cinzel', serif;
        font-size: 14px;
        color: #243656;
        text-align: center;
        margin: 4px 0;
    }
    </style>
    
    <div class="snowflakes" aria-hidden="true">
      <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❅</div>
      <div class="snowflake">❆</div><div class="snowflake">❅</div><div class="snowflake">❆</div>
    </div>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.markdown("<div class='header-azul'><h1 class='titulo-mega'>Mi Graduación</h1></div>", unsafe_allow_html=True)

st.markdown("""
    <div class='texto-emotivo'>
        Después de años de esfuerzo, sacrificios y sueños que jamás abandoné, 
        hoy recojo el fruto de mi constancia. Nada de esto habría sido posible 
        sin el amor, el apoyo y la guía incondicional de mis padres. 
        Con el corazón lleno de gratitud, hoy me convierto en abogada.
    </div>
    """, unsafe_allow_html=True)

# Cuenta regresiva horizontal pequeña
fecha = datetime(2026, 3, 21, 19, 0)
diff = fecha - datetime.now()
d, h, m = diff.days, diff.seconds//3600, (diff.seconds//60)%60

st.markdown(f"""
    <div class='timer-container'>
        <div class='timer-box'><div class='timer-num'>{d}</div><div class='timer-lab'>Días</div></div>
        <div class='timer-box'><div class='timer-num'>{h}</div><div class='timer-lab'>Hrs</div></div>
        <div class='timer-box'><div class='timer-num'>{m}</div><div class='timer-lab'>Min</div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <p class='info-texto' style='color:#D4AF37; font-weight:bold;'>SÁBADO 21 DE MARZO - 07:00 P.M.</p>
        <p class='info-texto'>Altos del Moral (Salón de Recepciones)</p>
        <p class='info-texto'>Cra. 8A #153 - 51</p>
        <p class='info-texto' style='color:#D4AF37;'>✉️ Lluvia de Sobres</p>
    </div>
    """, unsafe_allow_html=True)

# FORMULARIO
with st.form("conf"):
    nombre = st.text_input("¿Quién confirma?")
    btn = st.form_submit_button("CONFIRMAR ASISTENCIA")
    
    if btn and nombre:
        # CORRECCIÓN DE WHATSAPP:
        # El número debe ir sin el "+" inicial en el enlace wa.me para que funcione en todos los navegadores
        num = "573196360231" 
        txt = urllib.parse.quote(f"¡Hola! Soy {nombre}, confirmo mi asistencia al grado de Valentina. ¡Muchas gracias!")
        link = f"https://wa.me/{num}?text={txt}"
        
        st.balloons() # Efecto de globos al confirmar
        st.success(f"¡Gracias {nombre}! Haz clic en el enlace para enviar el mensaje.")
        st.markdown(f'''
            <a href="{link}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">
                    ¡CLIC AQUÍ PARA ENVIAR WHATSAPP!
                </div>
            </a>
            ''', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; font-size:10px; color:gray;'>Familia Gonzalez Londoño y Novio ❤️</p>", unsafe_allow_html=True)


