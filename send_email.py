import smtplib, ssl
from email.message import EmailMessage
from dotenv import load_dotenv  # Import the loader
import os 

def send_email(message):

    load_dotenv()

    host = os.getenv("SMTP_HOST")
    port = os.getenv("SMTP_PORT")

    username = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_EMAIL_PASSWORD")

    context = ssl.create_default_context()

    msg = EmailMessage()
    msg["Subject"] = "Todays News"
    msg["From"] = os.getenv("SENDER_EMAIL")
    msg["To"] = os.getenv("RECIPENT_EMAIL")

    msg.set_content(message, charset="utf-8")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        
        server.login(username, password)
        server.send_message(msg)
        
if __name__ == "__main__":
    send_email("Hello, how are you?")
