import streamlit as st
import streamlit_extras as ste


nav_pages = (['Home', 'Credits', 'Sources'])
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

