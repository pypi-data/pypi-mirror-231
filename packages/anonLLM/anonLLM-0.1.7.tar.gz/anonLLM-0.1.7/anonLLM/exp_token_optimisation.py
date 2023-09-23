import spacy
import subprocess

# Dictionary to map language codes to spaCy language models
LANGUAGE_MODELS = {
    'en': 'en_core_web_sm',
    'es': 'es_core_news_sm',
    'de': 'de_core_news_sm',
    'fr': 'fr_core_news_sm',
    'pt': 'pt_core_news_sm',
    # Add more languages here
}


def download_model_if_not_exists(lang_code):
    model_name = LANGUAGE_MODELS.get(lang_code)
    if model_name is None:
        print(f"Language code {lang_code} not supported.")
        return False

    try:
        spacy.load(model_name)
        return True
    except OSError:
        print(f"Downloading language model for {lang_code}")
        subprocess.run(["python", "-m", "spacy", "download", model_name])
        return True


def remove_stopwords_and_punctuation_spacy(text, lang_code):
    if not download_model_if_not_exists(lang_code):
        return text

    # Load the appropriate language model
    nlp = spacy.load(LANGUAGE_MODELS[lang_code])

    # Process the text through spaCy NLP pipeline
    doc = nlp(text)

    # Generate filtered text
    filtered_text = " ".join([token.text for token in doc if not token.is_stop and token.text != "."])

    return filtered_text


# Test the function with English text
text_en = "Write a poem about resilience. I am experiencing a lot of loneliness and frustration. I am working on my programming skills but I feel like I still hit roadblocks. After months and months of work I am still frustrated by the amount of stuff I can't do. I lack motivation today and feel like a failure. I need a poem to boost my morale. Write if for me."
result_en = remove_stopwords_and_punctuation_spacy(text_en, 'en')
print("English:", result_en)

# Test the function with Spanish text
# text_es = "El zorro marrón rápido salta sobre el perro perezoso."
# result_es = remove_stopwords_and_punctuation_spacy(text_es, 'es')
# print("Spanish:", result_es)

# Add more tests for other languages
