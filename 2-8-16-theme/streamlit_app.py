'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 15:29:38
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 15:30:03
FilePath: /Subject/learn/learn-streamlit/2-8-16-theme/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day16

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)