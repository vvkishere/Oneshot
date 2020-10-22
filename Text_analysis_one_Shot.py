from ktrain import text
import pandas as pd
import streamlit as st
import tensorflow as tf


st.title("Sentence Explorer and Classifier")

#Data Loading Code - In The Sidebar
data = st.sidebar.file_uploader("Load the file to be analysed",type='xlsx')
df = pd.ExcelFile((data))
sheetlist = df.sheet_names
option = st.sidebar.selectbox('Select sheet with data', sheetlist)
textdata = pd.read_excel(data, sheet_name=option)
cols = textdata.columns
colname = st.sidebar.selectbox('Select the column name with data', cols)

#Display data on the main screen if needed
if st.sidebar.checkbox("Preview Data"):
    st.text("Data Loaded")
    textdata[colname]

finaldata = textdata[colname]
zsl = text.ZeroShotClassifier()
