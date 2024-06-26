import streamlit as st
import pandas
from send_email import send_email

topics = []
df = pandas.read_csv("topics.csv")

for index, row in df.iterrows():
    topics.append(row['topic'])

with st.form(key="contacts"):
    user_email = st.text_input(label="Your Email Address")
    topic = st.selectbox(label="What topic do you want to discuss?", options=topics)
    raw_message = st.text_area(label="Text")
    button = st.form_submit_button()

message = f"""\
Subject: New email form {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""

if button:
    send_email(message)
    st.info("Your email was sent successfully")
