# notifications/email_alert.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_report(filepath, jobs):
    user = os.getenv("EMAIL_USER")
    passwd = os.getenv("EMAIL_PASS")
    to = os.getenv("RECEIVER_EMAIL")

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = f"[وظائف اليوم] {len(jobs)} وظيفة متاحة في مجال التثقيف الصحي"

    part = MIMEBase('application', "octet-stream")
    with open(filepath, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filepath}"')
    msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, passwd)
    server.send_message(msg)
    server.quit()
