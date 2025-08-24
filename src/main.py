 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/src/main.py b/src/main.py
index 07149990ffda425cfad80f09034056ce45a7bc9e..0a7b00027845accf591bf82a4c6a7fdd6a08d33b 100644
--- a/src/main.py
+++ b/src/main.py
@@ -1,40 +1,40 @@
 import sys
 import os
 sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
 
-from utils.licencia_online import validar_licencia_online, registrar_uso_en_hoja
+from utils.licencia_online import (
+    obtener_cliente_id,
+    validar_licencia_online,
+    registrar_uso_en_hoja,
+)
 from utils.transcriber import transcribir_audio
 from utils.analyzer import analizar_transcripcion
 from utils.reporter import guardar_reporte
 
-def leer_cliente_id():
-    with open("data/licencia/cliente_id.txt", "r") as f:
-        return f.read().strip()
-
 RUTA_AUDIO = "data/llamadas/llamada_cliente.mp3"
 
 def main():
-    cliente_id = leer_cliente_id()
-    valido, mensaje = validar_licencia_online()
+    cliente_id = obtener_cliente_id()
+    valido, mensaje = validar_licencia_online(cliente_id)
     if not valido:
         print(f"❌ {mensaje}")
         registrar_uso_en_hoja(cliente_id, mensaje, RUTA_AUDIO)
         return
 
     print("✅ Licencia válida. Ejecutando sistema...")
 
     transcripcion = transcribir_audio(RUTA_AUDIO)
     if transcripcion:
         print("\n📝 Transcripción:")
         print(transcripcion)
 
         analisis = analizar_transcripcion(transcripcion)
         print("\n📈 Análisis del tono:")
         print(analisis)
 
         comentario = input("\n🧑‍💼 Comentario del auditor (Enter para omitir):\n> ")
         guardar_reporte(RUTA_AUDIO, transcripcion, analisis, comentario)
         registrar_uso_en_hoja(cliente_id, "Licencia válida", RUTA_AUDIO)
 
 if __name__ == "__main__":
-    main()
+    main()
 
EOF
)
