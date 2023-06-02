'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 16:29:44
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 16:44:17
FilePath: /Subject/learn/learn-streamlit/2-9-19-layout/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day19

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import time
import streamlit as st

st.set_page_config(layout="wide")
# st.set_page_config(layout="centered")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


# st.header('Empty')
# with st.empty():
#     for seconds in range(10):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")

# st.write('Done!')

st.header('Placeholders')
placeholder = st.empty()
time.sleep(5)

# Replace the placeholder with some text:
placeholder.text("Hello")
time.sleep(5)

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(5)

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")
time.sleep(5)

# Clear all those elements:
placeholder.empty()

st.text('Done!')