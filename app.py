import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
#header section
with st.container():
	st.subheader("Hello World")
	st.title("Streamlit")
	st.write("This website is designed using streamlit")
	st.write("[Learn More about streamlit on] (https://docs.streamlit.io/)")

#adding animation 

def loadanime(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

#load animation
questionani = loadanime("https://assets1.lottiefiles.com/temp/lf20_9gY9Yf.json")

#What streamlit does
with st.container():
	st.write("---")
	left_column,right_column = st.columns(2)
	with left_column:
		st.header("What it does")
		st.write("##")
		st.write(
			"""
			Streamlit is an open-source Python library that 
			simplifies the process of building interactive web applications 
			for data science and machine learning tasks. 
			It allows developers to create customizable and 
			responsive web interfaces with minimal coding efforts, 
			making it easy to share data-driven insights and prototypes with others.
			With Streamlit, users can create interactive visualizations, 
			input forms, and other UI components that are updated in real-time, 
			enabling faster experimentation and collaboration in data science projects.
			"""
		)
	with right_column:
		st_lottie(questionani,height=300,key="question") 