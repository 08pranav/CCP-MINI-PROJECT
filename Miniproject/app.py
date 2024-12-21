import streamlit as st
import base64
import os


# Set page configuration
st.set_page_config(page_title="Welcome to India", layout="wide")


# Function to set background image
def set_bg_image(image_file):
   try:
       with open(image_file, "rb") as image:
           b64_image = base64.b64encode(image.read()).decode("utf-8")
       st.markdown(
           f"""
           <style>
           /* Background image */
           .stApp {{
               background-image: url("data:image/png;base64,{b64_image}");
               background-size: cover;
               background-repeat: no-repeat;
               background-attachment: fixed;
           }}
          
           /* Title styles */
           h1 {{
               font-family: Arial, sans-serif;
               margin: 0;
           }}
           .welcome {{
               font-size: 100px;
               font-weight: normal;
               color: white;
               letter-spacing: 2px;
               animation: fadeIn 2s ease-in-out;
           }}
           .india {{
               font-size: 225px;
               font-weight: bold;
               color: white;
               margin: 0;
               animation: fadeIn 3s ease-in-out;
           }}
           p {{
               color: white;
               font-size: 18px;
               max-width: 600px;
               animation: fadeIn 3s ease-in-out;
           }}


           /* Button styles for glassmorphism */
           .stButton > button {{
               background: rgba(255, 255, 255, 0.2);
               border: 1px solid rgba(255, 255, 255, 0.4);
               backdrop-filter: blur(10px);
               color: white;
               font-size: 18px;
               font-weight: bold;
               border-radius: 12px;
               padding: 10px 25px;
               transition: transform 0.3s ease, background 0.3s ease;
               margin : 60px
               cursor: pointer;
           }}


           .stButton > button:hover {{
               background: rgba(255, 255, 255, 0.4);
               transform: scale(1.05);
           }}


           /* Animation keyframes */
           @keyframes fadeIn {{
               from {{
                   opacity: 0;
                   transform: translateY(20px);
               }}
               to {{
                   opacity: 1;
                   transform: translateY(0);
               }}
           }}
           </style>
           """,
           unsafe_allow_html=True
       )
   except FileNotFoundError:
       st.error(f"Background image file '{image_file}' not found.")


def main():
   # Set the background image
   bg_image_path = "screenshot.jpg"
   if os.path.exists(bg_image_path):
       set_bg_image(bg_image_path)
   else:
       st.warning(f"Background image {bg_image_path} not found. Using default background.")


   # Create two columns for layout
   col1, col2 = st.columns([3, 2])


   with col1:
       # Title section
       st.markdown(
           """
           <h1>
               <span class="welcome">WELCOME TO</span><br>
               <span class="india">INDIA</span>
           </h1>
           """,
           unsafe_allow_html=True
       )
       st.markdown(
           """
           <p>
           Dive into the wonders of India with our interactive experience! Test your knowledge with fun quizzes, explore the diversity of Indian languages with our translator, and learn fascinating facts about this vibrant country. Whether you're here to explore or learn, let the journey begin!
           </p>
           """,
           unsafe_allow_html=True
       )


   with col2:
       st.markdown("<br><br>", unsafe_allow_html=True)


       # Add buttons with navigation
       if st.button("LANGUAGE TRANSLATOR"):
           st.switch_page("pages/translator.py")  # Redirect to Translator page
       if st.button("TAKE A QUIZ"):
           st.switch_page("pages/quiz.py")  # Redirect to Quiz page
       if st.button("KNOWLEDGE REPOSITORY"):
           st.switch_page("pages/repo.py")  # Redirect to Repository page
       if st.button("Voice Search"):
           st.switch_page("pages/voice_search.py")  # Placeholder for future functionality


if __name__ == "__main__":
   main()