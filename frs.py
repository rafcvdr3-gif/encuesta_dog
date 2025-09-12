import streamlit as st
import pandas as pd
from datetime import datetime

# Inicializar estado de la encuesta y respuestas
if "mostrar_encuesta" not in st.session_state:
    st.session_state.mostrar_encuesta = True
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
for i in range(1, 8):
    if f"respuesta{i}" not in st.session_state:
        st.session_state[f"respuesta{i}"] = "-- Elige una opción --"

# Función para reiniciar encuesta
def reiniciar_encuesta():
    st.session_state.mostrar_encuesta = True
    st.session_state.puntaje = 0
    for i in range(1, 8):
        st.session_state[f"respuesta{i}"] = "-- Elige una opción --"
    st.rerun()

# Imagen de fondo y estilo
st.markdown("""
    <style>
    body #{
#        background-image: url("https://tusitio.com/fondo.jpg");
#        background-size: cover;
#        background-attachment: fixed;
#        background-repeat: no-repeat;
#    }
    .pregunta {
        font-size: 22px;
        font-weight: bold;
        color: #333333;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Logotipo institucional
st.markdown("""
    <div style='text-align: center'>
        <img src='https://tusitio.com/logo.png' width='150'>
    </div>
""", unsafe_allow_html=True)

st.title("🐾 Tu compromiso con la adopción: un test para un final feliz.")
st.subheader("Evita regalar perros 🐶 como sorpresa o adquirirlos por moda. Cada perro merece un hogar donde sea amado, respetado y comprendido.")



# Mostrar encuesta si está activa
if st.session_state.mostrar_encuesta:
    puntaje = 0

    # Pregunta 1
    opciones1 = ["-- Elige una opción --", "Casi todo el tiempo", "Solo por las noches", "Solo los fines de semana", "Casi nunca"]
    st.markdown('<div class="pregunta">¿Con qué frecuencia estás en casa durante la semana?</div>', unsafe_allow_html=True)
    st.session_state.respuesta1 = st.selectbox("", opciones1, index=opciones1.index(st.session_state.respuesta1))

    if st.session_state.respuesta1 == "Casi todo el tiempo":
        puntaje += 1

    # Pregunta 2
    opciones2 = ["-- Elige una opción --", "Solo si no son muy altos", "No estoy seguro", "Sí, estoy preparado para asumir esos gastos", "Dependería de la situación"]
    st.markdown('<div class="pregunta">¿Estás dispuesto a cubrir gastos veterinarios, alimentación y otros cuidados?</div>', unsafe_allow_html=True)
    st.session_state.respuesta2 = st.selectbox("", opciones2, index=opciones2.index(st.session_state.respuesta2))

    if st.session_state.respuesta2 == "Sí, estoy preparado para asumir esos gastos":
        puntaje += 1

    # Pregunta 3
    opciones3 = ["-- Elige una opción --", "Sí, he tenido mascotas antes", "No, pero estoy dispuesto a aprender", "No, y no me interesa aprender", "Solo he convivido con mascotas de otras personas"]
    st.markdown('<div class="pregunta">¿Tienes experiencia previa cuidando mascotas?</div>', unsafe_allow_html=True)
    st.session_state.respuesta3 = st.selectbox("", opciones3, index=opciones3.index(st.session_state.respuesta3))

    if st.session_state.respuesta3 == "Sí, he tenido mascotas antes":
        puntaje += 1

    # Pregunta 4
    opciones4 = ["-- Elige una opción --", "Buscaría ayuda profesional o entrenamiento", "Intentaría resolverlo por mi cuenta", "Lo consideraría un problema menor", "Pensaría en devolverla"]
    st.markdown('<div class="pregunta">¿Qué harías si tu mascota presenta problemas de comportamiento?</div>', unsafe_allow_html=True)
    st.session_state.respuesta4 = st.selectbox("", opciones4, index=opciones4.index(st.session_state.respuesta4))

    if st.session_state.respuesta4 == "Buscaría ayuda profesional o entrenamiento":
        puntaje += 1

    # Pregunta 5
    opciones5 = ["-- Elige una opción --", "Sí, está permitido y tengo espacio adecuado", "No estoy seguro", "Sí, aunque el espacio es limitado", "No está permitido"]
    st.markdown('<div class="pregunta">¿Tu vivienda permite tener mascotas?</div>', unsafe_allow_html=True)
    st.session_state.respuesta5 = st.selectbox("", opciones5, index=opciones5.index(st.session_state.respuesta5))

    if st.session_state.respuesta5 == "Sí, está permitido y tengo espacio adecuado":
        puntaje += 1

    # Pregunta 6
    opciones6 = ["-- Elige una opción --", " Si ", "No"]
    st.markdown('<div class="pregunta">¿Tengo tiempo diario para paseos, juego y atención?</div>', unsafe_allow_html=True)
    st.session_state.respuesta6 = st.selectbox("", opciones6, index=opciones6.index(st.session_state.respuesta6))

    if st.session_state.respuesta6 == " Sí ,":
        puntaje += 1

    # Pregunta 7
    opciones7 = ["-- Elige una opción --", " puede ser ", " yo "]
    st.markdown('<div class="pregunta">¿Sabía que al adoptar un perro adquiere un compromiso de entre 10 y 15 años de cuidado y acompañamiento?</div>', unsafe_allow_html=True)
    st.session_state.respuesta7 = st.selectbox("", opciones7, index=opciones7.index(st.session_state.respuesta7))

    if st.session_state.respuesta7 == " puede ser ,":
        puntaje += 1


    # Botón para evaluar
    if st.button("✅ Evaluar aptitud para adoptar"):
        st.session_state.mostrar_encuesta = False
        st.session_state.puntaje = puntaje
        st.divider()

        # Mostrar resultado
        if puntaje >= 7:
            st.success("✅ ¡Felicidades! Según tus respuestas, eres apto para adoptar una mascota. Gracias por tu compromiso.")
        elif 2 <= puntaje < 8:
            st.warning("⚠️ Tienes buena disposición, pero hay aspectos que podrías considerar antes de adoptar. ¡Infórmate más y prepárate!")
        else:
            st.error("❌ Por ahora, no pareces estar listo para adoptar una mascota. Te recomendamos reflexionar y buscar orientación antes de tomar una decisión.")

        # Guardar respuestas en CSV
        datos = {
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Pregunta 1": [st.session_state.respuesta1],
            "Pregunta 2": [st.session_state.respuesta2],
            "Pregunta 3": [st.session_state.respuesta3],
            "Pregunta 4": [st.session_state.respuesta4],
            "Pregunta 5": [st.session_state.respuesta5],
            "Pregunta 6": [st.session_state.respuesta6],
            "Pregunta 7": [st.session_state.respuesta7],
            "Puntaje": [puntaje]
        }
        df = pd.DataFrame(datos)
        df.to_csv("respuestas_adopcion.csv", mode='a', header=False, index=False)
        st.info("📝 Tus respuestas han sido registradas correctamente.")

# Botón para iniciar nueva encuesta
if not st.session_state.mostrar_encuesta:
    if st.button("🔄 Iniciar nueva encuesta"):
        reiniciar_encuesta()
