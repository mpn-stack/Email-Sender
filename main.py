from http import server
import smtplib
from email.message import EmailMessage


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mpninfomail@gmail.com'
EMAIL_PORT_SSL = 465
EMAIL_HOST_PASSWORD=''

msg = EmailMessage()
msg['Subject']='Python email test'
msg['From']=EMAIL_HOST_USER
msg['To']='pakniat.mahmoud@gmail.com'
msg.set_content('This is a message body')

with open('log.png', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype='png', filename = file_name)

with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as Server:
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.send_message(msg)
