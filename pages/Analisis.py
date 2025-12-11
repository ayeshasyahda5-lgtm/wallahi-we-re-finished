import streamlit as st

st.title("Analisis Data")
st.write("### Berikut adalah hasil Analisis data kami: ")

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.markdown(
    """
   Menarik benang merah dari ketiga visualisasi di atas, terdapat pola segmentasi pasar yang jelas.
Pertama, struktur pasar saham Indonesia sangat heterogen. Dominasi papan "Pengembangan" mengindikasikan bahwa bursa kita sedang didorong oleh perusahaan-perusahaan skala menengah yang memiliki potensi pertumbuhan tinggi, bukan hanya didominasi oleh raksasa korporasi (Papan Utama).
Kedua, terdapat hubungan terbalik yang menarik (meski perlu uji korelasi lebih lanjut) antara grafik "Jumlah Lembar Saham" dan "Harga Saham Tertinggi". Emiten yang memiliki harga per lembar sangat tinggi (di grafik ketiga) jarang muncul sebagai emiten dengan jumlah lembar saham terbanyak (di grafik kedua). Sebaliknya, emiten dengan miliaran lembar saham seringkali memiliki harga nominal yang lebih rendah. Ini menunjukkan karakteristik profil risiko dan tipe investor yang berbeda; saham harga tinggi biasanya diburu untuk investasi jangka panjang, sementara saham dengan volume lembar melimpah seringkali menjadi sasaran pedagang harian karena likuiditasnya.
    """
)