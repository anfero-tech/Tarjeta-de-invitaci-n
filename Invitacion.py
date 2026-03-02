import streamlit as st
from datetime import datetime
import urllib.parse

# 1. Configuración para móvil
st.set_page_config(page_title="Grado de Valentina", page_icon="⚖️", layout="centered")

# 2. CSS PARA COPOS, DISEÑO HORIZONTAL Y ESTILO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cinzel:wght@400;700&family=Raleway:wght@400;700&display=swap');

    .stApp {
        background-color: #fdfaf5;
        background-image: url("https://www.transparenttextures.com/patterns/gray-floral.png");
    }

    /* EFECTO DE COPOS */
    .snowflake { color: #fff; font-size: 1.2em; position:fixed; top:-10%; z-index:9999; animation-name: snowflakes-fall,snowflakes-shake; animation-duration:10s,3s; animation-timing-function:linear,ease-in-out; animation-iteration-count:infinite,infinite; }
    @keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}
    @keyframes snowflakes-shake{0%{transform:translateX(0px)}50%{transform:translateX(80px)}100%{transform:translateX(0px)}}
    
    .snowflake:nth-of-type(0){left:1%;animation-delay:0s,0s}
    .snowflake:nth-of-type(1){left:10%;animation-delay:1s,1s}
    .snowflake:nth-of-type(2){left:25%;animation-delay:6s,.5s}
    .snowflake:nth-of-type(3){left:40%;animation-delay:4s,2s}
    .snowflake:nth-of-type(4){left:60%;animation-delay:2s,2s}
    .snowflake:nth-of-type(5){left:80%;animation-delay:8s,3s}

    .header-azul {
        background-color: #243656;
        padding: 35px 10px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        border-bottom: 5px solid #D4AF37;
    }

    .titulo-mega {
        font-family: 'Great Vibes', cursive;
        font-size: 45px !important;
        color: #ffffff !important;
        margin-bottom: 10px;
    }

    .nombre-completo {
        font-family: 'Cinzel', serif;
        font-size: 22px;
        color: #D4AF37;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .texto-emotivo {
        font-family: 'Raleway', sans-serif;
        font-size: 15px;
        text-align: center;
        color: #243656;
        padding: 15px 25px;
        line-height: 1.6;
    }

    /* CUENTA REGRESIVA PEQUEÑA (Para evitar que se ponga vertical) */
    .timer-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 15px 0;
    }
    .timer-box {
        background: white;
        padding: 5px;
        border-radius: 5px;
        min-width: 55px;
        text-align: center;
        border: 1px solid #D4AF37;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .timer-num { font-size: 18px; font-weight: bold; color: #243656; }
    .timer-lab { font-size: 9px; text-transform: uppercase; color: #D4AF37; }

    .info-texto {
        font-family: 'Cinzel', serif;
        font-size: 14px;
        color: #243656;
        text-align: center;
        margin: 5px 0;
    }

    /* Estilo del botón de Streamlit */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #243656;
        background-color: #fdfaf5;
        color: #243656;
    }
    </style>
    
    <div class="snowflakes">
      <div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❅</div>
      <div class="snowflake">❆</div><div class="snowflake">❅</div><div class="snowflake">❆</div>
    </div>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.markdown("""
    <div class='header-azul'>
        <h1 class='titulo-mega'>Mi Graduación</h1>
        <div class='nombre-completo'>Valentina Londoño Gonzalez</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class='texto-emotivo'>
        Después de años de esfuerzo, sacrificios y sueños que jamás abandoné, 
        hoy recojo el fruto de mi constancia. Nada de esto habría sido posible 
        sin el amor, el apoyo y la guía incondicional de mis padres. 
        Con el corazón lleno de gratitud, hoy me convierto en abogada.
    </div>
    """, unsafe_allow_html=True)

# Cuenta regresiva horizontal optimizada
fecha = datetime(2026, 3, 21, 19, 0)
diff = fecha - datetime.now()
d, h, m = diff.days, diff.seconds//3600, (diff.seconds//60)%60

st.markdown(f"""
    <div class='timer-container'>
        <div class='timer-box'><div class='timer-num'>{d}</div><div class='timer-lab'>Días</div></div>
        <div class='timer-box'><div class='timer-num'>{h}</div><div class='timer-lab'>Horas</div></div>
        <div class='timer-box'><div class='timer-num'>{m}</div><div class='timer-lab'>Min</div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; margin: 20px 0;'>
        <p class='info-texto' style='color:#D4AF37; font-weight:bold; font-size:16px;'>DOMINGO 22 DE MARZO - 07:00 P.M.</p>
        <p class='info-texto'>Altos del Moral (Salón de Recepciones)</p>
        <p class='info-texto'>Cra. 8A #153 - 51</p>
        <p class='info-texto' style='color:#D4AF37;'>✉️ Lluvia de Sobres</p>
    </div>
    """, unsafe_allow_html=True)

# SECCIÓN DE CONFIRMACIÓN
st.markdown("<hr style='border:0.5px solid #D4AF37; opacity:0.3;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-family:Raleway; font-weight:bold; color:#243656;'>CONFIRMA TU ASISTENCIA</p>", unsafe_allow_html=True)

with st.form("asistencia_form"):
    nombre = st.text_input("Escribe tu nombre y apellido:")
    btn = st.form_submit_button("REGISTRAR NOMBRE")
    
    if btn:
        if nombre:
            st.session_state['nombre_confirmado'] = nombre
            st.balloons()
        else:
            st.warning("Por favor, ingresa tu nombre antes de continuar.")

# Mostrar el botón de WhatsApp solo si ya ingresaron el nombre
if 'nombre_confirmado' in st.session_state:
    nombre_inv = st.session_state['nombre_confirmado']
    num = "573196360231" 
    txt = urllib.parse.quote(f"¡Hola! Soy {nombre_inv}, confirmo mi asistencia al grado de Valentina Londoño Gonzalez. ¡Muchas gracias!")
    link = f"https://wa.me/{num}?text={txt}"
    
    st.markdown(f"""
        <div style="background-color: #e8f5e9; padding: 15px; border-radius: 10px; border: 1px solid #25D366; text-align: center;">
            <p style="color: #243656; font-family: Raleway; font-size: 14px; margin-bottom: 10px;">
                <b>¡Casi listo!</b> Para finalizar, por favor toca el botón de abajo para enviar tu confirmación por WhatsApp:
            </p>
            <a href="{link}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366; color:white; padding:12px; border-radius:30px; text-align:center; font-weight:bold; font-size:16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                    ✅ ENVIAR CONFIRMACIÓN POR WHATSAPP
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)


