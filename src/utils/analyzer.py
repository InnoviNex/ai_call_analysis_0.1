from openai import OpenAI
from config.settings import OPENAI_API_KEY
from utils.logger import log_info, log_error

client = OpenAI(api_key=OPENAI_API_KEY)

def analizar_transcripcion(texto_transcripto):
    prompt = (
        "Analiza esta conversación entre un agente de atención al cliente y un cliente.\n"
        "Devuelve el tono general de la conversación (neutral, positivo, negativo) con un emoji.\n"
        "Incluí también una breve explicación del motivo y sugerencias para mejorar.\n"
        f"A continuación la transcripción:\n\n{texto_transcripto}"
    )
    try:
        log_info("📊 Analizando tono de la conversación...")
        respuesta = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        analisis = respuesta.choices[0].message.content
        log_info("✅ Análisis completado.")
        return analisis
    except Exception as e:
        log_error(f"❌ Error al analizar: {e}")
        return None