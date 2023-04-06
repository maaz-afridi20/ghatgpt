import pandas as pd 
import streamlit as stl


stl.number_input('Pick a number',0,10)
stl.text_input('Email Adress')
stl.date_input('birth date')
stl.text_area('description')
stl.color_picker('choose color')
stl.file_uploader('upload file')


stl.subheader('progress bar')
stl.progress(20)

stl.sidebar.title('enter your asdfa')
stl.sidebar.button('Click')
stl.sidebar.radio('enter gender',["Male","Female"])