'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 17:28:26
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 21:00:37
FilePath: /Subject/learn/learn-streamlit/2-8-24-cache/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day24

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st
import numpy as np
import pandas as pd
from time import time, sleep

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache_data()
def load_data_a(flag=1):
    df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
    )
    sleep(5)
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b(flag=1):
    df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
    )
    sleep(5)
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)