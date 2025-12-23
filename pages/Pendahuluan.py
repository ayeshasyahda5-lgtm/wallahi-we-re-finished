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
    Pasar modal memainkan peran penting dalam perekonomian karena menjadi tempat bertemunya pihak yang membutuhkan dana dengan pihak yang memiliki dana berlebih.
Selain itu, perubahan harga saham juga bisa menggambarkan kondisi serta performa perusahaan, serta menunjukkan bagaimana pasar bereaksi terhadap informasi ekonomi yang terus berkembang. Karena itu, data saham dapat digunakan sebagai salah satu sarana untuk memahami dinamika kegiatan ekonomi secara keseluruhan.

Penelitian ini dibuat sebagai bagian dari tugas praktikum Big Data dengan pendekatan deskriptif dan visualisasi data, menggunakan data saham dari perusahaan yang terdaftar di Indonesia.
Dalam penelitian ini, data saham tidak digunakan untuk tujuan pengambilan keputusan investasi, melainkan sebagai bahan analisis untuk mengamati pola serta variasi harga saham di antara perusahaan-perusahaan tersebut. Pendekatan ini bertujuan untuk memahami karakteristik data serta makna informasi yang terkandung di dalamnya.

Tujuan utama dari penelitian ini adalah untuk memberikan gambaran mengenai perbedaan harga saham antar perusahaan di Indonesia, memahami arti dari berbagai indikator harga saham seperti harga pembukaan, penutupan, tertinggi, dan terendah, serta menyajikan data dalam bentuk visual agar lebih mudah dipahami.
Selain itu, penelitian ini juga bertujuan untuk melatih kemampuan dalam mengolah serta menyajikan data dalam jumlah besar secara terstruktur dan informatif.

Fungsi utama dari penelitian ini adalah sebagai sarana eksplorasi data untuk melihat pola umum pergerakan harga saham antar perusahaan.
Hasil visualisasi diharapkan dapat membantu memberikan pemahaman awal mengenai kondisi pasar, perbedaan karakteristik perusahaan, serta variasi aktivitas perdagangan yang terjadi.

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
