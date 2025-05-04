# Yerel Lehçe Eşleştirme

Bu proje, Türkiye'nin farklı şehirlerinde kullanılan ve aynı anlama gelen yerel kelimeleri eşleştirmeyi amaçlamaktadır. Eşleştirme işlemi, TDK Lehçe Sözlüğü'nden alınan kelimelerin Word2Vec ile vektörleştirilmesi ve semantik benzerliklerinin hesaplanması yoluyla gerçekleştirilir.

## 🔍 Problem Tanımı

Türkiye'de bölgesel olarak farklılık gösteren kelimeler, aynı anlamı taşısa da lehçelere göre değişiklik gösterebilir. Örneğin:

- "Bakraç" (Doğu Anadolu) ↔ "Kova" (Batı Anadolu)

Bu proje, bu tür eş anlamlı yerel kelimeleri otomatik olarak türkçe kullanımını gösteren bir model geliştirmeyi hedefler.

## 📚 Veri Kaynağı

- Dergiler ve belediyelerin yayınlamış olduğu yöresel kelimeler

## 🧠 Kullanılan Yöntemler

- **Word2Vec**: Kelimeleri vektör uzayında temsil etmek için kullanılır.
- **TF-IDF**:Her bir temizlenmiş veri seti için TF-IDF vektörleştirme 
işlemi ayrı ayrı yapılacaktır. 

## 🔧 Adımlar

1. **Veri Hazırlama**:
   - Bulunan 5 kaynaktan 
   - Temizleme ve ön işleme adımları uygulanır.

2. **Vektörleştirme**:
   - Word2Vec modeli kullanılarak kelimeler sayısal vektörlere dönüştürülür.

## 💻 Kullanım

```bash
# Gereksinimleri yükle
pip install -r requirements.txt

# Modeli çalıştır
python main.py

