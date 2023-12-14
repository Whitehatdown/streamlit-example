# Import necessary libraries
import streamlit as st

# Define the title of the web app
st.title("Basic Streamlit App")

# Add a slider to the web app
user_input = st.slider("Select a value", 0, 100, 50)

# Display the selected value
st.write(f"You selected: {user_input}")

# Add a text input field
user_text = st.text_input("Enter some text", "Hello, Streamlit!")

# Display the entered text
st.write(f"You entered: {user_text}")
