import streamlit as st
import pandas as pd

st.title("Hello Wilders, Welcome to my application")

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

name = st.text_input("Please give me your name : ")
name_length = len(name)
st.write("Your name has ", name_length,"characters")

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")