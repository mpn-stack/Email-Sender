from http import server
import smtplib
from email.message import EmailMessage
'''
    sending email using python
'''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'Yor_Email_Address@gmail.com'
EMAIL_PORT_SSL = 465
EMAIL_HOST_PASSWORD='replace with your app password' """ Example : clluqiscfeduglpq"""

msg = EmailMessage()
msg['Subject']='Python Test'
msg['From']=EMAIL_HOST_USER
msg['To']='mpn_info@yahoo.com'
msg.set_content('This is a message body for test!')

with open('AttachmentFileName', 'rb') as f:
    file_data = f.read()
    file_name = f.name

''' change maintype and subtype for other attachment file except jpg '''
msg.add_attachment(file_data, maintype='image', subtype='jpg', filename = file_name)

with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
    try:
        server.login (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        print('your email has been sent')
    except:
        print('Failed to send email')
