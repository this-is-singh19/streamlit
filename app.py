import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#import image
dropbox = Image.open("Images\Dropbox-Logo.png")
ibm = Image.open("Images\IBM_logo.svg.png")
netflix = Image.open(r"Images\Netflix_Logo.png")
openai = Image.open(r"Images\OpenAI_Logo.svg.png")
uber = Image.open(r"Images\Uber_Logo.png")

st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
#header section
with st.container():
	col1, col2, col3 = st.columns(3)
	with col1:
    		st.write(' ')

	with col2:
    		st.title("HELLO WORLD")

	with col3:
    		st.write(' ')

with st.container():
	st.title("Streamlit")
	st.write("This website is designed using streamlit")
	st.write("[Learn More about streamlit by clicking on this](https://docs.streamlit.io/)")

#adding animation 

def loadanime(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

#load animation
questionani = loadanime("https://assets1.lottiefiles.com/temp/lf20_9gY9Yf.json")
dataanalyst = loadanime("https://assets9.lottiefiles.com/packages/lf20_49rdyysj.json")

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

#use cases of streamlit
with st.container():
	st.write("---")
	left_column,right_column = st.columns(2)
	with left_column:
		st_lottie(dataanalyst,height=300,key="analyst") 
	with right_column:
		st.header("Use cases of streamlit")
		st.write("##")
		st.write(
			"""
			Streamlit is a powerful tool for building interactive web applications with Python. 
			One common use case for Streamlit is data visualization, where it allows 
			developers to create engaging and dynamic data visualizations with minimal coding effort. 
			For example, a data analyst or data scientist can use Streamlit to build a dashboard that 
			displays key insights and trends from a dataset in a user-friendly way. 
			Additionally, Streamlit is also useful for building machine learning models, 
			as it allows developers to quickly prototype and visualize the performance 
			of different models and parameters. With its simple syntax and powerful features, 
			Streamlit is becoming an increasingly popular tool for data scientists and developers alike.
			"""
		)

#use cases of streamlit
with st.container():
	
	st.write("---")
	st.header("Companies that use streamlit")
	a,b,c = st.columns(3)
	with a:
		st.image(dropbox, use_column_width='auto' )
	with b:
		st.image(netflix, use_column_width='auto'  )
	with c:
		st.image(uber, use_column_width='auto'  )	

with st.container():
	col1, col2, col3 = st.columns(3)
	with col1:
    		st.write(' ')

	with col2:
    		st.title("Thank You for visiting")

	with col3:
    		st.write(' ')