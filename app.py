import streamlit as st
from translate import Translator
from gtts import gTTS
import tempfile

# Page configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 Language Translation Tool")
st.write(
    "Translate text from one language to another using an online translation service."
)

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru"
}

# Text input
text = st.text_area(
    "Enter text to translate:",
    placeholder="Type your text here..."
)

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_name = st.selectbox(
        "Source language:",
        list(languages.keys())
    )

with col2:
    target_name = st.selectbox(
        "Target language:",
        list(languages.keys()),
        index=1
    )

# Translation
if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    elif source_name == target_name:
        st.info("Source and target languages are the same.")
        translated_text = text

    else:
        try:
            source_language = languages[source_name]
            target_language = languages[target_name]

            translator = Translator(
                from_lang=source_language,
                to_lang=target_language
            )

            translated_text = translator.translate(text)

            st.success("Translation completed!")

        except Exception as e:
            st.error("Translation failed. Please try again.")
            st.error(str(e))
            translated_text = None

    # Show translation
    if translated_text:
        st.subheader("Translated Text")

        st.code(translated_text)

        # Text-to-speech
        if st.button("🔊 Listen to Translation"):
            try:
                speech_language = languages[target_name]

                audio = gTTS(
                    text=translated_text,
                    lang=speech_language
                )

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                ) as audio_file:

                    audio.save(audio_file.name)

                    st.audio(
                        audio_file.name,
                        format="audio/mp3"
                    )

            except Exception as e:
                st.error(
                    "Text-to-speech is not available for this language."
                )