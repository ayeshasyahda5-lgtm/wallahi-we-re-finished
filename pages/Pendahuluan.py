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
<<<<<<< HEAD
    Dalam era big data saat ini, kemampuan untuk menyajikan data pasar modal yang kompleks menjadi informasi yang mudah dicerna sangatlah krusial. Proyek ini berfokus pada pengembangan dashboard interaktif berbasis web menggunakan framework Streamlit dan lingkungan Jupyter Lab. Tujuan utamanya adalah melakukan eksplorasi statistik deskriptif terhadap data saham emiten di Indonesia.
Data yang digunakan mencakup variabel kunci seperti kode saham, nama emiten, jumlah lembar saham (shares outstanding), papan pencatatan (listing board), serta harga penutupan terakhir (last price). Melalui pendekatan visualisasi data, kita mencoba membedah struktur pasar saham saat ini, mulai dari segmentasi papan pencatatan hingga identifikasi saham-saham dengan valuasi harga tertinggi maupun volume lembar terbanyak. Laporan ini akan menguraikan temuan-temuan yang didapat dari grafik yang telah di-generate oleh sistem.
=======
    Dataset saham yang digunakan dalam penelitian atau proyek ini berisi daftar perusahaan publik di Indonesia lengkap dengan atribut seperti kode emiten, nama perusahaan, jumlah saham beredar (shares), kategori papan pencatatan, hingga harga penutupan terakhir (LastPrice). Informasi-informasi tersebut memberikan gambaran awal mengenai kondisi masing-masing perusahaan serta memungkinkan berbagai jenis analisis, mulai dari distribusi harga saham, perbedaan karakter perusahaan berdasarkan papan pencatatan, hingga pola pergerakan saham secara umum.

Dengan pendekatan visualisasi dan analisis data, dataset ini tidak hanya membantu menggambarkan struktur pasar secara lebih jelas, tetapi juga memudahkan pembaca—baik akademisi, praktisi, maupun pemula di dunia pasar modal—untuk memahami bagaimana penyebaran harga dan karakteristik emiten di Indonesia. Pendekatan yang lebih sederhana namun tetap sistematis diharapkan dapat menjembatani analisis akademis dengan interpretasi yang mudah dipahami dan relevan bagi banyak kalangan.
>>>>>>> f00fdec2c09c91a2c407e03c93f20b715a0d149f

    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("### Deskripsi Data")


st.markdown(
    """
   Data yang digunakan dalam simulasi dashboard ini merupakan data sekunder yang merekam profil dan aktivitas pasar saham emiten di Indonesia. Dataset ini disusun dalam format terstruktur (structured data) yang mencakup lima variabel kunci untuk setiap emiten.
Variabel pertama dan kedua berfungsi sebagai identitas unik, yaitu Kode Saham (Code) yang terdiri dari empat huruf kapital (seperti AALI, BBCA) dan Nama Perusahaan (Name) yang memuat nama lengkap badan usaha tersebut.  
Untuk keperluan analisis segmentasi pasar, dataset ini menyertakan variabel Papan Pencatatan (Listing Board). Variabel ini bersifat kategorikal yang mengklasifikasikan emiten ke dalam kelompok papan "Utama", "Pengembangan", atau "Akselerasi" sesuai dengan skala bisnis mereka.  
Sementara itu, untuk analisis kuantitatif, terdapat dua metrik finansial utama:

- Jumlah Saham (Shares): Merepresentasikan total lembar saham yang beredar (shares outstanding) milik emiten, yang angkanya bervariasi dari ratusan juta hingga miliaran lembar.  

- Harga Terakhir (Last Price): Menunjukkan harga penutupan pasar per lembar saham dalam satuan Rupiah, yang menjadi indikator valuasi terkini emiten tersebut.
    """
)
