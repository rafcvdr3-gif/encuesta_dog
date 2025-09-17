import streamlit as st
import pandas as pd
from datetime import datetime

# Inicializar estado
if "mostrar_encuesta" not in st.session_state:
    st.session_state.mostrar_encuesta = True
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
for i in range(1, 11):
    if f"respuesta{i}" not in st.session_state:
        st.session_state[f"respuesta{i}"] = "-- Elige una opción --"

# Función para reiniciar encuesta
def reiniciar_encuesta():
    st.session_state.mostrar_encuesta = True
    st.session_state.puntaje = 0
    for i in range(1, 11):
        st.session_state[f"respuesta{i}"] = "-- Elige una opción --"
    st.rerun()

# Imagen de fondo y estilo
st.markdown("""
    <style>
    body {
        background-image: url("https://tusitio.com/fondo.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    .pregunta {
        font-size: 22px;
        font-weight: bold;
        color: #333333;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Logotipo institucional
st.markdown("""
    <div style='text-align: center'>
        <img src='https://tusitio.com/logo.png' width='150'>
    </div>
""", unsafe_allow_html=True)

st.title("🐾 Evaluación para Adopción Responsable de Mascotas")

# Mostrar encuesta
if st.session_state.mostrar_encuesta:
    puntaje = 0

    preguntas = [
        ("¿Con qué frecuencia estás en casa durante la semana?", ["Casi todo el tiempo"]),
        ("¿Estás dispuesto a cubrir gastos veterinarios, alimentación y otros cuidados?", ["Sí, estoy preparado para asumir esos gastos"]),
        ("¿Tienes experiencia previa cuidando mascotas?", ["Sí, he tenido mascotas antes"]),
        ("¿Qué harías si tu mascota presenta problemas de comportamiento?", ["Buscaría ayuda profesional o entrenamiento"]),
        ("¿Tu vivienda permite tener mascotas?", ["Sí, está permitido y tengo espacio adecuado"]),
        ("¿Estás dispuesto a dedicar tiempo diario para jugar y convivir con tu mascota?", ["Sí, todos los días"]),
        ("¿Qué harías si tu mascota se enferma y requiere atención urgente?", ["La llevaría al veterinario inmediatamente"]),
        ("¿Tienes apoyo familiar o de personas cercanas para cuidar a tu mascota si tú no puedes?", ["Sí, tengo apoyo confiable"]),
        ("Un perro puede vivir entre 10 y 15 años. ¿Ha considerado esta responsabilidad a largo plazo?", ["Sí, estoy consciente y preparado"]),
        ("¿Qué tipo de mascota consideras más adecuada para tu estilo de vida?", ["Una pequeña y tranquila"])
    ]

    opciones_por_pregunta = [
        ["-- Elige una opción --", "Casi todo el tiempo", "Solo por las noches", "Solo los fines de semana", "Casi nunca"],
        ["-- Elige una opción --", "Solo si no son muy altos", "No estoy seguro", "Sí, estoy preparado para asumir esos gastos", "Dependería de la situación"],
        ["-- Elige una opción --", "Sí, he tenido mascotas antes", "No, pero estoy dispuesto a aprender", "No, y no me interesa aprender", "Solo he convivido con mascotas de otras personas"],
        ["-- Elige una opción --", "Buscaría ayuda profesional o entrenamiento", "Intentaría resolverlo por mi cuenta", "Lo consideraría un problema menor", "Pensaría en devolverla"],
        ["-- Elige una opción --", "Sí, está permitido y tengo espacio adecuado", "No estoy seguro", "Sí, aunque el espacio es limitado", "No está permitido"],
        ["-- Elige una opción --", "Sí, todos los días", "Solo algunos días", "Rara vez", "No tengo tiempo"],
        ["-- Elige una opción --", "La llevaría al veterinario inmediatamente", "Esperaría a ver si mejora", "Buscaría remedios caseros", "No sabría qué hacer"],
        ["-- Elige una opción --", "Sí, tengo apoyo confiable", "Tal vez, pero no seguro", "No cuento con apoyo", "No lo he considerado"],
        ["-- Elige una opción --", "Sí, estoy consciente y preparado", "Más o menos", "No mucho", "No lo había pensado"],
        ["-- Elige una opción --", "Una que requiera atención constante", "Una independiente", "Una pequeña y tranquila", "No estoy seguro"]
    ]

    for i in range(10):
        st.markdown(f'<div class="pregunta">{preguntas[i][0]}</div>', unsafe_allow_html=True)
        st.session_state[f"respuesta{i+1}"] = st.selectbox(
            "", opciones_por_pregunta[i], index=opciones_por_pregunta[i].index(st.session_state[f"respuesta{i+1}"])
        )
        if st.session_state[f"respuesta{i+1}"] in preguntas[i][1]:
            puntaje += 1

    # Botón para evaluar
    if st.button("✅ Evaluar aptitud para adoptar"):
        st.session_state.mostrar_encuesta = False
        st.session_state.puntaje = puntaje
        st.divider()

        # Mostrar resultado
        if puntaje >= 8:
            st.success("✅ ¡Felicidades! Según tus respuestas, eres apto para adoptar una mascota. Gracias por tu compromiso.")
        elif 3 <= puntaje < 8:
            st.warning("⚠️ Tienes buena disposición, pero hay aspectos que podrías considerar antes de adoptar. ¡Infórmate más y prepárate!")
        else:
            st.error("❌ Por ahora, no pareces estar listo para adoptar una mascota. Te recomendamos reflexionar y buscar orientación antes de tomar una decisión.")

        # Guardar respuestas en CSV
        datos = {
            "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Puntaje": [puntaje]
        }
        for i in range(1, 11):
            datos[f"Pregunta {i}"] = [st.session_state[f"respuesta{i}"]]
        df = pd.DataFrame(datos)
        df.to_csv("respuestas_adopcion.csv", mode='a', header=False, index=False)
        st.info("📝 Tus respuestas han sido registradas correctamente.")

# Botón para iniciar nueva encuesta
if not st.session_state.mostrar_encuesta:
    if st.button("🔄 Iniciar nueva encuesta"):
        reiniciar_encuesta()
