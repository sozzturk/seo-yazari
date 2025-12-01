import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("--- Google API Testi Başlıyor ---")

try:
    print("Erişilebilir modeller aranıyor...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Buldum: {m.name}")
            
    print("--- Test Bitti ---")
except Exception as e:
    print(f"Hata oluştu: {e}")