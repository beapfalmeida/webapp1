import requests
import streamlit as st
import time

key = "DXgKNQMNRK5Y0OMTbnLOxFDIvesPydEMI85HyeLB"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={key}"

st.set_page_config("wide")


response1 = requests.get(url)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

response2 = requests.get(image_url)

with open("galaxy.jpg", 'wb') as file:
    file.write(response2.content)

st.header(title)
st.image("galaxy.jpg")
st.write(explanation)



