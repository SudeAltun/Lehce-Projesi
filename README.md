# Yerel Lehçe Eşleştirme

Bu proje, Türkiye'nin farklı şehirlerinde kullanılan ve her yerde geçerli olan türkçe karşılığını bulmayı amaçlar . 5 farklı kaynakyan alınan kelimelerin Word2Vec ile vektörleştirilmesi ve semantik benzerliklerinin hesaplanması yoluyla gerçekleştirilir.

## 🧠 Problem Tanımı

Türkiye'de bölgesel olarak farklılık gösteren kelimeler, aynı anlamı taşısa da lehçelere göre değişiklik gösterebilir. Örneğin:

- "Bakraç" (Doğu Anadolu) ↔ "Kova" (Batı Anadolu)

Bu proje, bu tür eş anlamlı yerel kelimeleri otomatik olarak türkçe kullanımını gösteren bir model geliştirmeyi hedefler.

## 🗂️ Veri Kaynağı

- Dergiler ve belediyelerin yayınlamış olduğu yöresel kelimeler

## 🧠 Kullanılan Yöntemler

- **Word2Vec**: Kelimeleri vektör uzayında temsil etmek için kullanılır.
- **TF-IDF**:Her bir temizlenmiş veri seti için TF-IDF vektörleştirme 
işlemi ayrı ayrı yapılacaktır.
- **Pre-Processing**:
   • Stop word removal (gereksiz/sık kullanılan kelimelerin çıkarılması) 
   • Tokenization (noktalama işaretlerinin kaldırılması dâhil) 
   • Lowercasing (kelimelerin küçük harfe dönüştürülmesi) 
   • Lemmatization 
   • Stemming 
- **Zipf Yasası**:Ham veriye ait Zipf yasasına göre log-log grafiği çizilir. 

##  📦 Adımlar

1. **Veri Hazırlama**:
   - Bulunan 5 kaynaktan veri çekilir.
   - Temizleme ve ön işleme adımları uygulanır.

2. **Vektörleştirme**:
   - Word2Vec modeli kullanılarak kelimeler sayısal vektörlere dönüştürülür.
   -TF-IDF modeli kullanılarak Her bir temizlenmiş veri seti için TF-IDF vektörleştirme 
işlemi ayrı ayrı yapılacaktır.

## Kullanılan Kütüphaneler
- os
- pandas
- beautifulsoup4
- TurkishStemmer
- json
- fitz
- sklearn
- gensim
- numpy
- matplotlib
- nltk
- re
- collections
- bs4

## ⚙️ Modelin Oluşturulması (Adım Adım)

### 1. Reponun Klonlanması

```bash
git clone https://github.com/SudeAltun/Lehce-Projesi.git
cd Lehce-Projesi
```

### 2. Sanal Ortam Oluştur (Opsiyonel fakat önerilir)

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

### 4. Modeli Eğitme Script’ini Çalıştır
```bash
python Word2Vec.py
```

Tüm kütüphaneler requirements.txt dosyasında listelenmiştir.
Kurulum:
```bash
pip install -r requirements.txt
```

