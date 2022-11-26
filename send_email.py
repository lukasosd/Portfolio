import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()

username = 'emaildotestow0@gmail.com'
password = 'czhuqvftueizunpf'
receiver = 'lukas.gurgul@gmail.com'
message = """Subject: Contact from Portfolio!
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)