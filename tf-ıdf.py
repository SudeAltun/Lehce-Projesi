import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Dosya yolları
lemmatized_file = "lemmatization_veri.csv"
stemmed_file = "stemming_veri.csv"

# CSV dosyalarını oku ve ";" ile ayır
lemmatized_df = pd.read_csv(lemmatized_file)
stemmed_df = pd.read_csv(stemmed_file)

lemmatized_df = lemmatized_df["kelime;lemmatization"].str.split(";", n=1, expand=True)
lemmatized_df.columns = ["kelime", "metin"]

stemmed_df = stemmed_df["kelime;stemming"].str.split(";", n=1, expand=True)
stemmed_df.columns = ["kelime", "metin"]

# Boş olmayan metinleri filtrele
lemmatized_texts = lemmatized_df["metin"].dropna().astype(str)
stemmed_texts = stemmed_df["metin"].dropna().astype(str)

lemmatized_texts = [text for text in lemmatized_texts if text.strip()]
stemmed_texts = [text for text in stemmed_texts if text.strip()]

# TF-IDF vektörleştiricileri tanımla
lemmatized_vectorizer = TfidfVectorizer()
stemmed_vectorizer = TfidfVectorizer()

# TF-IDF matrislerini oluştur
lemmatized_tfidf = lemmatized_vectorizer.fit_transform(lemmatized_texts)
stemmed_tfidf = stemmed_vectorizer.fit_transform(stemmed_texts)

# DataFrame'e çevir
lemmatized_df_tfidf = pd.DataFrame(
    lemmatized_tfidf.toarray(),
    columns=lemmatized_vectorizer.get_feature_names_out()
)

stemmed_df_tfidf = pd.DataFrame(
    stemmed_tfidf.toarray(),
    columns=stemmed_vectorizer.get_feature_names_out()
)

# CSV olarak kaydet
lemmatized_df_tfidf.to_csv("tfidf_lemmatized.csv", index=False)
stemmed_df_tfidf.to_csv("tfidf_stemmed.csv", index=False)

print("TF-IDF dosyaları başarıyla kaydedildi.")
