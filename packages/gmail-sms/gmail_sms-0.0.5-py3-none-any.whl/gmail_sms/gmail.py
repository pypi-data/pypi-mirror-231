import smtplib

def send_message(gmail_user,gmail_app_password,recipient, subject, body ,exception=False):

    sent_from = gmail_user
    sent_to = recipient if isinstance(recipient, list) else [recipient]

    message = """From: {}\nTo: {}\nSubject: {}\n\n{}
    """.format(sent_from, ", ".join(sent_to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, message)
        server.close()

        print('Email sent!')
    except Exception as ex:
        if exception:
           raise ex
        print("Error: {}!\n\n" .format(ex))

