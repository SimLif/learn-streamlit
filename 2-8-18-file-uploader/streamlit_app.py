'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 15:54:13
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 16:24:51
FilePath: /Subject/learn/learn-streamlit/2-8-18-file-uploader/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day18

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import os
import streamlit as st
import pandas as pd

base_path = os.path.abspath(__file__)

st.title('st.file_uploader')
st.info(f'base_path: {base_path}')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
st.write('You uploaded this CSV file:', uploaded_file)

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')