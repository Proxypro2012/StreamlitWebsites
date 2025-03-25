import streamlit as st
import streamlit_extras as ste


nav_pages = (['Home', 'Credits', 'Sources'])
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

if selected_page == nav_pages[0]:
  st.title("Servius Tullius")
  import time
  import numpy as np
  import pandas as pd
  import streamlit as st
  
  _LOREM_IPSUM = """
  Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
  nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
  """
  
  
  def stream_data():
      for word in _LOREM_IPSUM.split(" "):
          yield word + " "
          time.sleep(0.02)
  
      yield pd.DataFrame(
          np.random.randn(5, 10),
          columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
      )
  
      for word in _LOREM_IPSUM.split(" "):
          yield word + " "
          time.sleep(0.02)
  
  
  if st.button("Stream data"):
      st.write_stream("hello")
