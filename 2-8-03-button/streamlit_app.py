'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 10:01:16
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-02 09:40:27
FilePath: /Subject/learn/learn-streamlit/2-8-03-button/streamlit_app.py
Description: 

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.header('st.button()')


if 'a_counter' not in st.session_state:
    st.session_state.a_counter = 0
if 'boolean' not in st.session_state:
    st.session_state.boolean = False

button_clicked = st.button('Say hello')

"before pressing the button, st.session_state is", st.session_state

if button_clicked:
    st.write(f'button_clicked: {button_clicked}')
    st.write('Why hello there')
    st.session_state.a_counter += 1
    st.session_state.boolean = not st.session_state.boolean
    "after pressing the button, st.session_state is", st.session_state
else:
    st.write(f'button_clicked: {button_clicked}')
    st.write('Goodbye')

st.selectbox('Select a number', range(st.session_state.a_counter))
    
        