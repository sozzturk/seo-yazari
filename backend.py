
import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env dosyasındaki şifreleri yükle
load_dotenv()

# Google API Anahtarını al ve yapılandır
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def metin_olustur(urun_adi, ozellikler, ton="Satış Odaklı"):
    """
    Google Gemini modeline bağlanıp ürün açıklamasını getiren fonksiyon.
    """
    
    # Model seçimi (Flash modeli hem hızlı hem ücretsiz kota dostudur)
    model =genai.GenerativeModel('models/gemini-2.5-flash')

    prompt = f"""
    Sen profesyonel bir e-ticaret SEO uzmanısın.
    Aşağıdaki ürün için {ton} bir dilde, SEO uyumlu, müşteriyi harekete geçiren,
    duygulara hitap eden bir ürün açıklaması yaz.
    
    Kurallar:
    1. Başlık kullanma, sadece açıklama metnini yaz.
    2. En az 3 tane popüler Instagram hashtag'i ekle.
    3. Emoji kullan.
    
    Ürün Adı: {urun_adi}
    Özellikler: {ozellikler}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"