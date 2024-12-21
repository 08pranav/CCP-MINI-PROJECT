import streamlit as st
import base64
import time


# Page configuration
st.set_page_config(page_title="Cultural Heritage Quiz", page_icon="🌍", layout="wide")


# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
   with open(bin_file, 'rb') as f:
       data = f.read()
   return base64.b64encode(data).decode()


# Function to set background image
def set_background(image_file):
   bin_str = get_base64_of_bin_file(image_file)
   page_bg_img = f'''
   <style>
   .stApp {{
       background-image: url("data:image/png;base64,{bin_str}");
       background-size: cover;
       background-position: center;
       background-repeat: no-repeat;
       background-attachment: fixed;
   }}


   /* Center the title */
   .title {{
       text-align: center;
       color: white !important;
       text-shadow: 2px 2px 4px rgba(0,0,0,0.7) !important;
       font-size: 3.5em !important;
       margin-bottom: 20px;
       animation: fadeIn 2s;
   }}


   /* Paragraph below the header */
   .intro-paragraph {{
       text-align: center;
       font-size: 1.8em !important;
       color: #ffffff !important;
       text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
       margin-bottom: 30px;
       animation: fadeInUp 3s;
   }}


   /* Question text animation */
   .stRadio > div > label {{
       font-size: 2em !important;
       line-height: 1.8 !important;
       color: #333 !important;
       margin-bottom: 15px !important;
       animation: fadeInUp 2s;
   }}


   /* Radio button options styling */
   .stRadio > div > div > label {{
       background-color: rgba(255, 255, 255, 0.9) !important;
       border-radius: 12px !important;
       padding: 10px 15px !important;
       margin-bottom: 10px !important;
       font-size: 1.5em !important;
       transition: all 0.3s ease !important;
   }}


   /* Highlight selection */
   .stRadio > div > div > label[data-selected="true"] {{
       background-color: rgba(255, 0, 0, 0.2) !important;
       border: 2px solid red !important;
   }}


   /* Button styling */
   .stButton > button {{
       background-color: #2196F3 !important;
       color: white !important;
       font-size: 1.5em !important;
       padding: 10px 25px !important;
       border-radius: 15px !important;
       transition: all 0.3s ease !important;
   }}


   .stButton > button:hover {{
       background-color: #1976D2 !important;
       transform: scale(1.05) !important;
   }}


   /* Animations */
   @keyframes fadeIn {{
       from {{ opacity: 0; }}
       to {{ opacity: 1; }}
   }}


   @keyframes fadeInUp {{
       from {{ opacity: 0; transform: translateY(20px); }}
       to {{ opacity: 1; transform: translateY(0); }}
   }}


   </style>
   '''
   st.markdown(page_bg_img, unsafe_allow_html=True)


# Function to display animated success message
def show_animated_success():
   with st.container():
       for i in range(3):
           st.markdown(f"<h1 style='text-align: center; color: lime;'>Correct! 🎉</h1>", unsafe_allow_html=True)
           time.sleep(0.3)
           st.markdown("", unsafe_allow_html=True)


# Function to display quiz
def display_quiz():
   # Set background image
   set_background('screenshot1.jpg')


   # Main title and introduction
   st.markdown("<h1 class='title'>Cultural Heritage Quiz 🌍</h1>", unsafe_allow_html=True)
   st.markdown("<p class='intro-paragraph'>Test Your Knowledge of Global Cultural Preservation</p>", unsafe_allow_html=True)


   # Questions
   score = 0
   q1 = st.radio(
       "1. Why is cultural heritage protection important in the context of globalization?",
       (
           "Cultural heritage protection is not necessary as globalization promotes homogenization",
           "Cultural heritage protection ensures that traditional cultures are preserved in their original form without adaptation",
           "Cultural heritage protection is important to maintain the diversity of human cultures, and international organizations like UNESCO help safeguard this diversity through conventions, education, and preservation efforts",
           "Cultural heritage protection only applies to tangible artifacts, not intangible cultural practices"
       )
   )


   if q1 == "Cultural heritage protection is important to maintain the diversity of human cultures, and international organizations like UNESCO help safeguard this diversity through conventions, education, and preservation efforts":
       score += 1


   q2 = st.radio(
       "2. How can modern technologies aid in protecting cultural practices and artifacts?",
       (
           "By replacing traditional practices with digital ones",
           "By making cultural artifacts more accessible but not offering any preservation benefits",
           "By capturing and digitally preserving cultural artifacts and practices, enabling future generations to study and recreate them without the risk of damage or loss",
           "By storing digital archives without any physical preservation methods"
       )
   )


   if q2 == "By capturing and digitally preserving cultural artifacts and practices, enabling future generations to study and recreate them without the risk of damage or loss":
       score += 1


   q3 = st.radio(
       "3. What are ethical considerations in protecting intangible cultural heritage?",
       (
           "The primary ethical concern is ensuring that traditional practices are not altered in any way to accommodate modernization",
           "Ethical considerations include respecting the community's right to own and control their cultural expressions while allowing for innovation that does not undermine the cultural significance of the practices",
           "The ethical focus should be solely on preserving traditional practices without consideration for the benefits of modernization",
           "There are no ethical considerations, as modernization naturally overcomes traditional practices"
       )
   )


   if q3 == "Ethical considerations include respecting the community's right to own and control their cultural expressions while allowing for innovation that does not undermine the cultural significance of the practices":
       score += 1


   # Submit button
   col1, col2, col3 = st.columns([1, 2, 1])
   with col2:
       if st.button("Submit Quiz"):
           if score == 3:
               st.balloons()
               st.success(f"Perfect Score! Your score is: {score}/3 🎉")
               show_animated_success()
           else:
               st.warning(f"Your score is: {score}/3. Keep practicing! 🙂")


# Display the quiz
if __name__ == "__main__":
   display_quiz()
