import streamlit as st
import streamlit_extras as ste


nav_pages = (['Home', 'Credits', 'Sources'])
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

if selected_page == nav_pages[0]:
  st.title("Servius Tullius")
  st.stream("Hello, sir we are callign from the microsofto.")
