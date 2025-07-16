import streamlit as st

# -------- Diccionario de frases a síntomas --------
frases_a_sintomas = {
    "me duele la cabeza": "dolor de cabeza",
    "tengo fiebre": "fiebre",
    "tengo tos": "tos",
    "tengo mocos": "congestión",
    "me duele la garganta": "dolor de garganta",
    "me duele el estómago": "dolor abdominal",
    "tengo diarrea": "diarrea",
    "vomité": "vómitos",
    "no puedo respirar": "dificultad respiratoria",
    "me siento mareado": "mareo",
    "me duelen los músculos": "dolor muscular",
    "me siento cansado": "fatiga",
    "no puedo dormir": "insomnio",
    "siento presión en la cabeza": "presión en la cabeza",
    "me duele el pecho": "dolor en el pecho",
    "siento hormigueo": "hormigueo",
    "siento que me ahogo": "sensación de ahogo",
    "sudo demasiado": "sudoración excesiva",
    "me duele el cuello": "dolor de cuello",
    "me duele el cuerpo": "dolor corporal",
    "me siento triste": "tristeza",
    "estoy ansioso": "ansiedad",
    "tengo estrés": "estrés",
    "no tengo energía": "fatiga emocional",
    "no me concentro": "falta de concentración",
    "siento que voy a explotar": "irritabilidad",
    "lloro sin razón": "llanto espontáneo",
    "me siento vacío": "vacío emocional",
    "tengo miedo sin razón": "miedo irracional",
    "pienso demasiado": "pensamientos repetitivos",
    "me siento culpable": "culpa",
}

# -------- Base de datos de enfermedades --------
enfermedades = {
    "Gripe": ["fiebre", "dolor de cabeza", "congestión", "tos", "dolor de garganta"],
    "COVID-19": ["fiebre", "tos", "dificultad respiratoria", "fatiga", "dolor muscular"],
    "Gastritis": ["dolor abdominal", "náuseas", "vómitos", "acidez"],
    "Migraña": ["dolor de cabeza", "presión en la cabeza", "mareo", "náuseas"],
    "Depresión": ["tristeza", "fatiga emocional", "vacío emocional", "culpa", "insomnio"],
    "Ansiedad": ["ansiedad", "miedo irracional", "pensamientos repetitivos", "palpitaciones", "sudoración excesiva"],
    "Estrés crónico": ["estrés", "dolor muscular", "irritabilidad", "dolor de cuello", "insomnio"],
    "Burnout": ["fatiga", "falta de concentración", "vacío emocional", "estrés"],
    "Sinusitis": ["dolor de cabeza", "congestión", "dolor de garganta"],
}

# -------- Recomendaciones --------
recomendaciones = {
    "Gripe": "Descansa, mantente hidratado y usa antipiréticos si es necesario.",
    "COVID-19": "Aíslate, usa mascarilla y consulta a un médico si los síntomas empeoran.",
    "Gastritis": "Evita alimentos irritantes, consume comidas ligeras y consulta con un gastroenterólogo.",
    "Migraña": "Descansa en un lugar oscuro, evita pantallas y toma analgésicos si es necesario.",
    "Depresión": "Busca apoyo emocional, intenta mantener una rutina y consulta con un psicólogo.",
    "Ansiedad": "Practica respiración profunda, evita cafeína y considera ayuda profesional.",
    "Estrés crónico": "Haz pausas activas, organiza tu tiempo y prueba técnicas de relajación.",
    "Burnout": "Tómate un descanso, organiza tus tareas y prioriza tu salud mental.",
    "Sinusitis": "Inhalaciones con vapor, descanso y consulta si hay fiebre persistente.",
}

# -------- Función para detectar síntomas --------
def detectar_sintomas(texto):
    texto = texto.lower()
    sintomas_detectados = []
    for frase, sintoma in frases_a_sintomas.items():
        if frase in texto:
            sintomas_detectados.append(sintoma)
    return list(set(sintomas_detectados))

# -------- Función para calcular coincidencias --------
def diagnosticar(sintomas_detectados):
    resultados = {}
    for enfermedad, sintomas_enfermedad in enfermedades.items():
        coincidencias = len(set(sintomas_detectados) & set(sintomas_enfermedad))
        if coincidencias > 0:
            resultados[enfermedad] = coincidencias / len(sintomas_enfermedad)
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
    return resultados_ordenados[:5]

# -------- Detectar emoción dominante --------
def detectar_emocion(sintomas_detectados):
    emociones = ["ansiedad", "tristeza", "culpa", "vacío emocional", "estrés", "fatiga emocional", "miedo irracional"]
    emociones_presentes = [e for e in emociones if e in sintomas_detectados]
    if emociones_presentes:
        return emociones_presentes[0]  # la primera dominante
    return None

# -------- Interfaz con Streamlit --------
st.set_page_config(page_title="Diagnóstico IA", layout="centered", page_icon="🧠")

st.title("🧠 Diagnóstico Inteligente Físico + Emocional")

entrada = st.text_area("Describe cómo te sientes hoy (síntomas físicos o emocionales):")

if st.button("Diagnosticar"):
    sintomas = detectar_sintomas(entrada)
    if not sintomas:
        st.error("No se detectaron síntomas conocidos. Intenta escribir de otra forma.")
    else:
        st.success(f"✅ Síntomas detectados: {', '.join(sintomas)}")

        diagnosticos = diagnosticar(sintomas)
        if diagnosticos:
            st.subheader("🔍 Diagnóstico probable:")
            for enfermedad, score in diagnosticos:
                st.write(f"**{enfermedad}** — {round(score * 100)}% de coincidencia")
                if enfermedad == diagnosticos[0][0]:  # solo para el más probable
                    st.info(f"🩺 Recomendación: {recomendaciones[enfermedad]}")

            emocion = detectar_emocion(sintomas)
            if emocion:
                st.warning(f"😟 Se detecta un estado emocional dominante: **{emocion}**. Considera hacer pausas, hablar con alguien o buscar ayuda emocional.")
        else:
            st.warning("No se pudo encontrar un diagnóstico claro.")

st.markdown("---")
st.caption("Creado por: Rafah Gondola, Adrián Abadía y Guillermo Sánchez.")
