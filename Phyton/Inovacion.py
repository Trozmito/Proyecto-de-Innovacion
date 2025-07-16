import streamlit as st

st.set_page_config(page_title="IA Diagnóstica", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #1c1c1c;
            color: white;
        }
        .stTextInput > div > div > input {
            color: white;
            background-color: #2e2e2e;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 IA Diagnóstica de Salud")
st.write("Escribe cómo te sientes y trataré de ayudarte 😊")

# Frases comunes que se traducen a síntomas
frases_a_sintomas = {
    "me duele la cabeza": "dolor de cabeza",
    "tengo fiebre": "fiebre",
    "tengo tos": "tos",
    "me duele la garganta": "dolor de garganta",
    "tengo mocos": "congestión nasal",
    "me siento mareado": "mareo",
    "vomité": "vómito",
    "tengo diarrea": "diarrea",
    "me duele el estómago": "dolor abdominal",
    "me duele el pecho": "dolor en el pecho",
    "no puedo respirar bien": "dificultad para respirar",
    "tengo escalofríos": "escalofríos",
    "me duele la espalda": "dolor de espalda",
    "tengo visión borrosa": "visión borrosa",
    "me cuesta caminar": "dificultad para caminar",
    "me arden los ojos": "ardor ocular",
    "me pica la piel": "picazón",
    "tengo manchas en la piel": "erupción",
    "me cuesta tragar": "dificultad para tragar",
    "tengo palpitaciones": "palpitaciones",
    "sudo demasiado": "sudoración excesiva",
    "no puedo dormir": "insomnio",
    "me siento triste": "tristeza",
    "tengo ansiedad": "ansiedad",
    "me siento vacío": "apatía",
    "lloro sin razón": "llanto frecuente",
    "siento culpa": "culpa",
    "me siento desconectado": "despersonalización",
    "tengo pensamientos negativos": "pensamientos negativos",
    "me tiemblan las manos": "temblores",
    "me siento inútil": "baja autoestima",
    "me da miedo salir": "agorafobia",
    "me siento estresado": "estrés",
    "siento presión en la cabeza": "presión en la cabeza",
    "me duele el cuello": "dolor de cuello",
    "me duele el oído": "dolor de oído",
    "me rasco mucho": "picazón",
    "me siento confundido": "confusión mental",
    "me siento solo": "soledad",
    "me siento vigilado": "paranoia",
    "no quiero ver a nadie": "aislamiento"
}

enfermedades = {
    "gripe": ["fiebre", "tos", "dolor de garganta", "dolor muscular", "escalofríos"],
    "resfriado común": ["congestión nasal", "tos", "dolor de garganta"],
    "covid-19": ["fiebre", "tos", "dificultad para respirar", "dolor muscular", "pérdida del olfato"],
    "sinusitis": ["dolor de cabeza", "presión en la cabeza", "congestión nasal"],
    "asma": ["dificultad para respirar", "tos", "sibilancias"],
    "gastritis": ["dolor abdominal", "náuseas", "vómito"],
    "ansiedad": ["ansiedad", "nerviosismo", "temblores", "insomnio"],
    "depresión": ["tristeza", "apatía", "insomnio", "baja autoestima"],
    "hipertiroidismo": ["palpitaciones", "sudoración excesiva", "ansiedad"],
    "hipotiroidismo": ["fatiga", "depresión", "frío constante"]
}

recomendaciones = {
    "gripe": "Descansa, toma líquidos y medicamentos para la fiebre si es necesario.",
    "resfriado común": "Mantente hidratado, usa descongestionantes y descansa.",
    "covid-19": "Aíslate y consulta a un médico si tienes dificultad para respirar.",
    "sinusitis": "Haz inhalaciones de vapor y mantente hidratado.",
    "asma": "Evita alérgenos y lleva contigo tu inhalador.",
    "gastritis": "Evita comidas irritantes y consulta a tu médico.",
    "ansiedad": "Respira profundo, realiza ejercicios relajantes y busca ayuda profesional.",
    "depresión": "Habla con un terapeuta, mantén rutinas saludables.",
    "hipertiroidismo": "Consulta a un endocrinólogo para tratamiento.",
    "hipotiroidismo": "Sigue tu tratamiento hormonal prescrito."
}

def diagnosticar(frase_usuario):
    sintomas_detectados = set()
    for frase, sintoma in frases_a_sintomas.items():
        if frase in frase_usuario.lower():
            sintomas_detectados.add(sintoma)

    puntajes = {}
    for enfermedad, sintomas in enfermedades.items():
        coincidencias = len(set(sintomas) & sintomas_detectados)
        if coincidencias > 0:
            puntajes[enfermedad] = coincidencias / len(sintomas)

    if not puntajes:
        return "❌ No se detectaron enfermedades compatibles con los síntomas ingresados."

    enfermedad_probable = max(puntajes, key=puntajes.get)
    porcentaje = puntajes[enfermedad_probable] * 100
    recomendacion = recomendaciones.get(enfermedad_probable, "Consulta a un especialista.")

    resultado = f"✅ **Diagnóstico más probable:** *{enfermedad_probable.upper()}* ({porcentaje:.1f}%)\n\n"
    resultado += f"💡 **Recomendación:** {recomendacion}\n\n"
    resultado += "**Otros posibles diagnósticos:**\n"
    for enf, score in sorted(puntajes.items(), key=lambda x: x[1], reverse=True):
        if enf != enfermedad_probable:
            resultado += f"- {enf} ({score*100:.1f}%)\n"
    return resultado

# Interfaz con el usuario
entrada = st.text_input("📝 ¿Qué síntomas tienes? Describe cómo te sientes:")

if entrada:
    st.markdown(diagnosticar(entrada))

st.markdown("---")
st.markdown("👨‍💻 *Creado por:* **[Tu nombre]**, **Adrián Abadia**, **Guillermo Sánchez**")
