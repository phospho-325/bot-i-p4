Proyecto: Bot de Telegram con Análisis de Imágenes usando Google Vision API

Este proyecto es un bot de Telegram que selecciona imágenes aleatorias de una carpeta, las analiza utilizando Google Vision API y genera descripciones provocativas basadas en las etiquetas detectadas. Posteriormente, envía estas imágenes (o videos) con sus descripciones al chat de Telegram configurado.

Características Principales

Análisis de Imágenes: Utiliza Google Vision API para identificar etiquetas en imágenes seleccionadas.

Descripciones Personalizadas: Genera descripciones atrevidas y creativas basadas en las etiquetas detectadas.

Envío Automático: Envía imágenes y videos directamente a un chat de Telegram.

Selección Aleatoria: Escoge un archivo aleatorio de una carpeta y asegura que no se repita.

Integración con Google Vision y Telegram: Combina el poder de Google Vision API con la API de Telegram para automatizar el proceso.

Requisitos del Sistema

Sistema Operativo: Compatible con Windows, macOS o Linux.

Python: Versión 3.7 o superior.

Librerías Python:

google-cloud-vision

requests

Instalación

Instala Python: Asegúrate de tener Python instalado en tu sistema. Descárgalo desde python.org.

Configura el entorno virtual (opcional):

python -m venv venv
source venv/bin/activate  # En Linux/MacOS
venv\Scripts\activate  # En Windows

Instala las dependencias:

pip install google-cloud-vision requests

Configura las credenciales de Google Vision API:

Descarga tu archivo de credenciales JSON desde la consola de Google Cloud Platform.

Coloca el archivo en la ruta indicada en el código:

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"ruta/a/tu/archivo.json"

Configura el bot de Telegram:

Obtén el token del bot desde BotFather.

Configura el ID del chat de Telegram.

Uso

Configura la carpeta de archivos:

Define la ruta a la carpeta que contiene las imágenes y videos en la variable CARPETA_ARCHIVOS.

Ejecuta el bot:

Abre una terminal en el directorio del script y ejecuta:

python bot_telegram.py

Interacción:

El bot seleccionará un archivo aleatorio, generará una descripción y lo enviará al chat configurado en Telegram.

Estructura del Código

1. analizar_imagen(ruta_imagen)

Propósito: Analiza una imagen usando Google Vision API y genera una lista de etiquetas.

Detalles:

Lee el archivo de imagen.

Llama a la API de Google Vision para detectar etiquetas.

Retorna las etiquetas más relevantes.

2. generar_descripcion_atrevida(etiquetas, es_video)

Propósito: Genera una descripción provocativa basada en las etiquetas detectadas.

Detalles:

Utiliza frases personalizadas para crear descripciones atractivas.

Adapta el texto según si es una imagen o un video.

3. elegir_archivo_azar(carpeta, archivos_usados)

Propósito: Selecciona un archivo aleatorio que no haya sido usado previamente.

Detalles:

Filtra archivos válidos (imágenes y videos).

Asegura que los archivos seleccionados no se repitan.

4. enviar_mensaje_telegram(token_bot, chat_id, ruta_archivo, descripcion)

Propósito: Envía un archivo multimedia con una descripción al chat de Telegram.

Detalles:

Usa la API de Telegram para enviar fotos o videos.

Incluye la descripción generada en el mensaje.

5. bot_telegram()

Propósito: Función principal que coordina el flujo completo del bot.

Detalles:

Selecciona archivos al azar.

Genera descripciones basadas en etiquetas.

Envía los archivos con las descripciones al chat de Telegram.

Personalización

Extensiones Válidas: Puedes ajustar las extensiones permitidas para los archivos en el filtro de elegir_archivo_azar.

Cantidad de Mensajes: Modifica el límite de mensajes enviados cambiando el valor de mensajes_enviados en bot_telegram.

Notas Importantes

Configuración de Google Vision API: Asegúrate de que las credenciales JSON estén correctamente configuradas.

Errores de Telegram: Verifica el token del bot y el ID del chat si encuentras problemas al enviar mensajes.

Archivos Repetidos: Si necesitas evitar repeticiones entre ejecuciones, puedes almacenar los archivos usados en un archivo temporal.
