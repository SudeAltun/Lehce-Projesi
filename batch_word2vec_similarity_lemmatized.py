import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import os

# Veri dosyası
text_path = "lemmatization_veri.csv"

# Model konfigürasyonları
model_configs = [
    {'model_type': 'cbow', 'window': 2, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 100},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 100},
    {'model_type': 'cbow', 'window': 2, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 2, 'vector_size': 300},
    {'model_type': 'cbow', 'window': 4, 'vector_size': 300},
    {'model_type': 'skipgram', 'window': 4, 'vector_size': 300},
]

# Metinleri yükle
text_df = pd.read_csv(text_path)
text_df = text_df["kelime;lemmatization"].str.split(";", n=1, expand=True)[1].fillna("")
n_samples = len(text_df)

# Ortalama vektör hesaplama fonksiyonu
def sentence_vector(sentence, model):
    vectors = [model.wv[word] for word in sentence.split() if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

# Tüm sonuçları biriktireceğimiz liste
all_results = []

# Her model için işlem
for config in model_configs:
    model_type = config['model_type']
    window = config['window']
    vector_size = config['vector_size']
    model_file = f"word2vec_lemmatized_{model_type}_win{window}_dim{vector_size}.model"

    if not os.path.exists(model_file):
        print(f"❌ Model bulunamadı: {model_file}")
        continue

    print(f"\n🚀 İşleniyor: {model_file}")
    model = Word2Vec.load(model_file)

    sentence_vectors = np.array([sentence_vector(text, model) for text in text_df])
    query_vector = sentence_vectors[0].reshape(1, -1)
    similarities = cosine_similarity(query_vector, sentence_vectors)[0]

    df = pd.DataFrame({
        "model_name": model_file,
        "document_index": range(n_samples),
        "similarity_score": similarities,
        "comment": text_df
    })

    all_results.append(df)

    # Terminal çıktısı: en benzer 5 yorum
    top5 = df.sort_values(by="similarity_score", ascending=False).iloc[1:6]
    print(f"🎯 Giriş Yorumu [0]:\n{text_df[0]}\n")
    print("🔗 En Benzer Yorumlar:\n")
    for _, row in top5.iterrows():
        print(f"🔸 Yorum [{int(row['document_index'])}] (Skor: {row['similarity_score']:.4f}):\n{row['comment']}\n")

# Tek bir CSV'ye kaydet
if all_results:
    final_df = pd.concat(all_results, ignore_index=True)
    final_df.to_csv("merged_word2vec_results_lemmatized.csv", index=False)
    print("\n✅ Tüm sonuçlar 'merged_word2vec_results_lemmatized.csv' dosyasına kaydedildi.")
