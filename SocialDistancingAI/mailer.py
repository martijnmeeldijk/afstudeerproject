import smtplib, ssl

class Mailer:
    global reciever
    def __init__(self, reciever):
        receiver_email = reciever

    def send(self):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "DeTeDichtOMeter@gmail.com"
        password = "JeBentTeDicht123"
        message = """\
        Subject: EWA

        TE DICHT OMG GA VERDER UIT ELKAAR!!"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)