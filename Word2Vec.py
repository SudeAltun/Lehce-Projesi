from gensim.models import Word2Vec
import pandas as pd
import time
import json

# CSV'den metinleri yükleyip cümle listesine dönüştür
def load_texts(path, column_name):
    df = pd.read_csv(path)
    df = df[column_name].str.split(";", n=1, expand=True)
    df.columns = ["kelime", "metin"]
    texts = df["metin"].dropna().astype(str).tolist()
    return [text.strip().split() for text in texts if text.strip()]

# Parametre setleri
parameters = [
    {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 300},
]

# Test edilecek kelimeler
test_words = ["su", "adam", "kadın", "masa", "güç"]

# Model eğitimi fonksiyonu
def train_models(sentences, data_type):
    results = []

    for params in parameters:
        sg = 1 if params["model_type"] == "skipgram" else 0
        vector_size = params["vector_size"]
        window = params["window"]
        model_name = f"word2vec_{data_type}_{params['model_type']}_win{window}_dim{vector_size}.model"

        print(f"Eğitiliyor: {model_name}")
        start = time.time()

        model = Word2Vec(
            sentences=sentences,
            vector_size=vector_size,
            window=window,
            sg=sg,
            min_count=1,
            workers=4,
            epochs=20
        )
        model.save(model_name)
        duration = time.time() - start

        word_results = {}
        for word in test_words:
            try:
                similar = model.wv.most_similar(word, topn=5)
                word_results[word] = similar
            except KeyError:
                word_results[word] = "Kelime bulunamadı"

        results.append({
            "model_name": model_name,
            "vector_size": vector_size,
            "window": window,
            "sg": sg,
            "training_time_sec": round(duration, 2),
            "similar_words": word_results
        })

    return results

# Verileri yükle
lemmatized_sentences = load_texts("lemmatization_veri.csv", "kelime;lemmatization")
stemmed_sentences = load_texts("stemming_veri.csv", "kelime;stemming")

# Modelleri eğit ve sonuçları al
lemmatized_results = train_models(lemmatized_sentences, "lemmatized")
stemmed_results = train_models(stemmed_sentences, "stemmed")

# Sonuçları JSON dosyasına kaydet
with open("word2vec_results.json", "w", encoding="utf-8") as f:
    json.dump({
        "lemmatized": lemmatized_results,
        "stemmed": stemmed_results
    }, f, ensure_ascii=False, indent=4)

print("Tüm modeller eğitildi ve sonuçlar word2vec_results.json dosyasına kaydedildi.")
