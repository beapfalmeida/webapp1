import streamlit as st
import plotly.express as px
from get_data import get_data

st.title("Weather Forecast for the Next Days:")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days, option)
        if option == "Temperature":
            temperatures = [dictionary["main"]["temp"] for dictionary in
                            filtered_data]
            temperatures = [temperature / 10 for temperature in temperatures]

            dates = [dictionary["dt_txt"] for dictionary in filtered_data]

            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dictionary["weather"][0]["main"] for dictionary in
                             filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.info("Please enter a name of a real place!")
