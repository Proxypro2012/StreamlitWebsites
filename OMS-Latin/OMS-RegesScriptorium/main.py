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
        text="A tree in the savannah",
        img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
        link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="OMS-Latin/OMS-RegesScriptorium/tshirt-merch.jpeg",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
    ),
    dict(
        title="Slide 4",
        text="PANDAS",
        img="pandas.webp",
    ),
    dict(
        title="Slide 4",
        text="CAT",
        img="cat.jpg",
    ),
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
    
    

    
