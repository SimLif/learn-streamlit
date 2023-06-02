'''
Author: simlif 517992857@qq.com
Date: 2023-06-02 09:21:42
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-02 09:54:32
FilePath: /Subject/learn/learn-streamlit/2-8-25-session-state/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day25

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

st.selectbox('Selectbox', options=['a', 'b', 'c'], key='selectbox')

col2_1 = st.columns(1)

next_option = st.button("Next", key='next_radio')
if next_option:
    if st.session_state.radio == 'A':
        st.session_state.radio = 'B'
    elif st.session_state.radio == 'B':
        st.session_state.radio = 'C'
    elif st.session_state.radio == 'C':
        st.session_state.radio = 'A'
    else:
        st.session_state.radio = 'A'
# radio
with col2_1[0]:
    option = st.radio("Pick an option.", ('A', 'B', 'C'), key='radio')


st.write(f'You selected {st.session_state.radio}')
st.write("st.session_state object:", st.session_state)