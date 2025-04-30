import spacy

nlp_en = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp_en(text)
    return [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['GPE', 'LOC', 'EVENT']]
