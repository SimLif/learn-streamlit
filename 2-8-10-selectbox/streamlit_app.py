'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 11:11:26
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 11:16:57
FilePath: /Subject/learn/learn-streamlit/2-8-10-selectbox/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day10

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.header('label_visibility')
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )