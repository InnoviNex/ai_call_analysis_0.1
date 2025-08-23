# AI Call Analysis - 1er Prototipo

Esta app permite analizar las llamadas de un centro de contacto, ayudando al sector de auditoría a automatizar y optimizar tareas repetitivas.

## 🚀 Características principales

- Transcripción automática de llamadas.
- Análisis de contenido y métricas clave.
- Ayuda en la detección de patrones en llamadas.
- Optimización de procesos de auditoría manual.
- Preparado para integrar mejoras de IA en futuras versiones.

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Whisper (OpenAI)
- Pandas
- Matplotlib
- PyInstaller (para versión ejecutable)

## 🛆 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/InnoviNex/ai_call_analysis_0.1.git
cd ai_call_analysis_0.1
```

2. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

3. Activar el entorno virtual:

- En Windows:

```bash
.\venv\Scripts\activate
```

- En Linux/Mac:

```bash
source venv/bin/activate
```

4. Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 🌟 Uso

### CLI

1. Ejecutar la aplicación principal:

```bash
python src/main.py
```

2. Seguir las instrucciones en pantalla para cargar archivos de audio y analizar llamadas.

### Servidor web

1. Levantar el servidor:

```bash
uvicorn web.app:app --reload
```

2. Endpoints disponibles:

- `POST /analizar`: enviar un archivo de audio en el campo `audio` y recibir la transcripción y el análisis.
- `GET /reportes/{nombre}`: descargar un reporte generado en `data/reportes`.

---

## 📊 Estado del Proyecto

🚧 **1er Prototipo en desarrollo.**  
Se encuentra en una etapa funcional inicial, en proceso de mejoras de rendimiento, interfaz gráfica y reportes automáticos.

---

## 🤝 Contribuciones

Actualmente este proyecto está siendo desarrollado internamente.  
En el futuro se abrirán invitaciones para colaboración.

---

## 📝 Licencia

Copyright (c) 2025 Nicolás Busto Gatti (InnoviNex).  
Todos los derechos reservados.  
Este software es de uso privado y no está autorizado su uso, copia, modificación ni distribución sin el consentimiento expreso del autor.

---

## ✉️ Contacto

- **Autor:** Nicolás Busto Gatti (InnoviNex)
- **Correo:** nicolassbusto1@gmail.com

---

