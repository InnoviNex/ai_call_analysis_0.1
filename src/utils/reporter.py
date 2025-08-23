import os
from datetime import datetime


def guardar_reporte(nombre_audio, transcripcion, analisis, comentario_auditor):
    os.makedirs("data/reportes", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_reporte = f"reporte_{timestamp}.txt"
    ruta = os.path.join("data/reportes", nombre_reporte)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"🧾 Reporte de llamada: {nombre_audio}\n")
        f.write("=" * 50 + "\n\n")
        f.write("📝 Transcripción:\n")
        f.write(transcripcion + "\n\n")
        f.write("📊 Análisis IA:\n")
        f.write(analisis + "\n\n")
        f.write("🧑‍💼 Comentario del auditor:\n")
        f.write((comentario_auditor or "Sin comentario.") + "\n")

    print(f"📁 Reporte guardado en: {ruta}")
