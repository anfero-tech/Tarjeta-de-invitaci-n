import streamlit as st
from datetime import datetime

# 1. Configuración para móvil
st.set_page_config(page_title="Grado de Valentina", page_icon="⚖️", layout="centered")

# 2. CSS PROFESIONAL Y RESPONSIVO PARA CELULARES
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cinzel:wght@700&family=Raleway:ital,wght@1,400&display=swap');

    /* Fondo crema con iconos de derecho y birretes sutiles */
    .stApp {
        background-color: #fdfaf5;
        background-image: url("https://www.transparenttextures.com/patterns/gray-floral.png");
        z-index: 1;
    }

    /* Contenedor del encabezado azul */
    .header-azul {
        background-color: #243656;
        padding: 50px 15px; /* Más padding para impacto visual */
        text-align: center;
        margin: -60px -20px 30px -20px;
        border-bottom: 6px solid #D4AF37;
        z-index: 999;
        position: relative;
    }

    /* TÍTULO EN CURSIVA, GIGANTE Y BLANCO BRILLANTE */
    .titulo-mega {
        font-family: 'Great Vibes', cursive;
        font-size: clamp(80px, 18vw, 130px) !important; /* Más grande en móviles grandes */
        color: #ffffff !important; /* Forzamos color BLANCO */
        margin: 0;
        padding: 0;
        line-height: 0.9;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5); /* Sombra para resaltar */
        z-index: 1000;
    }

    .nombre-valentina {
        font-family: 'Cinzel', serif;
        font-size: clamp(18px, 4.5vw, 26px);
        color: #D4AF37;
        letter-spacing: 3px;
        margin-top: 25px; /* Separación clara del título */
        font-weight: 700;
        text-transform: uppercase;
        z-index: 1000;
    }

    /* CUADRO DE TEXTO EMOTIVO */
    .texto-emotivo {
        font-family: 'Raleway', sans-serif;
        font-size: clamp(16px, 4vw, 20px);
        font-style: italic;
        text-align: center;
        color: #243656;
        padding: 25px;
        background: rgba(255, 255, 255, 0.85);
        border-radius: 12px;
        margin-bottom: 40px;
        line-height: 1.7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
    }

    /* INFORMACIÓN DEL EVENTO */
    .info-evento-contenedor {
        text-align: center;
        color: #243656;
        font-family: "Cinzel", serif;
        background-color: white;
        padding: 30px 20px;
        border-radius: 10px;
        border: 1px solid #eee;
        margin-bottom: 30px;
    }

    .fecha-destacada {
        color: #D4AF37;
        font-size: clamp(24px, 6vw, 32px);
        margin-bottom: 10px;
        font-weight: bold;
    }

    .hora-lugar {
        font-size: clamp(16px, 4vw, 19px);
        margin: 8px 0;
    }

    .lluvia-sobres {
        color: #D4AF37;
        margin-top: 25px;
        font-weight: bold;
        font-size: clamp(20px, 5vw, 26px);
        letter-spacing: 1px;
    }

    /* BOTÓN Y CONTACTO */
    .contacto-box {
        background-color: #243656;
        color: white;
        text-align: center;
        padding: 18px;
        border-radius: 50px; /* Bordes redondeados modernos */
        font-family: 'Cinzel', serif;
        border: 2px solid #D4AF37;
        margin-top: 30px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        z-index: 10;
        position: relative;
    }

    .telefono-contacto {
        font-size: clamp(20px, 5vw, 26px);
        display: block;
        margin-top: 5px;
        color: #D4AF37;
    }
    
    /* MENSAJE DE AMOR FINAL */
    .mensaje-amor-final {
        text-align: center;
        font-family: 'Great Vibes', cursive;
        color: #243656;
        font-size: 32px;
        margin-top: 50px;
        margin-bottom: 30px;
        opacity: 0.9;
    }

    .firmas-finales {
        text-align: center;
        font-family: 'Raleway', sans-serif;
        color: #aaa;
        font-size: 11px;
        font-style: italic;
    }

    /* Quitar padding extra de Streamlit en móvil */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LLUVIA DE ESTRELLAS DORADAS (JavaScript - No globos)
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var duration = 4 * 1000;
        var animationEnd = Date.now() + duration;
        var defaults = { startVelocity: 25, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
          return Math.random() * (max - min) + min;
        }

        var interval = setInterval(function() {
          var timeLeft = animationEnd - Date.now();

          if (timeLeft <= 0) {
            return clearInterval(interval);
          }

          var particleCount = 40 * (timeLeft / duration);
          // LLUVIA DE ESTRELLAS
          confetti(Object.assign({}, defaults, { 
            particleCount, 
            origin: { x: randomInRange(0.1, 0.4), y: Math.random() - 0.2 },
            colors: ['#D4AF37', '#F5DF4D'],
            shapes: ['star'] 
          }));
          confetti(Object.assign({}, defaults, { 
            particleCount, 
            origin: { x: randomInRange(0.6, 0.9), y: Math.random() - 0.2 },
            colors: ['#D4AF37', '#F5DF4D'],
            shapes: ['star']
          }));
        }, 300);
    </script>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA INVITACIÓN OBTENIDO DE LAS IMÁGENES ---

# Encabezado Azul
st.markdown("""
    <div class='header-azul'>
        <h1 class='titulo-mega'>Mi Graduación</h1>
        <div class='nombre-valentina'>Valentina Londoño Gonzalez</div>
    </div>
    """, unsafe_allow_html=True)

# Texto Emotivo (Obtenido de las imágenes)
st.markdown("""
    <div class='texto-emotivo'>
        "Después de años de esfuerzo, sacrificios y sueños que jamás abandoné, 
        hoy recojo el fruto de mi constancia. Nada de esto habría sido posible 
        sin el amor, el apoyo y la guía incondicional de mis padres.
        Con el corazón lleno de gratitud, hoy me convierto en abogada."
    </div>
    """, unsafe_allow_html=True)

# Información del evento (Obtenida de las imágenes)
st.markdown("""
    <div class='info-evento-contenedor'>
        <div class='fecha-destacada'>Sábado, 21 de Marzo</div>
        <p class='hora-lugar'>07:00 P.M.</p>
        <hr style='border: 1px solid #eee; width: 60%; margin: 15px auto;'>
        <p class='hora-lugar' style='font-size: 16px; letter-spacing: 0.5px;'>
            <b>Conjunto Residencial Altos del Moral</b><br>
            Salón de Recepciones<br>
            CRA. 8A #153 - 51
        </p>
        <h3 class='lluvia-sobres'>✉️ ¡LLUVIA DE SOBRES!</h3>
    </div>
    """, unsafe_allow_html=True)

# Conteo Regresivo
fecha_evento = datetime(2026, 3, 22, 19, 0, 0) # Fecha ajustada para conteo
faltan = fecha_evento - datetime.now()
c1, c2, c3 = st.columns(3)
c1.metric("Días", max(0, faltan.days))
c2.metric("Horas", max(0, faltan.seconds // 3600))
c3.metric("Minutos", (faltan.seconds // 60) % 60)

# Contacto (Obtenido de las imágenes)
st.markdown("""
    <div class='contacto-box'>
        CONFIRMAR ASISTENCIA:
        <span class='telefono-contacto'>310 609 8356</span>
    </div>
    """, unsafe_allow_html=True)

# Formulario personalizado para móvil
with st.form("asistencia"):
    st.markdown("<p style='text-align:center; font-family:serif; color:#243656; font-size:18px;'>¿Cuento con tu valiosa presencia?</p>", unsafe_allow_html=True)
    nombre = st.text_input("Ingresa tu nombre para confirmar") # Campo personalizado y bonito
    st.markdown("<br>", unsafe_allow_html=True)
    
    # CSS para centrar y estilizar el botón del formulario
    st.markdown("""
        <style>
        .stButton>button {
            display: block;
            width: 100%;
            background-color: #243656 !important;
            color: white !important;
            font-family: 'Cinzel', serif !important;
            border: 2px solid #D4AF37 !important;
            border-radius: 30px !important;
            padding: 12px !important;
            font-weight: bold !important;
            letter-spacing: 1px !important;
            margin-top: -10px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    submit = st.form_submit_button("¡ALLÍ ESTARÉ!")
    if submit:
        st.balloons() # Refuerzo sutil de estrellas doradas al confirmar
        st.success(f"¡Confirmado! Gracias {nombre}. Valentina te espera.")

# Mensaje de amor final personalizado
st.markdown("""
    <div class='mensaje-amor-final'>Con mucho amor...</div>
    <div class='firmas-finales'>
        Familia Gonzalez Londoño y Novio ❤️<br>
        2026
    </div>
    """, unsafe_allow_html=True)