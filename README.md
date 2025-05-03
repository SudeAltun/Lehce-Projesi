# Yerel Lehçe Eşleştirme

Bu proje, Türkiye'nin farklı şehirlerinde kullanılan ve aynı anlama gelen yerel kelimeleri eşleştirmeyi amaçlamaktadır. Eşleştirme işlemi, TDK Lehçe Sözlüğü'nden alınan kelimelerin Word2Vec ile vektörleştirilmesi ve semantik benzerliklerinin hesaplanması yoluyla gerçekleştirilir.

## 🔍 Problem Tanımı

Türkiye'de bölgesel olarak farklılık gösteren kelimeler, aynı anlamı taşısa da lehçelere göre değişiklik gösterebilir. Örneğin:

- "Bakraç" (Doğu Anadolu) ↔ "Kova" (Batı Anadolu)

Bu proje, bu tür eş anlamlı yerel kelimeleri otomatik olarak eşleştirebilecek bir model geliştirmeyi hedefler.

## 📚 Veri Kaynağı

- **TDK Lehçe Sözlüğü**: Türkiye'nin çeşitli bölgelerindeki yerel kelimeleri ve bu kelimelerin anlamlarını içeren resmi bir kaynaktır.

## 🧠 Kullanılan Yöntemler

- **Word2Vec**: Kelimeleri vektör uzayında temsil etmek için kullanılır.
- **Kosinüs Benzerliği**: Vektörler arası benzerliği ölçmek ve eşleştirme yapmak için kullanılır.

## 🔧 Adımlar

1. **Veri Hazırlama**:
   - TDK Lehçe Sözlüğü'nden kelimeler ve anlamları toplanır.
   - Temizleme ve ön işleme adımları uygulanır.

2. **Vektörleştirme**:
   - Word2Vec modeli kullanılarak kelimeler sayısal vektörlere dönüştürülür.

3. **Benzerlik Hesaplama**:
   - Her bir yerel kelimenin, diğer kelimelerle olan kosinüs benzerliği hesaplanır.
   - En yüksek benzerliğe sahip çiftler, eş anlamlı olarak eşleştirilir.

## 💻 Kullanım

```bash
# Gereksinimleri yükle
pip install -r requirements.txt

# Modeli çalıştır
python main.py
