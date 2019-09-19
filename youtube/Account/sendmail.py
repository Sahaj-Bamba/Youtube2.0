from .models import Notification
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sahajweb1999@gmail.com"
password = "web@999@"

notify = Notification.objects.all()

for i in notify:
    recipientmail = i.user.email
    message = i.content
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message)
