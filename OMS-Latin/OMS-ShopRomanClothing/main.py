import streamlit as st
import streamlit_shadcn_ui as ui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Helper function to get item price
def get_price(item):
    prices = {
        "Toga Praetexta": 14.99,
        "Purple Toga": 21.99,
        "White Toga": 11.99,
        "Lunula": 17.99,
        "Stola": 22.99,
        "Palla": 24.99
    }
    
    return prices.get(item, 0)  # Default to 0 if not found

# Initialize session state if not already initialized
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Define item images and prices
item_images = {
    "Toga Praetexta": "redtoga.png",
    "Purple Toga": "purpletoga.png",
    "White Toga": "whitetoga.png",
    "Lunula": "lunula.png",
    "Stola": "stola.png",
    "Palla": "palla.jpeg"
}

# Create columns for layout
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])
r4col1, r4col2, r4col3 = st.columns([1, 2, 1])
r5col1, r5col2, r5col3 = st.columns([1, 2, 1])
r6col1, r6col2, r6col3 = st.columns([1, 2, 1])

options = []
options.extend(["Home", "Mihi Canistrum"])
selected_page = st.sidebar.radio("Navigation Menu", options=options)

# Home page logic
if selected_page == options[0]:
    with r1col2:  
        st.title("Home Page")
    
    with r2col2:
        taboptions = ["Mens", "Womans", "Childrens"]
        selected_home_tab = ui.tabs(taboptions)

        

        if selected_home_tab == taboptions[0]:
            with r3col2:
                st.title("Mens Clothing")
            
            with r4col2:
                st.image(item_images["Purple Toga"], caption="Purple Toga. Pretium: $21.99", width=310)
            
            with r4col3:
                st.image(item_images["White Toga"], caption="White Toga. Pretium: $11.99", width=310)
            
            # Add to cart button
                    
            with r5col2:
                if st.button("Pone in Canistrum", key="ATCPT1"):
                    st.session_state.cart.append("Purple Toga")
                    
            with r5col3:
                if st.button("Pone in Canistrum", key="ATCWT1"):
                    st.session_state.cart.append("White Toga")


            
            with r6col2:
               with st.popover("Learn more about this product"):
                  st.markdown("Haec Toga est purprea. Toga monstrat diginitas et potestas. Toga est elegans et magnus. Toga involvebatur circa corpus. Toga habet multis coloribus, sed vēnum dāmus ablus et purprea")

            with r6col3:
               with st.popover("Learn more about this product"):
                  st.markdown("Haec Toga est alba. Cives Romani togam albam gerunt. Toga quoque est valde elegans et magnus. Haec toga est facta ē lanā. Est valde puclhat. Qualitas est valde mirabile!")
            






        
        
        if selected_home_tab == taboptions[1]:
            with r3col2:
                st.title("Womens Clothing")

            with r4col2:
                st.image(item_images["Stola"], caption="Stola. Pretium: $22.99", width=310)

            with r5col2: 
                if st.button("Pone in Canistrum", key="ATCRT1"):
                    st.session_state.cart.append("Stola")
            with r6col2:
               with st.popover("Learn more about this product"):
                  st.markdown("Nupta puellae togam gerit. Alter stratum vestis est")



            with r4col3:
                st.image(item_images["Palla"], caption="Palla. Pretium: $24.99", width=310)

            with r5col3: 
                if st.button("Pone in Canistrum", key="ATCRT521"):
                    st.session_state.cart.append("Palla")
            with r6col3:
               with st.popover("Learn more about this product"):
                  st.markdown("Puellae gerunt palla circa corpus. Puellae gerunt palla ex domus. Haec palla est facta e lana. Est valde puchra et commodus. In pictura, feminae gerit palla. ")


                





        
            

        if selected_home_tab == taboptions[2]:
            with r3col2:
                st.title("Childrens Clothing")
            
            with r4col2:
                st.image(item_images["Lunula"], caption="Lunula. Pretium: 17.99", width=310)
          
            with r4col1:
                st.image(item_images["Toga Praetexta"], caption="Toga Praetexta. Pretium: $14.99")

            with r5col1:
                if st.button("Pone in Canistrum", key="ATCRT1"):
                    st.session_state.cart.append("Red Toga")
            
            with r5col2:
                if st.button("Pone in Canistrum", key="ATCRT10"):
                    st.session_state.cart.append("Lunula")
           
            with r6col1:
               with st.popover("Learn more about this product"):
                  st.markdown("Toga Praetexta est commodus est pulchra. Cives Romani toga praetexta gerunt. ")

            with r6col2:
               with st.popover("Learn more about this product"):
                  st.markdown("Puellae gerunt lunula circa collum. Puellae gerunt lunula usque ad sedecim annos natae sunt.")
            

# My Cart page logic
if selected_page == options[1]:
    with r1col2:
        st.title("My Cart")
        st.header("Items:")
        
        total_price = 0  # Variable to keep track of the total price
        cart_content = []  # To store the cart items for email body

        # Display each item from the cart with a remove button
        for item in st.session_state.cart:
            if item in item_images:  # Ensure item exists in the dictionary
                price = get_price(item)  # Get the price
                total_price += price
                total_price = total_price * 0.0625 + total_price  # Add price to total
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.image(item_images[item], caption=f"{item}. Price: ${price:.2f}", width=200)
                with col2:
                    # Generate unique key for each button
                    unique_key = f"remove_{item}_{st.session_state.cart.index(item)}_{hash(item)}"
                    
                    # Remove from cart button with a unique key for each item
                    if st.button(f"Pone {item} ex canistra", key=unique_key):
                        st.session_state.cart.remove(item)
                        
                # Add the item to the cart content list for email
                cart_content.append(f"{item}: ${price:.2f}")

        # Display total price
        st.subheader(f"Total Price: ${total_price:.2f}")

    # Checkout button should only appear when cart is not empty
    if st.session_state.cart:
        recipient_email = st.text_input("Enter email to verify order:")

        if recipient_email:  # When email is entered
            if st.button("Checkout"):  # Checkout button appears after entering email
                # Create the body of the email
                cart_body = "DO NOT REPLY! This is an automated message. Inquire here: https://shopromanclothing.streamlit.app/n"
                cart_body = "You ordered:\n"
                cart_body += "\n".join(cart_content)
                cart_body += f"\n\nTotal Pretium (including tax): ${total_price:.2f}"

                # Send email
                def send_email(recipient, subject, body):
                    sender_email = "iamtheskibidisigma420@gmail.com"  # Your email address
                    sender_password = "hqqd yfbq ccdr hlyy"  # Your email password (or app-specific password)
                
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = recipient
                    msg['Subject'] = "Your order at shopromanclothing.streamlit.app is arriving soon!"  # Fixed subject
                
                    # Attach the body with the email
                    msg.attach(MIMEText(body, 'plain'))
                
                    try:
                        # Set up the server (for Gmail in this case)
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(sender_email, sender_password)
                        text = msg.as_string()
                        server.sendmail(sender_email, recipient, text)
                        server.quit()
                        st.success("Email sent successfully!")
                    except Exception as e:
                        st.error(f"Failed to send email: {e}")
                
                send_email(recipient_email, "Your order at shopromanclothing.streamlit.app is arriving soon!", cart_body)
        else:
            st.error("Please enter an email address. (example-email@your-domain.com)")
