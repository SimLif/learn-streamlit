import streamlit as st

st.header('st.sidebar')

add_sidebar = st.sidebar.selectbox('A or B', ['A', 'B'])

if add_sidebar == 'A':
    st.write('A')
else:
    st.write('B')


        