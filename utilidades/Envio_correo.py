import smtplib
import ssl
from email.message import EmailMessage
import random
import string
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def enviar_correo_recuperacion_contrasena(destino, contrasena, correo, usuario):
        # Define email sender and receiver
        email_sender = destino
        email_password = contrasena
        email_receiver = correo

        # Set the subject and body of the email
        subject = 'Recuperación de contraseña'
        contrasena = generar_contrasena(random.randrange(10, 22)) 
        body = f"""
        Estimado {usuario},

Hemos recibido una solicitud para restablecer la contraseña de tu cuenta. 
Para completar el proceso, te proporcionamos una nueva contraseña generada automáticamente:

Contraseña temporal: {contrasena}

Si no has solicitado la recuperación de contraseña o crees que esto puede ser un error, 
por favor, ignora este correo electrónico y no realices ninguna acción.

Te recomendamos cambiar esta contraseña temporal tan pronto como accedas a tu cuenta.

¡Gracias y saludos cordiales!

El Equipo de nyquist 
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        return contrasena


