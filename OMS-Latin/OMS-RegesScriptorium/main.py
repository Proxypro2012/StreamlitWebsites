import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patche
r1col1, r1col2 = st.columns([2, 2])


class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width = 300)
            



nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)




if selected_page == nav_pages[0]:
    st.title("The Servius Sentinel")
    st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

    
    for i in range(10):
        st.write("")

    
    operation = "retrieveImage"
    data = RetrieveData(operation)
    with r1col2:
        data.perform_operation()
    with r2col2:
        import streamlit as st
        fig, ax = plt.subplots()
        
        # Create a Rectangle patch
        rect = patches.Rectangle((0.1, 0.1), 0.6, 0.4, linewidth=2, edgecolor='blue', facecolor='green')
        
        # Add the rectangle to the plot
        ax.add_patch(rect)
        
        # Set the limits of the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        # Remove axes
        ax.axis('off')
        
        # Display the plot in Streamlit
        st.pyplot(fig)

