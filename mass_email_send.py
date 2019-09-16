import smtplib


def send_mail(subject,body):
    rcv_mail = ['reciever1@gmail.com','reciever2@gmail.com']
    smtp_port = 587
    smtp_server = "smtp.gmail.com"
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sender_mail@gmail.com', 'mailpassword')  ## Sender Email Address and password
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sender_mail@gmail.com', rcv_mail, msg) ## Sender Email Address , reciver email address can be a array of email address,and message
    print("Email Has been sent to "+rcv_mail)

    server.quit()


print("Executing send mail function")
sub = input("Please enter the Subject of the Mail : ")
mail_body = input("Please enter body of the Mail : ")
send_mail(mail,sub,mail_body)
