import smtplib, ssl
import os
from email.message import EmailMessage
import imghdr

SENDER = "beatrizoffline@gmail.com"
PASSWORD = os.getenv("PASSWORD")
RECEIVER = "beatrizoffline@gmail.com"


def send_email(image):
    message = EmailMessage()
    message["Subject"] = "New customer showed up"
    message.set_content("Hey, we just saw a new customer!")

    with open(image, 'rb') as file:
        content = file.read()

    message.add_attachment(content, maintype="image",
                           subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image="images/120.png")