import pandas as pd
import os
import re

# Girdi ve çıktı dosya yolları
input_file = r"C:\Users\asus\Desktop\Kod\data\stemming_data.csv"
output_file = r"C:\Users\asus\Desktop\Kod\data\stemming_clean.csv"

# Dosya var mı kontrolü
if not os.path.exists(input_file):
    print(f"HATA: Dosya bulunamadı: {input_file}")
else:
    try:
        # CSV dosyasını oku (nokt. yerine ; kullanıldığı için sep=';' önemli!)
        df = pd.read_csv(input_file, sep=';')

        # 'stemming' sütunu varsa temizleme işlemi yapılır
        if 'stemming' in df.columns:
            # Temizleme: Küçük harfe çevir, noktalama sil, boşlukları düzelt
            df['text'] = df['stemming'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x).lower()).strip())

            # Yalnızca temiz sütunu yazdır
            df[['text']].to_csv(output_file, index=False)
            print(f"✅ Temiz stemming verisi kaydedildi: {output_file}")
        else:
            print("HATA: 'stemming' adında bir sütun bulunamadı.")
    except Exception as e:
        print(f"HATA: İşlem sırasında bir hata oluştu: {e}")
import pandas as pd
import os
import re

# Girdi dosyasının yolu (ayarla)
input_file = r"C:\Users\asus\Desktop\Kod\data\lemmatized.csv"
output_file = r"C:\Users\asus\Desktop\Kod\data\lemmatized_clean.csv"

# Dosya mevcut mu kontrol et
if not os.path.exists(input_file):
    print(f"HATA: Dosya bulunamadı: {input_file}")
else:
    try:
        # Dosyayı oku (nokt. yerine ; kullanıldığı için sep=';' önemli!)
        df = pd.read_csv(input_file, sep=';')

        # Eğer 'lemmatization' sütunu varsa işleme devam
        if 'lemmatization' in df.columns:
            # Temizleme işlemi: Küçük harf, noktalama temizleme, extra boşlukları kaldır
            df['text'] = df['lemmatization'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x).lower()).strip())

            # Sadece temiz sütunu kaydet
            df[['text']].to_csv(output_file, index=False)
            print(f"✅ Temiz veri başarıyla kaydedildi: {output_file}")
        else:
            print("HATA: 'lemmatization' adında bir sütun bulunamadı.")
    except Exception as e:
        print(f"HATA: İşlem sırasında bir hata oluştu: {e}")