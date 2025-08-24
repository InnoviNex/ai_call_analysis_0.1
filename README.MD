(cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.MD b/README.MD
index 045a1799fa34416040970714f0045de5af86755f..3612030c356943875fa012bdbef834ee6859209e 100644
--- a/README.MD
+++ b/README.MD
@@ -33,61 +33,76 @@ cd ai_call_analysis_0.1
 python -m venv venv
 ```
 
 3. Activar el entorno virtual:
 
 - En Windows:
CMD
venv\Scripts\activate.bat
 
 PowerShell 
 .\venv\Scripts\Activate.ps1
 ```
 
 - En Linux/Mac:
 
 gitbash
 source venv/bin/activate
 ```
 
 4. Instalar las dependencias necesarias:
 
 ```bash
 pip install -r requirements.txt
 ```
 
 ---
 
-## 🌟 Uso
-
-1. Ejecutar la aplicación principal:
-
-```bash
-python src/main.py
-```
-
-2. Seguir las instrucciones en pantalla para cargar archivos de audio y analizar llamadas.
-
----
+## 🌟 Uso
+
+### CLI
+
+1. Ejecutar la aplicación principal:
+
+```bash
+python src/main.py
+```
+
+2. Seguir las instrucciones en pantalla para cargar archivos de audio y analizar llamadas.
+
+### Servidor web
+
+1. Levantar el servidor:
+
+```bash
+uvicorn web.app:app --reload
+```
+
+2. Endpoints disponibles:
+
+- `POST /analizar`: enviar un archivo de audio en el campo `audio` y recibir la transcripción y el análisis.
+- `GET /reportes/{nombre}`: descargar un reporte generado en `data/reportes`.
+
+---
 
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
 
 
EOF
)

