import pandas as pd
from itertools import combinations

# CSV'den benzerlik sonuçlarını yükle
# Örnek: Word2Vec sonuçlarını birleştirdiğiniz dosya
df = pd.read_csv("merged_word2vec_results_lemmatized.csv")  # veya stemmed

# Giriş metninin indeksini belirt (genelde 0)
giris_index = 0

# Her modelin ilk 5 benzer sonucunu toplayan fonksiyon
def get_top5_sets(df, giris_index=0):
    top5_sets = {}
    for model in df["model_name"].unique():
        model_df = df[df["model_name"] == model]
        model_df = model_df.sort_values(by="similarity_score", ascending=False)
        top5 = set(model_df[model_df["document_index"] != giris_index].head(5)["document_index"])
        top5_sets[model] = top5
    return top5_sets

# Jaccard benzerliği fonksiyonu
def jaccard_similarity(set_a, set_b):
    return len(set_a & set_b) / len(set_a | set_b)

# Model çiftleri için Jaccard hesapla
def compute_jaccard_for_all(top5_sets):
    results = []
    for (model_a, set_a), (model_b, set_b) in combinations(top5_sets.items(), 2):
        sim = jaccard_similarity(set_a, set_b)
        results.append({
            "model_a": model_a,
            "model_b": model_b,
            "jaccard_similarity": round(sim, 4)
        })
    return pd.DataFrame(results)

# Uygula
top5_sets = get_top5_sets(df)
jaccard_df = compute_jaccard_for_all(top5_sets)

# Sonuçları göster
print(jaccard_df.sort_values(by="jaccard_similarity", ascending=False))

# CSV'ye kaydetmek istersen:
# jaccard_df.to_csv("jaccard_similarity_results.csv", index=False)
