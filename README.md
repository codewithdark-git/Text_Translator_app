# Text Translator

The Text Translator is a simple web application built using Streamlit and Google Translate API. It allows users to translate text from one language to another easily.

## Features

- Translation of text from one language to another.
- Selection of target language from a dropdown menu.
- Customizable Streamlit theme for a better user experience.
- Error handling for translation failures.

## Setup

To run the Text Translator locally, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/codewithdark-git/text-translator.git
   ```

2. Navigate to the project directory.
   ```bash
   cd text-translator
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

5. Access the Text Translator in your web browser at `http://localhost:8501`.

## Usage

1. Enter the text you want to translate in the text area provided.
2. Select the target language from the dropdown menu.
3. Click the "Translate" button to initiate the translation.
4. View the translated text displayed below.

## Dependencies

- Streamlit
- Googletrans

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
