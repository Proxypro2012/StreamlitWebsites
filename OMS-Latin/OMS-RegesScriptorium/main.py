import streamlit as st
from streamlit_carousel import carousel


r1col1, r1col2 = st.columns([1, 0.5])
rgap1col1, rgap1col2 = st.columns([1, 0.5])
r2col1, r2col2 = st.columns([1, 2])
r3col1, r3col2, r3col3 = st.columns([2, 2, 2])
r4col1, r4col2, r4col3 = st.columns([0.1, 4, 0.1])# Create two columns, one smaller (1) and one larger (2)

class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width=230, caption="***In Pictura Est Servius Tullius***")
        if self.operation == "displayHomeTitle":
            st.title("The Servius Sentinel")
            st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

# Sidebar navigation
nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

items_images = [
    dict(
        title="Slide 1",
        text="Merch for Servius Tullius",
        img="OMS-Latin/OMS-RegesScriptorium/tshirt-merch.jpeg"
        
    ),

    dict(
        title="Slide 2",
        text="Servius",
        img="https://upload.wikimedia.org/wikipedia/commons/1/1a/Servius_by_Rouille.jpg"
        
    )
]

if selected_page == nav_pages[1]:
    st.title("Credits")
    st.write("Developers and Writers")

    for i in range(10):
        st.write("")

    st.write("Kabir Tiwari - Developer and Writer")
    st.write("Gunner Gordon - Writer and Designer")

if selected_page == nav_pages[0]:
    
    
    operation = "displayHomeTitle"
    data = RetrieveData(operation)
    with r1col1:
        data.perform_operation()

    with rgap1col1:
        for i in range(10):
            st.write("")

    operation = "retrieveImage"
    data = RetrieveData(operation)
    
    # Add content in two columns
    with r2col1:
        data.perform_operation()# Left column for the image
        

    with r2col2:
        st.subheader("**The Rise**")
        #st.write("Servius Tullius est sextus rex")
        st.write("**Servius Tullius** natus est servus")
        st.write("**Tarquinnius Priscus** est quintus rex. Uxor eius est **Tanaquil**. **Tanaqil** videt **ignis cirum Servius caput.**")
        st.markdown("**Servius Tullius** aedificit **Muri Serviani**")
        st.markdown("**Sextus Tullius** habet **primum censum**")

    for i in range(10):
        st.write("")

    with r3col1:
        st.header("The Rise")
        st.markdown("**Servius Tullius** was born a slave. One day, the wife of the fifth roman king **Tarquinius Priscus**, **Tanaquil**, saw the young boy with a ring of fire around his head. She interpreted this as a sign from the gods. She told **Tarquinius Priscus**, and the two of them decided to raise **Servius Tullius** to be the next king.")

    with r3col2:
        st.header("The Rule")
        st.write("**Servius Tullius** was a great king. He had many accomplishments during his rule, including **expanding the walls** around **Rome**. He also held the first official **census**, a count of the population. He also had **success in battles** and he also brought the **Cult of Diana** to **Rome**.")
    with r3col3:
        st.header("The Revolt")
        st.write("**Servius Tullius** was eventually overthrown by the love intrest of his daughter **Tullia**, **Tarquinius Superbus**. **Servius** was kicked down the stairs of the **Senate House**, where he was then **ran over by his daughter** in a chariot.")
    with r4col2:
        carousel(items=items_images)
    
    

    
