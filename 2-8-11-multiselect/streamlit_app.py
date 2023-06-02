'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 11:19:16
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 11:19:20
FilePath: /Subject/learn/learn-streamlit/2-8-11-multiselect/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day11

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)