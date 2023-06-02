'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 15:37:50
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 15:37:58
FilePath: /Subject/learn/learn-streamlit/2-8-17-secrets/streamlit_app.py
Description: 

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])