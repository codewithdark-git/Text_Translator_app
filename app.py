import streamlit as st
from googletrans import LANGUAGES, Translator

# Dictionary mapping language codes to full country names
language_mapping = {code: LANGUAGES[code] for code in LANGUAGES}

# List of all language codes
all_language_codes = list(language_mapping.keys())

# List of all language names
all_language_names = list(language_mapping.values())

# Customizing Streamlit's theme
st.markdown(
    """
    <style>
    /* Modify the background color */
    body {
        background-color: #f0f2f6;
    }
    /* Modify the text color */
    .stApp {
        color: white;
    }
    /* Increase font size */
    .st-ec {
        font-size: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language)
        return translated_text.text
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return None

def main():
    st.title("Text Translator")

    col1, col2 = st.columns([2, 1])

    with col1:
        input_text = st.text_area("Enter the text to translate:", height=200)

    with col2:
        target_language_name = st.selectbox("Select target language:", options=all_language_names)

    target_language_code = [code for code, name in language_mapping.items() if name == target_language_name][0]

    if st.button("Translate"):
        if input_text and target_language_code:
            translated_text = translate_text(input_text, target_language_code)
            if translated_text is not None:
                st.success(f"Translation to {target_language_name}:")
                st.code(translated_text, language='python')
        else:
            st.warning("Please provide both text and select a target language.")

if __name__ == "__main__":
    main()
