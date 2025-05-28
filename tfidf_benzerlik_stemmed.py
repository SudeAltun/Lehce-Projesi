import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Dosya yolları
tfidf_path = "tfidf_stemmed.csv"
text_path = "stemming_veri.csv"

# TF-IDF vektörlerini oku
tfidf_df = pd.read_csv(tfidf_path, index_col=0)
tfidf_matrix = tfidf_df.values
n_samples = len(tfidf_df)

# Metinleri oku ve hizala
text_df = pd.read_csv(text_path)
text_df = text_df["kelime;stemming"].str.split(";", n=1, expand=True)[1].fillna("")

# Uzunlukları eşitle (güvenli hale getir)
if len(text_df) < n_samples:
    missing = n_samples - len(text_df)
    text_df = pd.concat([text_df, pd.Series([""] * missing)], ignore_index=True)
elif len(text_df) > n_samples:
    text_df = text_df[:n_samples]

# Giriş vektörü (ilk cümle)
query_vector = tfidf_matrix[0].reshape(1, -1)

# Cosine similarity hesapla
similarities = cosine_similarity(query_vector, tfidf_matrix)[0]

# Tüm skorları tabloya al
all_results = pd.DataFrame({
    "document_index": range(n_samples),
    "similarity_score": similarities,
    "comment": text_df
})

# CSV olarak kaydet
all_results.to_csv("similarity_results_stemmed.csv", index=False)
print("📁 Tüm benzerlik skorları 'similarity_results_stemmed.csv' dosyasına kaydedildi.\n")

# En benzer 5 yorumu yazdır
top5 = all_results.sort_values(by="similarity_score", ascending=False).iloc[1:6]

print(f"🎯 Giriş Yorumu [0]:\n{text_df[0]}\n")
print("🔗 En Benzer Yorumlar:\n")
for _, row in top5.iterrows():
    print(f"🔸 Yorum [{int(row['document_index'])}] (Skor: {row['similarity_score']:.4f}):\n{row['comment']}\n")
