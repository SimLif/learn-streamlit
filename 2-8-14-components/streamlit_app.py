'''
Author: simlif 517992857@qq.com
Date: 2023-06-01 11:35:18
LastEditors: simlif 517992857@qq.com
LastEditTime: 2023-06-01 11:36:11
FilePath: /Subject/learn/learn-streamlit/2-8-14-components/streamlit_app.py
Description: https://github.com/victoryhb/streamlit-option-menu

Copyright (c) 2023 by simlif, All Rights Reserved. 
'''
import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

# 2. horizontal menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# 3. CSS style definitions
selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# 4. Manual Item Selection
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None
    
selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    orientation="horizontal", manual_select=manual_select, key='menu_4')
st.button(f"Move to Next {st.session_state.get('menu_option',1)}", key='switch_button')
selected4

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")
    
selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        on_change=on_change, key='menu_5', orientation="horizontal")
selected5