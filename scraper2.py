import re
import json

def extract_words_to_json(pdf_path, json_output_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    # Kelime - anlam eşleşmelerini yakala
    pattern = re.findall(r"([A-ZÇĞİÖŞÜ][a-zçğıöşüA-ZÇĞİÖŞÜ\- ]+):\s+([^\n]+)", text)

    # Listeyi sözlükler listesi hâline getir
    words_list = [{"kelime": k.strip(), "anlam": v.strip()} for k, v in pattern]

    # JSON dosyasına yaz
    with open(json_output_path, "w", encoding="utf-8") as json_file:
        json.dump(words_list, json_file, ensure_ascii=False, indent=2)

    print(f"{len(words_list)} kelime başarıyla {json_output_path} dosyasına kaydedildi.")

# Kullanım
extract_words_to_json("Ci