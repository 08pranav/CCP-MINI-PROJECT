import streamlit as st
import os
from pathlib import Path


def load_html_content(file_path):
   """
   Function to load HTML content from a given file path.
   """
   try:
       with open(file_path, 'r', encoding='utf-8') as file:
           html_content = file.read()
       return html_content
   except FileNotFoundError:
       st.error(f"File not found: {file_path}")
       return None
   except Exception as e:
       st.error(f"Error loading file: {str(e)}")
       return None


# Page Configuration
st.set_page_config(page_title="E-Books Viewer", layout="wide")


# Add custom background, font styles, and animations
st.markdown("""
   <style>
   /* Background styling */
   .stApp {
       background-color: #ffe0b3;
       background-image: linear-gradient(120deg, #ff9966 0%, #ff5e62 100%);
       color: #000;
       font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   }


   /* Custom fonts and header */
   h1, h2, h3 {
       text-align: center;
       color: #333;
       animation: fadeIn 2s ease-in-out;
   }
  
   p {
       font-size: 16px;
       line-height: 1.5;
       color: #444;
       animation: fadeIn 3s ease-in-out;
   }


   /* Animations */
   @keyframes fadeIn {
       from { opacity: 0; transform: translateY(-20px); }
       to { opacity: 1; transform: translateY(0); }
   }


   /* Buttons */
   .stButton > button {
       background-color: #ff7f50;
       color: white;
       font-size: 16px;
       font-weight: bold;
       border-radius: 8px;
       padding: 8px 20px;
       margin-top: 20px;
       border: none;
       transition: all 0.3s ease;
   }
   .stButton > button:hover {
       background-color: #ff6347;
       transform: scale(1.05);
   }


   /* Scrollable iframe */
   iframe {
       border: none !important;
       box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
       border-radius: 12px;
   }
   </style>
""", unsafe_allow_html=True)


# Main content area
try:
   # Load the HTML content from the file in the same directory
   html_file_path = "e books.html"
   content = load_html_content(html_file_path)
  
   if content:
       # Display the HTML content inside an iframe with animations
       st.markdown("<h1>E-Books Viewer</h1>", unsafe_allow_html=True)
       st.components.v1.html(content, height=800, scrolling=True)
   else:
       st.error("Could not load the e-books content.")
      
except Exception as e:
   st.error(f"An error occurred: {str(e)}")



