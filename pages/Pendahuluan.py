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
    Dalam era saat ini, kemampuan untuk menyajikan data pasar modal yang kompleks menjadi informasi yang mudah dicerna sangatlah penting untuk di pelajari. Proyek tugas ini berfokus pada pengembangan dashboard  berbasis web menggunakan framework Streamlit dan lingkungan Jupyter Lab. Tujuan pyoyek ini adalah melakukan eksplorasi statistik deskriptif terhadap data saham yang ada di Indonesia.
Data yang digunakan sebagai variabel kunci seperti kode saham, nama emiten, jumlah lembar saham (shares outstanding), papan pencatatan (listing board), serta harga penutupan terakhir (last price). Melalui pendekatan visualisasi data, kita mencoba membedah struktur pasar saham saat ini, mulai dari segmentasi papan pencatatan hingga identifikasi saham-saham dengan valuasi harga tertinggi maupun volume lembar terbanyak. Laporan ini akan menguraikan temuan-temuan yang didapat dari grafik yang telah di-generate oleh sistem.

    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("### Deskripsi Data")


st.markdown(
    """
   Data yang digunakan dalam simulasi dashboard ini merupakan data sekunder yang merekam profil dan aktivitas pasar saham emiten di Indonesia. Dataset ini disusun oleh lima variabel kunci dengan format terstruktur (structured data) untuk setiap emiten.
Variabel pertama dan kedua berfungsi sebagai identitas unik, yaitu Kode Saham (Code) yang terdiri dari empat huruf kapital (seperti AALI, BBCA) dan Nama Perusahaan (Name) yang memuat nama lengkap badan usaha-usaha yang di teliti.  
Untuk keperluan analisis segmentasi pasar, dataset ini menyertakan variabel Papan Pencatatan (Listing Board). Variabel ini bersifat kategorikal yang mengklasifikasikan emiten ke dalam kelompok papan "Utama", "Pengembangan", atau "Akselerasi" sesuai dengan skala bisnis mereka.  
Sementara itu, untuk analisis kuantitatif, terdapat dua metrik finansial utama:

- Jumlah Saham (Shares): total lembar saham yang beredar (shares outstanding) milik emiten, yang angkanya bervariasi mulai ratusan juta hingga miliaran lembar.  

- Harga Terakhir (Last Price): harga penutupan pasar per-lembar saham dalam bentuk Rupiah, yang menjadi indikator valuasi terkini emiten.
    """
)
