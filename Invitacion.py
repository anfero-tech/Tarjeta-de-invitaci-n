import streamlit as st
from datetime import datetime
import urllib.parse

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
    }

    /* Contenedor del encabezado azul */
    .header-azul {
        background-color: #243656;
        padding: 40px 10px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        border-bottom: 5px solid #D4AF37;
    }

    /* TÍTULO EN CURSIVA, GIGANTE Y BLANCO */
    .titulo-mega {
        font-family: 'Great Vibes', cursive;
        font-size: 70px !important; /* Ajustado para pantalla de celular */
        color: #ffffff !important; /* Forzamos color BLANCO */
        margin: 0;
        padding: 0;
        line-height: 1.1;
    }

    .nombre-valentina {
        font-family: 'Cinzel', serif;
        font-size: 20px;
        color: #D4AF37;
        letter-spacing: 2px;
        margin-top: 15px; /* Separación clara del título */
        font-weight: 700;
        text-transform: uppercase;
    }

    /* CUADRO DE TEXTO EMOTIVO */
    .texto-emotivo {
        font-family: 'Raleway', sans-serif;
        font-size: 18px;
        font-style: italic;
        text-align: center;
        color: #243656;
        padding: 20px;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        margin-bottom: 30px;
        line-height: 1.6;
    }

    /* ICONOS DE FONDO (BALANZA Y BIRRETE) */
    .decoracion-fondo {
        text-align: center;
        opacity: 0.1;
        font-size: 100px;
        position: absolute;
        width: 100%;
        z-index: -1;
    }

    /* BOTÓN Y CONTACTO */
    .contacto-box {
        background-color: #243656;
        color: white;
        text-align: center;
        padding: 15px;
        border-radius: 8px;
        font-family: 'Cinzel', serif;
        border: 2px solid #D4AF37;
        margin-top: 20px;
    }
    
    /* Quitar padding extra de Streamlit en móvil */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. EFECTO DE COPOS DE NIEVE/ESTRELLAS (JavaScript)
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var duration = 10 * 1000;
        var animationEnd = Date.now() + duration;
        var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
          return Math.random() * (max - min) + min;
        }

        var interval = setInterval(function() {
          var timeLeft = animationEnd - Date.now();

          if (timeLeft <= 0) {
            return clearInterval(interval);
          }

          var particleCount = 50 * (timeLeft / duration);
          // COPOS DE NIEVE / ESTRELLAS
          confetti(Object.assign({}, defaults, { 
            particleCount, 
            origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
            colors: ['#ffffff', '#D4AF37'],
            shapes: ['circle', 'star'] 
          }));
          confetti(Object.assign({}, defaults, { 
            particleCount, 
            origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
            colors: ['#ffffff', '#D4AF37'],
            shapes: ['circle', 'star']
          }));
        }, 250);
    </script>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA INVITACIÓN OBTENIDO DE LAS IMÁGENES ---

# Iconos de fondo sutiles
st.markdown("<div class='decoracion-fondo'>⚖️ <br> 🎓</div>", unsafe_allow_html=True)

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
    <div style='text-align: center; color: #243656; font-family: "Cinzel";'>
        <h2 style='color: #D4AF37;'>Sábado 21 de Marzo</h2>
        <p style='font-size: 20px;'>07:00 P.M.</p>
        <hr style='border: 1px solid #D4AF37; width: 50%; margin: auto;'>
        <p style='margin-top: 15px;'><b>Conjunto Residencial Altos del Moral</b><br>Salón de Recepciones</p>
        <h3 style='color: #D4AF37; margin-top: 20px;'>✉️ Lluvia de Sobres</h3>
    </div>
    """, unsafe_allow_html=True)

# Conteo Regresivo
fecha_evento = datetime(2026, 3, 21, 19, 0, 0) # Fecha ajustada para conteo
faltan = fecha_evento - datetime.now()
c1, c2, c3 = st.columns(3)
c1.metric("Días", max(0, faltan.days))
c2.metric("Horas", max(0, faltan.seconds // 3600))
c3.metric("Minutos", (faltan.seconds // 60) % 60)

# Contacto (Obtenido de las imágenes)
st.markdown("""
    <div class='contacto-box'>
        Confirmar asistencia:<br>
        <span style='font-size: 22px;'>310 609 8356</span>
    </div>
    """, unsafe_allow_html=True)

# Formulario personalizado para móvil
with st.form("asistencia"):
    nombre = st.text_input("Nombre del invitado")
    
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
            border-radius: 8px !important;
            padding: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    submit = st.form_submit_button("¡ALLÍ ESTARÉ!")
    
    if submit:
        # Mensaje de agradecimiento después de confirmar
        st.success(f"¡Muchas gracias por tu confirmación, {nombre}! Te esperamos.")
        
        # Redirección a WhatsApp con mensaje predefinido para la mamá de Valentina
        # Número de teléfono de la mamá (obtenido de las imágenes)
        numero_mama = "+573106098356" 
        mensaje = f"¡Hola! Confirmo mi asistencia al grado de Valentina. Atentamente: {nombre}"
        url_whatsapp = f"https://wa.me/{numero_mama}?text={urllib.parse.quote(mensaje)}"
        
        # Usamos un componente de Streamlit para redirigir
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url_whatsapp}">', unsafe_allow_html=True)

# Mensaje de amor final
st.markdown("""
    <div style='text-align: center; font-family:serif; color:#aaaaaa; font-size: 12px; margin-top: 50px;'>
        Con mucho amor...<br>
        Familia Gonzalez Londoño y Novio ❤️<br>
        2026
    </div>
    """, unsafe_allow_html=True)
