import re
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from TurkishStemmer import TurkishStemmer

# Gerekli ayarlar
stop_words_tr = stopwords.words("turkish")
stop_words_en = stopwords.words("english")
stop_words = set(stop_words_tr + stop_words_en)

lemmatizer = WordNetLemmatizer()
stemmer = TurkishStemmer()

def on_isleme_pipeline(metin):
    orijinal = metin

    # 1. Küçük harfe çevirme
    metin = metin.lower()

    # 2. HTML etiketlerini temizleme
    metin = BeautifulSoup(metin, "html.parser").get_text()

    # 3. Noktalama ve sayıları kaldırma
    metin = re.sub(r"\d+", "", metin)
    metin = re.sub(f"[{re.escape(string.punctuation)}]", " ", metin)
    metin = re.sub(r"\s+", " ", metin).strip()

    # 4. Tokenization
    tokens = word_tokenize(metin, language="turkish")

    # 5. Stop words çıkarma
    tokens = [t for t in tokens if t not in stop_words]

    # 6. Lemmatization (sınırlı etkili olabilir Türkçede)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # 7. Stemming
    stemmed = [stemmer.stem(token) for token in lemmas]

    return {
        "orijinal": orijinal,
        "lowercase": metin,
        "tokens": tokens,
        "lemmas": lemmas,
        "stemmed": stemmed
    }
