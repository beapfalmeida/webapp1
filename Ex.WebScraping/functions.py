import requests
import selectorlib
import time
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

def extracting_temp(url):
    response = requests.get(url)
    code = response.text

    extractor = selectorlib.Extractor.from_yaml_file("file.yaml")
    temperature = extractor.extract(code)["temperature"]
    return temperature


def get_date():
    date = time.strftime("%d-%m-%y-%H-%M-%S")
    return date


def save_data(date, temperature):
    cursor.execute("INSERT INTO events VALUES (?,?)", (date, temperature))
    connection.commit()


if __name__ == "__main__":
    temperature = extracting_temp(url="http://programmer100.pythonanywhere.com/")
    date = get_date()
    save_data(date, temperature)

