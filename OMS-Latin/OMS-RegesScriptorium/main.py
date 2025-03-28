import streamlit as st
import streamlit_extras as ste
import time


nav_pages = (['Home', 'Credits', 'Sources'])
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

#def write_text_consecutively(text, interval):
  

if selected_page == nav_pages[0]:
  st.title("The Servius Sentinel")
  st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

  
  
  TEST = """
  Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
  nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
  """


