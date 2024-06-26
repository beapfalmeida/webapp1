import streamlit as st
import plotly.express as px
import functions
import sqlite3

url = "http://programmer100.pythonanywhere.com/"

temperature = functions.extracting_temp(url)
date = functions.get_date()
functions.save_data(date, temperature)

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()

dates = [item[0] for item in rows]
temperatures = [item[1] for item in rows]

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)" })
st.plotly_chart(figure)