import streamlit as st
from backend import metin_olustur # Yazdığımız motoru buraya çağırdık
from streamlit_extras.st_copy_to_clipboard import st_copy_to_clipboard

# Sayfa Ayarları
st.set_page_config(page_title="AI İçerik Sihirbazı", page_icon="🚀")

# Başlık ve Alt Başlık
st.title("🚀 E-Ticaret Ürün Açıklaması Sihirbazı")
st.markdown("""
Bu araç, ürünleriniz için **SEO uyumlu** ve **satış odaklı** açıklamaları saniyeler içinde yazar.
""")

st.divider() # Çizgi çek

# Sol ve Sağ sütun oluştur (Görünüm düzeni)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Ürün Bilgileri")
    urun_adi = st.text_input("Ürün Adı", placeholder="Örn: Deri Cüzdan")
    ozellikler = st.text_area("Özellikler (Virgülle ayırın)", placeholder="Siyah, hakiki deri, 5 kart bölmesi...", height=150)
    ton = st.selectbox("Metin Tonu", ["Satış Odaklı", "Eğlenceli", "Resmi", "Bilgilendirici"])
    
    olustur_btn = st.button("✨ Açıklamayı Oluştur", type="primary")

with col2:
    st.subheader("Sonuç")
    
    if olustur_btn:
        if not urun_adi or not ozellikler:
            st.warning("Lütfen ürün adı ve özelliklerini giriniz.")
        else:
            with st.spinner("Yapay zeka düşünüyor..."):
                # Backend dosyasındaki fonksiyonu çalıştır
                sonuc = metin_olustur(urun_adi, ozellikler, ton)
                # ... diğer kodlar ...

    # Metin varsa göster
    if sonuc:
        st.markdown("### 📝 Oluşturulan Ürün Açıklaması")
        
        # Metni bir alana yerleştirme
        st.text_area("Kopyalamak İçin Tıklayın", sonuc, height=300)
        
        # Kopyalama butonunu ekle
        st_copy_to_clipboard(sonuc, 'Kopyalandı! 📋')
                   

# Alt bilgi
st.markdown("---")
st.markdown("© 2025 AI Writer App | Python ile geliştirildi")


