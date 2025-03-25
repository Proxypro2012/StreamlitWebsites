import streamlit as st
import streamlit_extras as ste

nav_pages = (['Home', 'Credits', 'Sources'])
selected_page = st.sidebar.radio("Navigation", nav_pages)
