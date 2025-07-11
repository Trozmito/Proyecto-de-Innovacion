import streamlit as st

st.set_page_config(page_title="Diagnóstico IA", layout="centered")

# Frases comunes -> síntomas clave
frases_a_sintomas = {
    "dolor de cabeza": "dolor de cabeza",
    "me duele la cabeza": "dolor de cabeza",
    "fiebre": "fiebre",
    "me siento caliente": "fiebre",
    "dolor muscular": "dolores musculares",
    "dolores musculares": "dolores musculares",
    "me duelen los músculos": "dolores musculares",
    "no puedo dormir": "insomnio",
    "duermo mal": "insomnio",
    "me cuesta dormir": "insomnio",
    "cansancio": "fatiga",
    "estoy cansado": "fatiga",
    "me siento cansado": "fatiga",
    "tos seca": "tos seca",
    "tos": "tos seca",
    "dolor de garganta": "dolor de garganta",
    "me duele la garganta": "dolor de garganta",
    "presión en el pecho": "dolor en el pecho",
    "dificultad para respirar": "dificultad para respirar",
    "mareo": "mareo",
    "náuseas": "náuseas",
    "vómito": "vómitos",
    "no tengo ganas": "apatía",
    "me siento triste": "depresión",
    "tristeza": "depresión",
    "ansioso": "ansiedad",
    "me siento ansioso": "ansiedad",
    "estresado": "estrés",
    "me siento estresado": "estrés",
}

# Enfermedades con sus síntomas
enfermedades = {
    "Gripe": ["fiebre", "tos seca", "dolor de garganta", "dolores musculares", "fatiga"],
    "COVID-19": ["fiebre", "tos seca", "dificultad para respirar", "dolores musculares", "fatiga"],
    "Migraña": ["dolor de cabeza", "náuseas", "fatiga", "mareo"],
    "Insomnio": ["insomnio", "fatiga", "ansiedad"],
    "Estrés": ["estrés", "fatiga", "insomnio", "dolor de cabeza"],
    "Ansiedad": ["ansiedad", "insomnio", "mareo", "dificultad para respirar"],
    "Depresión": ["depresión", "apatía", "insomnio", "fatiga"],
    "Neumonía": ["fiebre", "tos seca", "dolor en el pecho", "dificultad para respirar"],
    "Resfriado común": ["fiebre", "tos seca", "dolor de garganta", "fatiga"],
}

# Recomendaciones para la más probable
recomendaciones = {
    "Gripe": ["Descansa mucho", "Toma líquidos", "Consulta al médico si la fiebre es alta"],
    "COVID-19": ["Aíslate", "Consulta a un médico", "Hidrátate bien"],
    "Migraña": ["Evita luces fuertes", "Descansa en un lugar tranquilo", "Consulta si el dolor es frecuente"],
    "Insomnio": ["Evita pantallas antes de dormir", "Mantén una rutina de sueño", "Haz respiraciones profundas"],
    "Estrés": ["Realiza ejercicios de relajación", "Habla con alguien de confianza", "Descansa"],
    "Ansiedad": ["Haz respiración lenta", "Evita la cafeína", "Busca apoyo emocional"],
    "Depresión": ["Busca apoyo emocional", "Haz actividad física ligera", "Consulta a un profesional"],
    "Neumonía": ["Consulta urgente al médico", "Descansa", "Sigue el tratamiento recetado"],
    "Resfriado común": ["Descansa", "Hidrátate", "Alivia los síntomas con medicamentos suaves"],
}

# Detectar síntomas en la frase
def detectar_sintomas(frase):
    sintomas = []
    frase = frase.lower()
    for clave, sintoma in frases_a_sintomas.items():
        if clave in frase:
            sintomas.append(sintoma)
    return list(set(sintomas))

# Diagnóstico basado en coincidencias
def diagnostico(sintomas):
    resultados = {}
    for enfermedad, sintomas_enf in enfermedades.items():
        coincidencias = set(sintomas).intersection(sintomas_enf)
        if coincidencias:
            porcentaje = round((len(coincidencias) / len(sintomas_enf)) * 100, 1)
            resultados[enfermedad] = porcentaje
    return sorted(resultados.items(), key=lambda x: x[1], reverse=True)[:5]

# Interfaz
st.title("🤖 Diagnóstico IA")
st.write("Describe cómo te sientes o tus síntomas. Ej: *Tengo fiebre y dolor de cabeza*")

entrada = st.text_area("✍️ Escribe aquí:")

if st.button("🔍 Analizar"):
    if not entrada.strip():
        st.warning("Por favor escribe algo.")
    else:
        sintomas_detectados = detectar_sintomas(entrada)
        if not sintomas_detectados:
            st.error("No se reconocieron síntomas. Intenta escribirlo de otra forma.")
        else:
            resultados = diagnostico(sintomas_detectados)
            if not resultados:
                st.warning("No se encontró un diagnóstico probable.")
            else:
                st.subheader("🩺 Diagnósticos más probables:")
                for i, (enf, porc) in enumerate(resultados):
                    st.markdown(f"**{i+1}. {enf}** — {porc}%")
                    if i == 0 and enf in recomendaciones:
                        st.write("💡 Recomendaciones:")
                        for r in recomendaciones[enf]:
                            st.write(f"- {r}")
                st.markdown("---")
                st.write("🧠 **Síntomas detectados:**")
                for s in sintomas_detectados:
                    st.write(f"- {s}")

# Créditos (al pie de página)
st.markdown("---")
st.markdown("### 👥 Creado por:")
st.markdown("- **Rafah Gondola**")
st.markdown("- **Adrián Abadía**")
st.markdown("- **Guillermo Sánchez**")
