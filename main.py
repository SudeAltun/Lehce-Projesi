import os
import pandas as pd
from preprocessing import on_isleme_pipeline

# Giriş dosyasının adı
input_file = "birlesik_sozluk.csv"
output_file = "yorumlar_on_islemli.csv"

# Dosyanın varlığını kontrol et
if not os.path.exists(input_file):
    print(f"❌ HATA: '{input_file}' dosyası bulunamadı.")
    exit()

# Dosyayı oku
try:
    df = pd.read_csv(input_file, encoding="utf-8", sep=",", engine="python", quotechar='"', on_bad_lines='skip')
except UnicodeDecodeError:
    print("⚠️ UTF-8 ile okunamadı, ISO-8859-9 ile tekrar deneniyor...")
    try:
        df = pd.read_csv(input_file, encoding="ISO-8859-9", sep=",", engine="python", quotechar='"',
                         on_bad_lines='skip')
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")
        exit()
except Exception as e:
    print(f"❌ Dosya okuma hatası: {e}")
    exit()

# Sütun adlarını kontrol et ve normalize et
print("Sütun adları:", df.columns)
df.columns = df.columns.str.strip().str.lower()  # Boşlukları kaldır, küçük harfe çevir

# "kelime" ve "anlam" sütununun varlığını kontrol et
if "kelime" not in df.columns or "anlam" not in df.columns:
    print("❌ HATA: 'kelime' veya 'anlam' sütunu bulunamadı. Mevcut sütunlar:", df.columns)
    exit()

# Yeni sütunlar için listeler
lowercase_list = []
tokens_list = []
lemmas_list = []
stemmed_list = []

# Her yoruma ön işleme uygula
print("🔄 Yorumlar işleniyor...")
for i, anlam in enumerate(df["anlam"]):
    try:
        anlam_str = str(anlam)

        # Tokenize etmeden önce tekrar eden kelimeleri engellemek için her kelimeyi eşsiz yapıyoruz
        kelimeler = anlam_str.split()  # Anlamdaki kelimeleri ayır
        kelimeler = list(set(kelimeler))  # 'set' kullanarak benzersiz hale getir
        anlam_str = " ".join(kelimeler)  # Tekrarları engellenmiş anlam

        # Pipeline işleminden sonra anlamın yeniden düzenlenmesi
        sonuc = on_isleme_pipeline(anlam_str)

        # Her bir işlemde, bir anlam için 5 tane tekrar edilmesini engellemek
        lowercase_list.append(sonuc["lowercase"])
        tokens_list.append(" ".join(sorted(set(sonuc["tokens"]))))  # Tokenleri benzersiz yap
        lemmas_list.append(" ".join(sorted(set(sonuc["lemmas"]))))  # Lemmatize edilmiş kelimeleri benzersiz yap
        stemmed_list.append(" ".join(sorted(set(sonuc["stemmed"]))))  # Stemmed kelimeleri benzersiz yap

    except Exception as e:
        print(f"⚠️ {i}. anlam işlenemedi: {e}")
        lowercase_list.append("")
        tokens_list.append("")
        lemmas_list.append("")
        stemmed_list.append("")

# Sonuçları yeni sütunlara ekle
df["lowercase"] = lowercase_list
df["tokens"] = tokens_list
df["lemmas"] = lemmas_list
df["stemmed"] = stemmed_list

# Yeni CSV olarak kaydet
try:
    df.to_csv(output_file, index=False, encoding="utf-8", sep=";", quotechar='"')
    print("✅ Tüm yorumlara ön işleme başarıyla uygulandı ve 'yorumlar_on_islemli.csv' dosyasına kaydedildi.")
except Exception as e:
    print(f"❌ CSV kaydetme hatası: {e}")
