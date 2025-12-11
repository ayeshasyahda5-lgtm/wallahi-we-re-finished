import streamlit as st

st.title("Dataset Saham Indonesia✦")
st.write("##### Anggota Kelompok ฅ^>⩊<^ฅ =")
st.write("- Ayesha Syahda Ardiningrum")
st.write("- Fitriannisaa Nabila")
st.write("- Helmi Sulfa Yulidiawati")
st.write("- Ade Febriani")

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("### Pendahuluan")

st.markdown(
    """
    Dataset saham yang digunakan dalam penelitian atau proyek ini berisi daftar perusahaan publik di Indonesia lengkap dengan atribut seperti kode emiten, nama perusahaan, jumlah saham beredar (shares), kategori papan pencatatan, hingga harga penutupan terakhir (LastPrice). Informasi-informasi tersebut memberikan gambaran awal mengenai kondisi masing-masing perusahaan serta memungkinkan berbagai jenis analisis, mulai dari distribusi harga saham, perbedaan karakter perusahaan berdasarkan papan pencatatan, hingga pola pergerakan saham secara umum.

Dengan pendekatan visualisasi dan analisis data, dataset ini tidak hanya membantu menggambarkan struktur pasar secara lebih jelas, tetapi juga memudahkan pembaca—baik akademisi, praktisi, maupun pemula di dunia pasar modal—untuk memahami bagaimana penyebaran harga dan karakteristik emiten di Indonesia. Pendekatan yang lebih sederhana namun tetap sistematis diharapkan dapat menjembatani analisis akademis dengan interpretasi yang mudah dipahami dan relevan bagi banyak kalangan.

    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("### Deskripsi Data")

st.markdown(
    """
    Dataset yang dianalisis terdiri dari 300 baris data dengan empat variabel utama:
    """
)
st.markdown(
    """
   - Tahun (2010–2024)
Data tahun tidak berurutan karena diambil secara acak, tetapi tetap berada dalam rentang 2010 sampai 2024. Variabel ini berfungsi sebagai konteks waktu terhadap data ekonomi.
    """
)
st.markdown(
    """
   - PDB
Nilai PDB dalam dataset berada di sekitar kisaran 10.000–14.000, menunjukkan variasi ekonomi yang cukup luas. Nilai ini merupakan angka simulasi yang menyerupai pola pertumbuhan ekonomi Indonesia.
    """
)
st.markdown(
    """
  - Inflasi (%)
Inflasi berada pada kisaran 2% – 5%, mencerminkan kondisi stabil dan realistis sebagaimana rata-rata inflasi Indonesia dalam 10 tahun terakhir.
    """
)
st.markdown(
    """
 - IHSG
Nilai IHSG berada di rentang 6.000–7.500, yang merepresentasikan pergerakan umum pasar saham Indonesia.
    """
)