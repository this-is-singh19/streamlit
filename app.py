import streamlit as st
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
#header section
with st.container():
	st.subheader("Hello World")
	st.title("Streamlit")
	st.write("This website is designed using streamlit")
	st.write("[Learn More about streamlit on] (https://docs.streamlit.io/)")

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