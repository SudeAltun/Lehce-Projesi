import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Dosya yolları
output_stemming_file = r"C:\Users\asus\Desktop\Kod\stemming_veri.csv"
output_lemmatization_file = r"C:\Users\asus\Desktop\Kod\lemmatization_veri.csv"

# Dosyanın mevcut olup olmadığını kontrol et
if not os.path.exists(output_stemming_file):
    print(f"❌ Dosya bulunamadı: {output_stemming_file}")
    exit()  # Eğer dosya bulunamazsa, işlem sonlandırılır

if not os.path.exists(output_lemmatization_file):
    print(f"❌ Dosya bulunamadı: {output_lemmatization_file}")
    exit()  # Eğer dosya bulunamazsa, işlem sonlandırılır

# Dosyaları oku
try:
    df_stemming = pd.read_csv(output_stemming_file, encoding="utf-8", sep=";")
    df_lemmatization = pd.read_csv(output_lemmatization_file, encoding="utf-8", sep=";")
    print("✅ Dosyalar başarıyla yüklendi.")
except Exception as e:
    print(f"❌ Dosya okuma hatası: {e}")
    exit()


# Zipf grafiği çizme fonksiyonu
def plot_zipf_distribution(df, column_name):
    """
    Verilen dataframe'den belirtilen sütunu alarak Zipf grafiğini çizen fonksiyon.
    """
    # Sütunu tokenize et ve kelimelerin sıklıklarını say
    all_words = " ".join(df[column_name].dropna()).split()
    word_counts = Counter(all_words)

    # En sık kullanılan kelimeleri sırala
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Kelimelerin sıklıklarını al
    words, counts = zip(*sorted_word_counts)

    # Zipf Grafiğini çiz
    plt.figure(figsize=(10, 6))
    sns
