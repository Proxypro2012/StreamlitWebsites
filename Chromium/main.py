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
    "slope_1": "https://xlegends.github.io/slope-1/"
}


webpages = ["Home", "Games", "Status"]
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("", webpages)
st.sidebar.image("Chromium/logo.png")





if selected_page == webpages[0]:
    st.title("Chromium")
    st.write("Versatile web proxy. For my guys at school.")




    
    
if selected_page == webpages[1]:
    st.subheader("Slope 1")
    try:
        components.iframe(game_urls["slope_1"], width=800, height=605)
    except:
        st.error("Embedding failed. Use the link below to play the game.")
    
    # Alternative option: Provide a clickable link
    st.subheader("Alternative Link")
    
    hidden_url_script = f"""
    <a href="javascript:void(0);" onclick="window.open('about:blank').document.write('<iframe src={game_urls['slope_1']} style=width:100%;height:100%;border:none;></iframe>')">Click here to play Slope 1</a>
    """
    
    st.markdown(hidden_url_script, unsafe_allow_html=True)
    
    # Additional app features
    st.text("Enjoy playing Slope 1!")





if selected_page == webpages[2]:
    #with st.status("Downloading repository data..."):
    #    st.write("Searching for data...")
    #    time.sleep(2)
    #    st.write("Found URL.")
    #    time.sleep(1)
    #    st.write("Extracting data...")
    #    time.sleep(1)
    st.status("Website Under Development")
    



