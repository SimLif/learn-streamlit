'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 10:59:10
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 11:05:09
FilePath: /Subject/learn/learn-streamlit/2-8-09-line-chart/streamlit_app.py
Description: https://30days.streamlit.app/?challenge=Day9
    st.line_chart 显示一个折线图。
    这是围绕 st.altair_chart 实现的一个语法糖。最主要的区别是这个命令使用数据本身的列名与索引来确定图表的参数，因此简单易用，适合于很多“画个图看看”的场景，但较难调整样式和选项。
    如果 st.line_chart 不能正确猜到数据的结构，请尝试使用 st.altair_chart 手动指定参数来生成你想要的图表。

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# altair_chart
# https://docs.streamlit.io/library/api-reference/charts/st.altair_chart