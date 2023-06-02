'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 16:48:43
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 16:48:46
FilePath: /Subject/learn/learn-streamlit/2-8-21-progress/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day21

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()