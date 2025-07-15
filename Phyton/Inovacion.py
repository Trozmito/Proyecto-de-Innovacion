import streamlit as st

st.set_page_config(page_title="IA Diagnóstico Emocional y Físico", layout="centered")

# Frases comunes -> síntomas físicos y emocionales
frases_a_sintomas = {
    # Físicos
    "me duele la cabeza": "dolor de cabeza", "dolor de cabeza": "dolor de cabeza",
    "tengo fiebre": "fiebre", "temperatura alta": "fiebre", "me siento caliente": "fiebre",
    "escalofríos": "escalofríos", "tiritando": "escalofríos",
    "me duele el cuerpo": "dolores musculares", "dolor muscular": "dolores musculares", "dolores en los músculos": "dolores musculares",
    "no puedo dormir": "insomnio", "duermo mal": "insomnio", "insomnio": "insomnio",
    "estoy cansado": "fatiga", "me siento agotado": "fatiga", "cansancio": "fatiga", "debilidad": "fatiga",
    "tengo tos seca": "tos seca", "tos seca": "tos seca",
    "tengo flema": "tos con flema", "tos con flema": "tos con flema",
    "tengo mocos": "congestión nasal", "nariz tapada": "congestión nasal", "goteo nasal": "congestión nasal",
    "me duele la garganta": "dolor de garganta", "ardor en la garganta": "dolor de garganta",
    "no respiro bien": "dificultad para respirar", "me cuesta respirar": "dificultad para respirar",
    "náuseas": "náuseas", "ganas de vomitar": "náuseas",
    "vomité": "vómitos", "vómito": "vómitos",
    "diarrea": "diarrea", "evacuaciones líquidas": "diarrea",
    "dolor de estómago": "dolor estomacal", "retorcijones": "dolor estomacal", "malestar estomacal": "dolor estomacal",
    "reflujo": "reflujo", "acidez": "reflujo",
    "visión borrosa": "visión borrosa",
    "ojos rojos": "ojos irritados", "picazón en los ojos": "ojos irritados", "ojos llorosos": "ojos irritados",
    "zumbido en los oídos": "dolor de oídos", "dolor en los oídos": "dolor de oídos",
    "latidos rápidos": "palpitaciones", "palpitaciones": "palpitaciones",
    "mareo": "mareo", "me siento mareado": "mareo",
    "no huelo nada": "pérdida del olfato", "pérdida del olfato": "pérdida del olfato",
    "me duele la espalda": "dolor lumbar", "dolor lumbar": "dolor lumbar",
    
    # Emocionales
    "me siento triste": "tristeza", "estoy triste": "tristeza",
    "me siento vacío": "apatía", "sin ganas de nada": "apatía", "no quiero hacer nada": "apatía",
    "estoy estresado": "estrés", "siento mucho estrés": "estrés", "me siento presionado": "estrés",
    "tengo ansiedad": "ansiedad", "me siento ansioso": "ansiedad", "estoy nervioso": "ansiedad",
    "me altero fácilmente": "irritabilidad", "me enojo fácil": "irritabilidad",
    "no me concentro": "niebla mental", "me cuesta concentrarme": "niebla mental", "mi mente está nublada": "niebla mental",
    "me siento inquieto": "ansiedad", "me siento mal emocionalmente": "tristeza",
    "no tengo motivación": "apatía", "me siento apagado": "apatía",
}

# Enfermedades ampliadas
enfermedades = {
    "Gripe": ["fiebre", "dolor de cabeza", "fatiga", "tos seca", "escalofríos", "dolores musculares"],
    "Resfriado común": ["congestión nasal", "tos seca", "dolor de garganta", "fiebre"],
    "COVID-19": ["fiebre", "tos seca", "fatiga", "dolor de cabeza", "dificultad para respirar", "pérdida del olfato"],
    "Gastritis por ansiedad": ["dolor estomacal", "náuseas", "ansiedad", "insomnio"],
    "Estrés crónico": ["estrés", "dolor de cabeza", "dolores musculares", "insomnio", "fatiga"],
    "Depresión": ["tristeza", "apatía", "insomnio", "fatiga", "niebla mental"],
    "Ansiedad generalizada": ["ansiedad", "estrés", "insomnio", "palpitaciones", "dificultad para respirar"],
    "Fatiga emocional": ["apatía", "fatiga", "estrés", "tristeza"],
    "Sinusitis": ["dolor de cabeza", "congestión nasal", "fiebre", "ojos irritados"],
    "Migraña": ["dolor de cabeza", "náuseas", "visión borrosa", "fatiga"],
    "Otitis": ["dolor de oídos", "fiebre", "mareo"],
    "Reflujo gástrico": ["reflujo", "dolor estomacal", "náuseas"],
    "Infección estomacal": ["diarrea", "dolor estomacal", "náuseas", "vómitos", "fiebre"],
    "Insomnio crónico": ["insomnio", "niebla mental", "fatiga", "estrés"],
    "Trastorno de ansiedad": ["ansiedad", "palpitaciones", "insomnio", "estrés"],
    "Síndrome de burnout": ["fatiga", "apatía", "estrés", "tristeza", "niebla mental"],
}

# Recomendaciones
recomendaciones = {
    "Gripe": ["Descansa bien", "Toma líquidos calientes", "Evita cambios bruscos de temperatura"],
    "Resfriado común": ["Toma infusiones naturales", "Mantente hidratado", "Usa pañuelos limpios"],
    "COVID-19": ["Aíslate", "Consulta al médico", "Monitorea tu oxígeno"],
    "Gastritis por ansiedad": ["Evita café y picante", "Relájate con respiración", "Come en horarios regulares"],
    "Estrés crónico": ["Haz pausas activas", "Medita 10 min al día", "Consulta si persiste"],
    "Depresión": ["Habla con alguien de confianza", "Haz actividad física suave", "Consulta a un psicólogo"],
    "Ansiedad generalizada": ["Haz ejercicios de respiración", "Evita estimulantes", "Busca ayuda emocional"],
    "Fatiga emocional": ["Descansa", "Realiza actividades agradables", "No te sobrecargues de trabajo"],
    "Sinusitis": ["Haz vaporizaciones", "Usa solución salina nasal", "Consulta si el dolor es fuerte"],
    "Migraña": ["Evita luces fuertes", "Descansa en lugar oscuro", "Consulta si es frecuente"],
    "Otitis": ["Evita mojar los oídos", "Consulta al médico", "Aplica calor local con cuidado"],
    "Reflujo gástrico": ["Evita acostarte después de comer", "Come porciones pequeñas", "Evita grasas y ácidos"],
    "Infección estomacal": ["Toma suero oral", "Evita lácteos", "Consulta si hay fiebre persistente"],
    "Insomnio crónico": ["Evita pantallas antes de dormir", "Haz rutina nocturna relajante", "Consulta si persiste"],
    "Trastorno de ansiedad": ["Practica mindfulness", "Habla con un especialista", "Evita situaciones de tensión innecesaria"],
    "Síndrome de burnout": ["Toma tiempo libre", "Organiza tu carga laboral", "Busca apoyo psicológico"],
}

# Procesar texto a síntomas
def procesar_sintomas(texto):
    sintomas_detectados = []
    texto = texto.lower()
    for frase, sintoma in frases_a_sintomas.items():
        if frase in texto:
            sintomas_detectados.append(sintoma)
    return list(set(sintomas_detectados))

# Diagnóstico
def diagnosticar(sintomas_usuario):
    resultados = {}
    for enfermedad, sintomas in enfermedades.items():
        coincidencias = set(sintomas_usuario) & set(sintomas)
        probabilidad = len(coincidencias) / len(sintomas)
        if probabilidad > 0:
            resultados[enfermedad] = round(probabilidad * 100, 2)
    resultados_ordenados = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))
    return dict(list(resultados_ordenados.items())[:4])

# Interfaz
st.title("🧠 IA de Diagnóstico Emocional y Físico")

entrada = st.text_area("Escribe cómo te sientes o tus síntomas físicos/emocionales (ej: tengo fiebre y no puedo dormir):")

if st.button("Diagnosticar"):
    sintomas_usuario = procesar_sintomas(entrada)
    if sintomas_usuario:
        st.success(f"Síntomas detectados: {', '.join(sintomas_usuario)}")
        resultados = diagnosticar(sintomas_usuario)
        if resultados:
            enf_principal = next(iter(resultados))
            st.subheader("🩺 Posibles enfermedades:")
            for enf, prob in resultados.items():
                st.markdown(f"**{enf}** — {prob}%")
            st.subheader(f"💡 Recomendaciones para: {enf_principal}")
            for rec in recomendaciones.get(enf_principal, ["Consulta a un especialista."]):
                st.markdown(f"- {rec}")
        else:
            st.warning("No se encontró ninguna enfermedad coincidente.")
    else:
        st.warning("No se detectaron síntomas reconocibles. Intenta usar otras palabras.")

st.markdown("---")
st.caption("Creado por Rafah Gondola, Adrián Abadia y Guillermo Sánchez")
