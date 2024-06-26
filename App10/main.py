import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# Getting the html code corresponding to the web page in a txt file
def scrape(url):
    """ Scrape the page source from the url"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "beatrizoffline@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "beatrizoffline@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    print("row =", row)
    band, city, date = row
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",
                   (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            row = read(extracted)
            # If row is not an empty list
            if not row:
                try:
                    store(extracted)
                    send_email(message="Hey, new event was found")
                except sqlite3.OperationalError:
                    connection.rollback()
                    print("rollback")

        time.sleep(2)
