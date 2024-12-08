import os
import random
import requests
from google.cloud import vision

# Configuración de credenciales para Google Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\010111010\python\bot- telegram\archivo-json\proyecto-telegram-442023-827aca6433ca.json"

# Inicializa el cliente de Google Vision
client = vision.ImageAnnotatorClient()

# Configuración del bot de Telegram
TOKEN_BOT = '8048656094:AAG6n5ZhE9ptTy_QSbuq3MSJxDejiAmBIuc'
CHAT_ID = '-1002248531793'
CARPETA_ARCHIVOS = r"D:\010111010\algo\de nuevo\imagenes probidia"

# Función para analizar una imagen con Google Vision
def analizar_imagen(ruta_imagen):
    """Usa Google Vision para analizar la imagen y generar etiquetas."""
    print(f"Analizando la imagen: {ruta_imagen}")
    with open(ruta_imagen, 'rb') as imagen:
        contenido = imagen.read()

    image = vision.Image(content=contenido)
    response = client.label_detection(image=image)

    if response.error.message:
        print("Error al analizar la imagen:", response.error.message)
        return ["Contenido exclusivo 🔥"]

    etiquetas = [label.description for label in response.label_annotations[:5]]
    print(f"Etiquetas detectadas: {etiquetas}")
    return etiquetas

# Función para generar descripciones atrevidas basadas en etiquetas
def generar_descripcion_atrevida(etiquetas, es_video=False):
    """
    Genera una descripción atrevida y provocativa basada en las etiquetas de la imagen o video.
    """
    tipo_contenido = "🔥 este video caliente" if es_video else "💋 esta imagen provocativa"
    
    # Frases iniciales
    introducciones = [
        "😈 No podrás resistirte a lo que estás a punto de ver:",
        "🔥 Este contenido viene con una advertencia: demasiado candente para ignorarlo.",
        "💋 Te presentamos algo exclusivo para encender tus sentidos:",
        "🌶️ Prepárate para subir la temperatura con:",
        "❤️ ¿Listo para perder el control con:"
    ]
    
    # Frases intermedias con etiquetas
    cuerpo = [
        f"Un toque de {', '.join(etiquetas)} para hacer que todo sea aún más irresistible.",
        f"Con detalles de {', '.join(etiquetas)}, sabemos que no podrás apartar la mirada.",
        f"Un juego perfecto entre {', '.join(etiquetas)}, pensado solo para ti.",
        f"Inspirado en {', '.join(etiquetas)}, porque sabemos lo que deseas."
    ]
    
    # Frases finales
    cierres = [
        "💋 ¿Te atreves a más?",
        "🔥 Esto es solo una probadita de lo que viene.",
        "❤️ Deja que esto despierte todos tus sentidos.",
        "😈 Solo los valientes se atreven a continuar.",
        "🌶️ ¿Preparado para el próximo nivel?"
    ]
    
    # Construcción de la descripción
    descripcion = f"{random.choice(introducciones)} {random.choice(cuerpo)} {random.choice(cierres)}"
    
    # Añadir el tipo de contenido al final
    descripcion_final = f"{descripcion}\n👉 Disfruta {tipo_contenido} y déjame saber qué opinas. 😘"
    return descripcion_final

# Función para elegir un archivo al azar
def elegir_archivo_azar(carpeta, archivos_usados):
    """Selecciona un archivo aleatorio que no haya sido usado."""
    archivos = [f for f in os.listdir(carpeta) if f.endswith(('jpg', 'jpeg', 'png', 'gif', 'mp4'))]
    archivos_no_usados = [f for f in archivos if f not in archivos_usados]
    if archivos_no_usados:
        archivo_aleatorio = random.choice(archivos_no_usados)
        return os.path.join(carpeta, archivo_aleatorio)
    else:
        print("No hay archivos disponibles.")
        return None

# Función para enviar mensajes a Telegram
def enviar_mensaje_telegram(token_bot, chat_id, ruta_archivo, descripcion):
    """Envía un archivo multimedia a Telegram con una descripción generada."""
    url = f"https://api.telegram.org/bot{token_bot}/sendPhoto" if ruta_archivo.endswith(('jpg', 'jpeg', 'png', 'gif')) else f"https://api.telegram.org/bot{token_bot}/sendVideo"
    
    print(f"Enviando archivo a Telegram: {ruta_archivo}")
    with open(ruta_archivo, 'rb') as archivo:
        archivos = {'photo' if ruta_archivo.endswith(('jpg', 'jpeg', 'png', 'gif')) else 'video': archivo}
        datos = {'chat_id': chat_id, 'caption': descripcion}
        respuesta = requests.post(url, data=datos, files=archivos)
        if respuesta.status_code == 200:
            print("Mensaje enviado correctamente a Telegram.")
        else:
            print("Error al enviar el mensaje a Telegram:", respuesta.text)

# Función principal del bot
def bot_telegram():
    print("Iniciando bot de Telegram...")
    archivos_usados = set()
    mensajes_enviados = 0  # Contador de mensajes enviados

    while mensajes_enviados < 2:  # Límite de mensajes a enviar
        archivo = elegir_archivo_azar(CARPETA_ARCHIVOS, archivos_usados)
        if archivo:
            print(f"Archivo seleccionado: {archivo}")
            es_video = archivo.endswith(('mp4',))
            etiquetas = analizar_imagen(archivo)
            descripcion = generar_descripcion_atrevida(etiquetas, es_video)
            enviar_mensaje_telegram(TOKEN_BOT, CHAT_ID, archivo, descripcion)
            archivos_usados.add(os.path.basename(archivo))
            mensajes_enviados += 1  # Incrementa el contador de mensajes enviados
        else:
            print("No hay archivos disponibles para enviar.")
            break

# Ejecutar el bot
if __name__ == "__main__":
    bot_telegram()

