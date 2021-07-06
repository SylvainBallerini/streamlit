import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import numpy as np

st.title("Hello Wilders, Welcome to my application")

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
#st.write(df_weather)

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

df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)