from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ne-en")

def translate_nepali_to_english(text):
    try:
        result = translator(text, max_length=512)
        return result[0]['translation_text']
    except Exception as e:
        print(f"Translation error: {e}")
        return text
