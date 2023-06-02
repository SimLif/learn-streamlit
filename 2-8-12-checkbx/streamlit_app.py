'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 11:22:00
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 11:22:14
FilePath: /Subject/learn/learn-streamlit/2-8-12-checkbx/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day12

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")