import streamlit as st
import os, base64

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Its Santu")

# Absolute path of the image
image_path = os.path.abspath("HOME.png")

# Inject custom CSS to remove padding and margins
hide_streamlit_style = """
    <style>
        /* Remove padding and margins from the main content */
        .block-container {
            padding: 0;
            margin: 0;
        }
        #MainMenu {visibility: hidden;}  /* Hide the main menu */
        footer {visibility: hidden;}  /* Hide the footer */
        header {visibility: hidden;}  /* Hide the header */
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

custom_css = """
    <style>
        body {
            background-color: #f0f0f0;  /* Change background color */
        }
        .css-1aumxhk {
            display: none;  /* Hides specific Streamlit components */
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load your HTML file
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string

# Path to your image
# image_path = "images/your-image.jpg"
encoded_image = image_to_base64("images/HOME.png")
# Streamlit App
# st.title("Embed HTML, CSS, and JS in Streamlit")

# Load the HTML content
html_content = load_html("templates/index.html")

# Embed the HTML with full-screen dimensions
st.components.v1.html(
    html_content,
    height=890,  # Set a high value for height
    scrolling=True  # Allow scrolling if needed
)

# Add a centered footer text
st.markdown(
    """
    <div style="text-align: center; margin-top: -20px; font-size: 14px; color: gray;">
        &copy; 2024 It's Santu. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True,
)