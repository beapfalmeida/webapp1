import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Company")

comp_description = """ A company description is an overview or summary of a business.
 It's an important part of a business plan that often briefly
  describes an organization's history, location,
  mission statement, management personnel and, when appropriate, legal structure."""

st.write(comp_description)

st.header("Our team")

col1, col2, col3 = st.columns(3)

data_frame = pandas.read_csv("../CompanyApp/data2.csv", sep=",")

with col1:
    for index, row in data_frame[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images2/" + row['image'])

with col2:
    for index, row in data_frame[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images2/" + row["image"])

with col3:
    for index, row in data_frame[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images2/" + row['image']) # importante! / neste sentido para filepaths (ctrl 7)
