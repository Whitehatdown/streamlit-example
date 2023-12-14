# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for demonstration
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [30, 45, 25, 50]
}
df = pd.DataFrame(data)

# Title of the web app
st.title("Analysis Report with Streamlit")

# Section for Graphs
st.header("Graphs")

# Line Chart
st.subheader("Line Chart")
st.line_chart(df.set_index('Category'))

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(df.set_index('Category'))

# Pie Chart (using streamlit's pie chart function)
st.subheader("Pie Chart")
st.pie_chart(df.set_index('Category')['Values'])

# Area Chart
st.subheader("Area Chart")
st.area_chart(df.set_index('Category'))

# Section for Analysis
st.header("Analysis")

# Add images for analysis
st.image("path_to_image1.jpg", caption="Caption for Image 1", use_column_width=True)
st.image("path_to_image2.jpg", caption="Caption for Image 2", use_column_width=True)

# Future Prediction Section
st.header("Future Prediction")

# Input for future prediction
future_prediction = st.text_input("Enter your prediction for the future:", "The values will increase.")

# Display the prediction
st.write(f"Future Prediction: {future_prediction}")

# Links Section for Citations
st.header("Links and Citations")

# Input for links
citation_links = st.text_area("Enter citations and links:", "Author et al., (Year). Title of the Paper. [Link to Paper]")

# Display the links
st.write("Citations and Links:")
st.markdown(citation_links)

# Note: Replace "path_to_image1.jpg" and "path_to_image2.jpg" with the actual file paths or URLs of your images.

# Data for token distribution
token_distribution_data = {
    "Gnosis Vault, Founders & Project": 95.8,
    "ICO Investors": 4.2
}

# Title of the web app
st.title("Token Distribution Information")

# Display token distribution information
st.header("Token Distribution")

# Create a DataFrame for better formatting
token_distribution_df = pd.DataFrame(list(token_distribution_data.items()), columns=["Category", "Percentage"])

# Display the token distribution table
st.table(token_distribution_df)
