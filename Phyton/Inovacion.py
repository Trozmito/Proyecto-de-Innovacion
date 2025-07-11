import streamlit as st

# Diccionario de frases clave para detectar síntomas
frases_a_sintomas = {
    "no puedo dormir": "insomnio",
    "duermo mal": "insomnio",
    "me cuesta dormir": "insomnio",
    "últimamente me siento cansado": "fatiga",
    "me siento cansado": "fatiga",
    "estoy irritable": "irritabilidad",
    "me duele la cabeza": "dolor de cabeza",
    "me siento raro": "ansiedad",
    "me siento incómodo": "estrés",
    "no tengo energía": "cansancio",
    "no tengo ganas de hacer nada": "apatía",
    "presión en el pecho": "ansiedad",
    "me cuesta respirar": "dificultad para respirar",
    "me siento sin ganas": "apatía",
    "me siento mal": "malestar general"
}

# Enfermedades relacionadas a síntomas
enfermedades = {
    "estrés": ["fatiga", "insomnio", "irritabilidad", "dolor de cabeza"],
    "ansiedad": ["insomnio", "ansiedad", "dificultad para respirar", "presión en el pecho"],
    "depresión": ["apatía", "cansancio", "insomnio", "malestar general"],
    "migraña": ["dolor de cabeza", "insomnio", "fatiga"],
}

# Recomendaciones para cada enfermedad
recomendaciones = {
    "estrés": [
        "🧘 Realiza ejercicios de respiración o meditación.",
        "💧 Bebe suficiente agua durante el día.",
        "🛌 Dormir al menos 7 horas por noche.",
    ],
    "ansiedad": [
        "🌿 Prueba infusiones naturales como valeriana o manzanilla.",
        "🚶 Da caminatas suaves al aire libre.",
        "🧘 Haz ejercicios de relajación guiada.",
    ],
    "depresión": [
        "🤝 Habla con alguien de confianza.",
        "🏃 Realiza actividad física ligera regularmente.",
        "📝 Lleva un diario emocional.",
    ],
    "migraña": [
        "🌑 Descansa en una habitación oscura.",
        "💧 Hidrátate bien.",
        "💊 Usa medicación si fue recetada por un médico.",
    ]
}

# Función para detectar síntomas en el texto del usuario
def detectar_sintomas_en_frase(frase_usuario):
    frase_usuario = frase_usuario.lower()
    sintomas_detectados = []
    for clave, sintoma in frases_a_sintomas.items():
        if clave in frase_usuario:
            sintomas_detectados.append(sintoma)
    return list(set(sintomas_detectados))  # eliminar duplicados

# Función para determinar el diagnóstico más probable
def diagnostico_ia(sintomas_usuario):
    resultados = {}
    for enfermedad, sintomas in enfermedades.items():
        coincidencias = set(sintomas_usuario).intersection(sintomas)
        if coincidencias:
            porcentaje = len(coincidencias) / len(sintomas)
            resultados[enfermedad] = round(porcentaje * 100, 1)
    # Ordenar por mayor porcentaje
    return sorted(resultados.items(), key=lambda x: x[1], reverse=True)

# Interfaz con Streamlit
st.title("🧠 IA Emocional - Diagnóstico desde tus palabras")

st.write("Escribe cómo te has sentido últimamente (ejemplo: 'me siento raro, no puedo dormir').")

entrada = st.text_area("Describe tus síntomas o cómo te sientes:")

if st.button("Analizar"):
    if not entrada.strip():
        st.error("Por favor, escribe algo para analizar.")
    else:
        sintomas = detectar_sintomas_en_frase(entrada)
        if not sintomas:
            st.warning("❌ No se detectaron síntomas. Intenta escribir cómo te sientes con más detalles.")
        else:
            diagnosticos = diagnostico_ia(sintomas)
            if not diagnosticos:
                st.warning("❌ No se encontró un diagnóstico claro con los síntomas ingresados.")
            else:
                st.subheader("🧾 Resultados:")
                st.markdown("**Síntomas detectados:**")
                for s in sintomas:
                    st.write(f"- {s}")
                enfermedad_principal, porcentaje = diagnosticos[0]
                st.markdown(f"**Diagnóstico más probable:** {enfermedad_principal.upper()} ({porcentaje}%)")
                if enfermedad_principal in recomendaciones:
                    st.markdown("**Recomendaciones:**")
                    for rec in recomendaciones[enfermedad_principal]:
                        st.write(f"- {rec}")
