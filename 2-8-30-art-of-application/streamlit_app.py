'''
Author: simlif 517992857@qq.com
Date: 2023-06-02 14:46:43
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-02 14:46:51
FilePath: /Subject/learn/learn-streamlit/2-8-30-art-of-application/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day30

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')