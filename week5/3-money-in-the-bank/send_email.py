import smtplib
import getpass


def send_email(email, code):
    # The below code never changes, though obviously those variables need values.
    GMAIL_USERNAME = "nikolaykgeorgiev@gmail.com"
    GMAIL_PASSWORD = getpass.getpass("Enter pass: ")
    email_subject = "password change"
    recipient = email
    body_of_email = "Your new password is {}".format(code)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                           "subject: " + email_subject,
                           "to: " + recipient,
                           "mime-version: 1.0",
                           "content-type: text/html"])

    # body_of_email can be plaintext or html!
    content = headers + "\r\n\r\n" + body_of_email
    session.sendmail(GMAIL_USERNAME, recipient, content)

if __name__ == '__main__':
    send_email("nikolaykgeorgiev@gmail.com", 42)
