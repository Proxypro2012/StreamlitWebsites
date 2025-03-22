import streamlit as st
import streamlit.components.v1 as components
import time

# Set page config (must be the first Streamlit command)
st.set_page_config(
    layout="wide",
    page_title="Chromium",
    page_icon="Chromium/logo.png",  # Optionally, set a page icon
    initial_sidebar_state="expanded"
)


game_urls = {
    "getaway_shootout": "https://selenite-e3u.pages.dev/getawayshooter/"
}


webpages = ["Home", "Games", "Status"]
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("", webpages)
st.sidebar.image("Chromium/logo.png")





if selected_page == webpages[0]:
    st.title("Chromium")
    st.write("Versatile web proxy. For my guys at school.")




    
    
if selected_page == webpages[1]:
    st.subheader("Getaway Shootout!")
    try:
        components.iframe(game_urls["getaway_shootout"], width=800, height=605)
    except:
        st.error("Embedding failed. Use the link below to play the game.")
    
    # Alternative option: Provide a clickable link
    st.subheader("Alternative Link")
    st.markdown(f'[Click here to play Getaway Shootout]({game_urls["getaway_shootout"]})', unsafe_allow_html=True)
    
    # Additional app features
    st.text("Enjoy playing Getaway Shootout!")





if selected_page == webpages[2]:
    #with st.status("Downloading repository data..."):
    #    st.write("Searching for data...")
    #    time.sleep(2)
    #    st.write("Found URL.")
    #    time.sleep(1)
    #    st.write("Extracting data...")
    #    time.sleep(1)
    st.status("Website Under Development")
    



