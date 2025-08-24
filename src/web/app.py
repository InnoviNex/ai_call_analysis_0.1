import os
import sys
import uuid

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

# Permitir importar módulos desde "src"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.licencia_online import (
    obtener_cliente_id,
    validar_licencia_online,
    registrar_uso_en_hoja,
)
from utils.transcriber import transcribir_audio
from utils.analyzer import analizar_transcripcion
from utils.reporter import guardar_reporte


app = FastAPI()


@app.post("/analizar")
async def analizar(audio: UploadFile = File(...)):
    cliente_id = obtener_cliente_id()
    valido, mensaje = validar_licencia_online(cliente_id)
    if not valido:
        registrar_uso_en_hoja(cliente_id, mensaje, audio.filename)
        raise HTTPException(status_code=400, detail=mensaje)

    os.makedirs("data/llamadas", exist_ok=True)
    nombre_temp = f"{uuid.uuid4()}_{audio.filename}"
    ruta_audio = os.path.join("data/llamadas", nombre_temp)
    with open(ruta_audio, "wb") as buffer:
        buffer.write(await audio.read())

    transcripcion = transcribir_audio(ruta_audio)
    analisis = analizar_transcripcion(transcripcion) if transcripcion else ""

    guardar_reporte(ruta_audio, transcripcion, analisis, comentario_auditor=None)
    registrar_uso_en_hoja(cliente_id, "Licencia válida", ruta_audio)

    return {"transcripcion": transcripcion, "analisis": analisis}


@app.get("/reportes/{nombre}")
def obtener_reporte(nombre: str):
    ruta = os.path.join("data/reportes", nombre)
    if not os.path.isfile(ruta):
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return FileResponse(ruta)

