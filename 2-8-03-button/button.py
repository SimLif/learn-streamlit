import streamlit as st

st.header('st.button()')

button_clicked = st.button('Say hello')

if button_clicked:
    st.write(f'button_clicked: {button_clicked}')
    st.write('Why hello there')
else:
    st.write(f'button_clicked: {button_clicked}')
    st.write('Goodbye')
    

        