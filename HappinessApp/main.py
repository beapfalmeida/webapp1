import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis",
             options=['GDP', 'Generosity', 'Happiness'])
y_axis = st.selectbox("Select the data for the Y-axis",
             options=['GDP', 'Generosity', 'Happiness'])

df = pd.read_csv("happy.csv")

match x_axis:
    case 'GDP':
        x = df['gdp']
        x_label = 'GDP'
    case 'Generosity':
        x = df['generosity']
        x_label = 'Generosity'
    case 'Happiness':
        x = df['happiness']
        x_label = 'Happiness'

match y_axis:
    case 'GDP':
        y = df['gdp']
        y_label = 'GDP'
    case 'Generosity':
        y = df['generosity']
        y_label = 'Generosity'
    case 'Happiness':
        y = df['happiness']
        y_label = 'Happiness'

st.subheader(f"{x_label} and {y_label}")

figure = px.scatter(df, x=x, y=y, labels={"x": x_label, "y": y_label})
st.plotly_chart(figure)
