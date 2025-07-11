import streamlit as st

st.set_page_config(page_title="Diagnóstico IA", layout="centered")

# 🧠 Frases comunes -> síntomas clave (muy ampliado)
frases_a_sintomas = {
    "dolor de cabeza": "dolor de cabeza", "me duele la cabeza": "dolor de cabeza", "presión en la cabeza": "dolor de cabeza",
    "fiebre": "fiebre", "temperatura alta": "fiebre", "me siento caliente": "fiebre",
    "escalofríos": "escalofríos", "tiritando": "escalofríos",
    "dolor muscular": "dolores musculares", "me duele el cuerpo": "dolores musculares",
    "no puedo dormir": "insomnio", "duermo mal": "insomnio", "me despierto en la noche": "insomnio",
    "cansancio": "fatiga", "estoy cansado": "fatiga", "me siento agotado": "fatiga", "debilidad": "fatiga",
    "tos seca": "tos seca", "tengo tos seca": "tos seca",
    "tos con flema": "tos con flema", "flema": "tos con flema",
    "nariz tapada": "congestión nasal", "mocos": "congestión nasal", "goteo nasal": "congestión nasal",
    "me duele la garganta": "dolor de garganta", "ardor en la garganta": "dolor de garganta",
    "me cuesta respirar": "dificultad para respirar", "no respiro bien": "dificultad para respirar",
    "náuseas": "náuseas", "ganas de vomitar": "náuseas",
    "vómito": "vómitos", "vomité": "vómitos",
    "diarrea": "diarrea", "evacuaciones líquidas": "diarrea",
    "dolor de estómago": "dolor estomacal", "malestar estomacal": "dolor estomacal", "retorcijones": "dolor estomacal",
    "acidez": "reflujo", "reflujo": "reflujo",
    "me siento triste": "depresión", "tristeza": "depresión",
    "nervioso": "ansiedad", "ansioso": "ansiedad", "ataques de pánico": "ansiedad",
    "estresado": "estrés",
    "visión borrosa": "visión borrosa",
    "ojos rojos": "irritación ocular",
    "picazón en los ojos": "alergia ocular", "ojos llorosos": "alergia ocular",
    "dolor en los oídos": "dolor de oído", "zumbido en los oídos": "dolor de oído",
    "palpitaciones": "taquicardia", "latidos rápidos": "taquicardia",
    "mareo": "mareo", "me siento mareado": "mareo",
    "pérdida del olfato": "anosmia", "no huelo nada": "anosmia",
    "dolor lumbar": "dolor de espalda", "me duele la espalda baja": "dolor de espalda"
}

# 😷 Enfermedades y sus síntomas
enfermedades = {
    "Gripe": ["fiebre", "dolor de cabeza", "dolores musculares", "fatiga", "tos seca", "escalofríos"],
    "COVID-19": ["fiebre", "tos seca", "dificultad para respirar", "dolores musculares", "fatiga", "dolor de garganta", "anosmia"],
    "Resfriado común": ["congestión nasal", "tos seca", "dolor de garganta", "fiebre", "fatiga"],
    "Sinusitis": ["dolor de cabeza", "congestión nasal", "fiebre", "dolor de garganta"],
    "Gastritis": ["dolor estomacal", "náuseas", "vómitos", "reflujo"],
    "Migraña": ["dolor de cabeza", "náuseas", "mareo", "visión borrosa", "fatiga"],
    "Ansiedad": ["ansiedad", "insomnio", "mareo", "dificultad para respirar", "taquicardia"],
    "Depresión": ["depresión", "apatía", "insomnio", "fatiga"],
    "Insomnio": ["insomnio", "fatiga", "ansiedad"],
    "Estrés": ["estrés", "fatiga", "dolor de cabeza", "insomnio"],
    "Neumonía": ["fiebre", "tos con flema", "dolor en el pecho", "dificultad para respirar", "fatiga"],
    "Gastroenteritis": ["diarrea", "náuseas", "vómitos", "dolor estomacal", "fiebre"],
    "Alergia respiratoria": ["tos seca", "congestión nasal", "picazón en los ojos", "fatiga"],
    "Otitis": ["dolor de oído", "fiebre", "zumbido en los oídos"],
    "Conjuntivitis": ["ojos rojos", "picazón en los ojos"],
    "Lumbalgia": ["dolor de espalda", "fatiga", "dolores musculares"]
}

# ✅ Recomendaciones por enfermedad
recomendaciones = {
    "Gripe": ["Descansa", "Toma líquidos calientes", "Evita el frío"],
    "COVID-19": ["Aíslate", "Consulta al médico", "Hidrátate bien"],
    "Resfriado común": ["Toma infusiones", "Descansa", "Ventila tu habitación"],
    "Sinusitis": ["Haz vaporizaciones", "Bebe agua", "Consulta si no mejora"],
    "Gastritis": ["Evita comidas irritantes", "No bebas alcohol", "Consulta si persiste"],
    "Migraña": ["Evita luces fuertes", "Descansa en silencio", "Toma analgésicos recomendados"],
    "Ansiedad": ["Respira profundo", "Evita café", "Haz ejercicio ligero"],
    "Depresión": ["Busca apoyo", "Haz ejercicio", "Consulta a un psicólogo"],
    "Insomnio": ["Crea una rutina nocturna", "Apaga pantallas", "Evita cafeína"],
    "Estrés": ["Haz pausas activas", "Respira hondo", "Habla con alguien"],
    "Neumonía": ["Consulta al médico", "Toma medicamentos", "Descansa bien"],
    "Gastroenteritis": ["Bebe suero oral", "Evita comidas pesadas", "Consulta si se prolonga"],
    "Alergia respiratoria": ["Evita alérgenos", "Usa antihistamínicos", "Limpia bien tu entorno"],
    "Otitis": ["Consulta al médico", "No mojes el oído", "Toma analgésicos"],
    "Conjuntivitis": ["Evita tocarte los ojos", "Lava tus manos", "Consulta si hay secreción"],
    "Lumbalgia": ["Aplica calor local", "Evita esfuerzos", "Consulta si persiste"]
}

def procesar_sintomas(texto):
    sintomas_detectados = []
    texto = texto.lower()
    for frase, sintoma in frases_a_sintomas.items():
        if frase in texto:
            sintomas_detectados.append(sintoma)
    return list(set(sintomas_detectados))

def diagnosticar(sintomas_usuario):
    resultados = {}
    for enfermedad, sintomas in enfermedades.items():
        coincidencias = set(sintomas_usuario) & set(sintomas)
        probabilidad = len(coincidencias) / len(sintomas)
        if probabilidad > 0:
            resultados[enfermedad] = round(probabilidad * 100, 2)
    resultados_ordenados = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))
    top5 = dict(list(resultados_ordenados.items())[:5])
    return top5

st.title("🤖 IA de Diagnóstico de Enfermedades")
entrada = st.text_area("Describe tus síntomas lo más naturalmente posible:")

if st.button("Diagnosticar"):
    sintomas_usuario = procesar_sintomas(entrada)
    if sintomas_usuario:
        st.success(f"🩺 Síntomas detectados: {', '.join(sintomas_usuario)}")
        resultados = diagnosticar(sintomas_usuario)
        if resultados:
            enfermedad_principal = next(iter(resultados))
            st.subheader("🔎 Enfermedades probables:")
            for enf, prob in resultados.items():
                st.write(f"**{enf}** — {prob}%")
            st.subheader(f"💡 Recomendaciones para: {enfermedad_principal}")
            for rec in recomendaciones.get(enfermedad_principal, ["Consulta a un profesional."]):
                st.markdown(f"- {rec}")
        else:
            st.warning("No se pudo determinar una enfermedad probable.")
    else:
        st.warning("No se detectaron síntomas conocidos. Intenta describirlo de otra forma.")

st.markdown("---")
st.caption("Creado por Rafah Gondola, Adrián Abadia y Guillermo Sánchez")
