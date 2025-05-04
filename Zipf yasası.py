import json
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# JSON verisini oku
with open("birlesik_sozluk.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# "anlam" alanlarını birleştir
texts = [entry.get("anlam", "") for entry in data if isinstance(entry.get("anlam", ""), str)]
all_text = " ".join(texts)
tokens = all_text.split()

# Kontrol çıktısı
print(f"Toplam kelime sayısı: {len(tokens)}")
print(f"Farklı kelime sayısı: {len(set(tokens))}")

# Zipf analizi
word_counts = Counter(tokens)
sorted_counts = sorted(word_counts.values(), reverse=True)
ranks = np.arange(1, len(sorted_counts) + 1)

# Grafik çizimi
plt.figure(figsize=(10, 6))
plt.loglog(ranks, sorted_counts, marker=".")
plt.title("Zipf Yasası - Log-Log Grafiği (Anlamlar üzerinden)")
plt.xlabel("Kelime Sırası (Rank)")
plt.ylabel("Kelime Frekansı")
plt.grid(True)
plt.tight_layout()
plt.show()