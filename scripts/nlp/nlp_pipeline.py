from data_collector import collect_articles, collect_tweets
from multilingual_nlp import translate_nepali_to_english
from summarization import generate_summary
from sentiment_analysis import analyze_sentiment_transformer
from ner import extract_entities
from topic_modeling import perform_topic_modeling

def run_nlp_pipeline():
    # Step 1: Collect Data
    urls = [
        "https://example.com/climate-news-1",
        "https://example.com/climate-news-2"
    ]
    tweets = collect_tweets("climate change nepal", max_results=50)
    articles = collect_articles(urls)

    raw_texts = articles + tweets

    # Step 2: Translate Nepali to English if needed
    translated_texts = [translate_nepali_to_english(text) for text in raw_texts]

    # Step 3: Generate Summaries
    summaries = [generate_summary(text) for text in translated_texts]

    # Step 4: Sentiment Analysis
    sentiments = [analyze_sentiment_transformer(text) for text in translated_texts]

    # Step 5: Named Entity Recognition
    all_entities = [extract_entities(text) for text in translated_texts]

    # Step 6: Topic Modeling
    topics = perform_topic_modeling(translated_texts, n_topics=5)

    # Step 7: Integration-ready output
    results = []
    for i, text in enumerate(translated_texts):
        result = {
            "original_text": raw_texts[i],
            "translated": text,
            "summary": summaries[i],
            "sentiment": sentiments[i],
            "entities": all_entities[i]
        }
        results.append(result)

    print("Sample NLP Insight:")
    for i, r in enumerate(results[:3]):
        print(f"\n--- Document {i + 1} ---")
        print("Summary:", r['summary'])
        print("Sentiment:", r['sentiment'])
        print("Entities:", r['entities'])

    print("\nIdentified Topics:")
    for i, topic in enumerate(topics):
        print(f"Topic {i + 1}: {', '.join(topic)}")

if __name__ == "__main__":
    run_nlp_pipeline()
