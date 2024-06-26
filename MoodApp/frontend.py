import streamlit as st
import plotly.express as px
import glob
import pathlib
from nltk.sentiment import SentimentIntensityAnalyzer

dates = []
paths = glob.glob("diary/*.txt")
for path in paths:
    filename = pathlib.Path(path).stem
    dates.append(filename)

scores = []
analyzer = SentimentIntensityAnalyzer()
for path in paths:
    with open(path) as file:
        content = file.read()
    score = analyzer.polarity_scores(content)
    scores.append(score)

positivity = []
negativity = []
for item in scores:
    positivity.append(item['pos'])
    negativity.append(item['neg'])

st.title("Diary Tone")

st.subheader("Positivity")
figure = px.line(x=dates, y=positivity,
                             labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=negativity,
                             labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)