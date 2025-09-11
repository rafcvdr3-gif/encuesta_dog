import streamlit as st

st.title("🐾 Evaluación para Adopción Responsable de Mascotas")
st.subheader("Evita regalar perros 🐶 como sorpresa o adquirirlos por moda. Cada perro merece un hogar donde sea amado, respetado y comprendido.")

# Estilo CSS para agrandar el texto de las preguntas
st.markdown("""
    <style>
    .pregunta {
        font-size: 18px;
        font-weight: bold;
        color: #1033330;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

puntaje = 0

# Pregunta 1
st.markdown('<div class="pregunta">¿Con qué frecuencia estás en casa 🏡 durante la semana?</div>', unsafe_allow_html=True)
respuesta1 = st.selectbox("", ["-", "Casi todo el tiempo", "Solo por las noches", "Solo los fines de semana", "Casi nunca"])
#respuesta1 = st.selectbox(st.title("¿Con qué frecuencia estás en casa durante la semana?"),
                          #["Casi todo el tiempo", "Solo por las noches", "Solo los fines de semana", "Casi nunca"])
if respuesta1 == "Casi todo el tiempo":
    puntaje += 1

# Pregunta 2
st.markdown('<div class="pregunta">¿Estás dispuesto a cubrir gastos veterinarios 🚑 , alimentación 🍖 y otros cuidados?</div>', unsafe_allow_html=True)
respuesta2 = st.selectbox("", ["Solo si no son muy altos", "No estoy seguro", "Sí, estoy preparado para asumir esos gastos", "Dependería de la situación"])
if respuesta2 == "Sí, estoy preparado para asumir esos gastos":
    puntaje += 1

# Pregunta 3
st.markdown('<div class="pregunta">¿Tienes experiencia previa cuidando mascotas?</div>', unsafe_allow_html=True)
respuesta3 = st.selectbox("", ["Si,he tenido mascotas antes", "No, pero estoy dispuesto a aprender", "No, y no me interesa aprender", "Solo he convivido con mascotas de otras personas"])
if respuesta3 == "Si,he tenido mascotas antes":
    puntaje += 1

# Pregunta 4
st.markdown('<div class="pregunta">¿Qué harías si tu mascota presenta problemas de comportamiento?</div>', unsafe_allow_html=True)
respuesta4 = st.selectbox("", ["Buscar ayuda profesional o entrenamiento", "Intentaria resolverlo por mi cuenta", "Lo consideraria un problema menor",
                           "Pensaria en devolverla"])
if respuesta4 == "Buscar ayuda profecional o entrenamiento":
    puntaje += 1

# Pregunta 5
st.markdown('<div class="pregunta">¿Tu vivienda permite tener mascotas?</div>', unsafe_allow_html=True)
respuesta5 = st.selectbox("", ["Si, está permitido y tengo espacio adecuado", "No estoy seguro", "Sí, aunque el espacio es limitado",
                           "No está permitido"])
if respuesta5 == "Si, está permitido y tengo espacio adecuado":
    puntaje += 1

# Pregunta 6
st.markdown('<div class="pregunta">¿Tengo tiempo diario para paseos, juego y atención?</div>', unsafe_allow_html=True)
respuesta6 = st.selectbox("", ["Si", "No", ])
if respuesta6 == "Si":
    puntaje += 1

# Pregunta 7
st.markdown('<div class="pregunta">¿Sabía que al adoptar un perro adquiere un compromiso de entre 10 y 15 años de cuidado y acompañamiento??</div>', unsafe_allow_html=True)
respuesta7 = st.selectbox("", [" Si", "No", ])
if respuesta7 == " Si":
   puntaje += 1

# (Agrega más preguntas aquí con lógica similar...)

# Evaluación final
if st.button("Evaluar aptitud para adoptar"):
    if puntaje >= 7:
        st.success("✅ ¡Felicidades! Según tus respuestas, eres apto para adoptar una mascota. Gracias por tu compromiso.")
    elif 2 <= puntaje < 7:
        st.warning("⚠️ Tienes buena disposición, pero hay aspectos que podrías considerar antes de adoptar. ¡Infórmate más y prepárate!")
    else:
        st.error("❌ Por ahora, no pareces estar listo para adoptar una mascota. Te recomendamos reflexionar y buscar orientación antes de tomar una decisión.")

