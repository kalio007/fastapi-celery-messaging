from celery import Celery
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

celery = Celery('tasks', broker=os.getenv('CELERY_BROKER_URL'))

@celery.task
def send_mail_task(email: str):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    receiver_email = email
    subject = "Test Email"
    body = "This is a test email."

    message = f"""\
    Subject: {subject}

    {body}"""

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
