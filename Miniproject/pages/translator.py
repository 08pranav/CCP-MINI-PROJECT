import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(page_title="Language Translator", layout="wide")

# Translator functionality
def display_translator():
    st.title("🌐 Language Translator")
    st.write("Translate text into various Indian languages.")

    # Initialize session state
    st.session_state.setdefault('text', '')
    st.session_state.setdefault('language', 'Hindi')
    st.session_state.setdefault('translated_text', '')

    st.session_state.text = st.text_input("Enter text to translate:", value=st.session_state.text)

    # List of Indian languages
    indian_languages = {
        "Hindi": "hi",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Kannada": "kn",
        "Odia": "or",
    }

    st.session_state.language = st.selectbox("Select language:", list(indian_languages.keys()), index=0)

    if st.button("Translate"):
        if st.session_state.text.strip():
            try:
                lang_code = indian_languages[st.session_state.language]
                translated = GoogleTranslator(source='auto', target=lang_code).translate(st.session_state.text)
                st.session_state.translated_text = translated
                st.success(f"Translated Text: {st.session_state.translated_text}")
            except Exception as e:
                st.error(f"Translation error: {e}")
        else:
            st.error("Please enter some text to translate.")

    if st.session_state.translated_text:
        st.subheader("✅ Translated Text:")
        st.write(st.session_state.translated_text)

# Main Translator Logic
if __name__ == "__main__":
    display_translator()
