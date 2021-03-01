import smtplib, ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailer:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.receiver_email = self.config['USER']['email_reciever']
        self.cutomMessage = self.config['USER']['message']


    def send(self):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "DeTeDichtOMeter@gmail.com"
        password = "JeBentTeDicht123"
        message = MIMEMultipart("alternative")
        message["Subject"] = "Detect-O-Alert"
        message["From"] = sender_email
        message["To"] = self.receiver_email


        text = """\
            unusual amount of violations detected
            """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        html = """\
        <html>
        <body>
            <p>This is an automated message,
            <br>
            <br>
            """ +self.cutomMessage +"""
            </p>
        </body>
        </html>
        """

        
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, self.receiver_email, message.as_string()
            ) 

            
mailer = Mailer()
mailer.send()