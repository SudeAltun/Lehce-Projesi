import os
import pandas as pd
from preprocessing import on_isleme_pipeline  # Var olan işlem fonksiyonu

# Giriş dosyasının adı
input_file = "birlesik_sozluk.csv"
output_stemming_file = "stemming_veri.csv"
output_lemmatization_file = "lemmatization_veri.csv"

# Dosyanın varlığını kontrol et
if not os.path.exists(input_file):
    print(f"❌ HATA: '{input_file}' dosyası bulunamadı.")
    exit()

# Dosyayı oku
df = pd.read_csv(input_file, encoding="utf-8", sep=",", engine="python", quotechar='"', on_bad_lines='skip')

# Sütun adlarını kontrol et ve normalize et
df.columns = df.columns.str.strip().str.lower()

# "kelime" ve "anlam" sütununun varlığını kontrol et
if "kelime" not in df.columns or "anlam" not in df.columns:
    print("❌ HATA: 'kelime' veya 'anlam' sütunu bulunamadı. Mevcut sütunlar:", df.columns)
    exit()

# Yeni sütunlar için listeler
stemming_list = []
lemmatization_list = []

# Her yoruma ön işleme uygula
for anlam in df["anlam"]:
    try:
        # Pipeline'dan her iki işlem için sonuçları al
        sonuc = on_isleme_pipeline(str(anlam))

        # Stemming ve Lemmatization sonuçları
        stemming_list.append(" ".join(sonuc["stemmed"]))
        lemmatization_list.append(" ".join(sonuc["lemmas"]))
    except Exception as e:
        print(f"⚠️ Yorum işlenemedi: {e}")
        stemming_list.append("")
        lemmatization_list.append("")

# Sonuçları yeni sütunlara ekle
df["stemming"] = stemming_list
df["lemmatization"] = lemmatization_list

# Stemming ve Lemmatization dosyalarını kaydet
df[["kelime", "stemming"]].to_csv(output_stemming_file, index=False, encoding="utf-8", sep=";", quotechar='"')
df[["kelime", "lemmatization"]].to_csv(output_lemmatization_file, index=False, encoding="utf-8", sep=";", quotechar='"')

print(f"✅ 'stemming_veri.csv' ve 'lemmatization_veri.csv' dosyaları başarıyla kaydedildi.")
