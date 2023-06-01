'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 10:02:09
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 10:16:48
FilePath: /Subject/learn/learn-streamlit/2-8-05-write/write.py
Description: https://30days.streamlit.app/?challenge=Day5
    
Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write(1234)

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# st.caption
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# st.markdown
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# st.header
st.header('This is a header')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')
st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

# st.text
st.text('This is some text.')

# st.latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# st.code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')