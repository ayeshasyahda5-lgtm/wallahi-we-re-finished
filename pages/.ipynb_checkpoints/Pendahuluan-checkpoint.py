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
   Data yang digunakan dalam penelitian ini adalah data saham dari perusahaan-perusahaan di Indonesia, yang dikumpulkan pada tanggal 22 Desember 2025.
Dataset ini mencakup kurang lebih sekitar 300 perusahaan sebagai sampel, sehingga bisa memberikan gambaran yang cukup komplit mengenai kondisi harga saham pada periode tersebut.

Setiap baris dalam data merepresentasikan satu perusahaan, dengan beberapa variabel yang menunjukkan pergerakan harga saham dalam satu hari perdagangan.
Variabel-variabel yang digunakan dalam penelitian ini meliputi:
- Kode Perusahaan

Kode perusahaan adalah identitas unik yang digunakan untuk membedakan satu perusahaan dengan perusahaan lain di pasar saham.
Variabel ini berfungsi sebagai penanda utama dalam pengolahan dan penyajian data.
- Nama Perusahaan

Variabel ini menunjukkan nama resmi dari perusahaan yang sahamnya diperdagangkan.
Informasi ini membantu memudahkan pemahaman hasil analisis serta memberikan konteks terhadap data yang ditampilkan.
- Open Price (Harga Pembukaan)

Harga pembukaan adalah harga saham pada awal sesi perdagangan.
Nilai ini mencerminkan kondisi pasar awal dan ekspektasi para pelaku pasar terhadap perusahaan pada hari tersebut.
- High Price (Harga Tertinggi)

Harga tertinggi menunjukkan nilai tertinggi yang dicapai saham selama sesi perdagangan.
Variabel ini menggambarkan tingkat permintaan tertinggi terhadap saham perusahaan dalam satu hari.
- Low Price (Harga Terendah)

Harga terendah adalah nilai terendah yang terjadi selama sesi perdagangan. Rephrase
Variabel ini mungkin mencerminkan tekanan jual atau ketidakpastian pasar terhadap saham perusahaan.
- Close Price (Harga Penutupan)

Harga penutupan adalah harga saham pada akhir sesi perdagangan.
Nilai ini sering digunakan sebagai gambaran posisi terakhir pasar karena merupakan hasil dari interaksi antara permintaan dan penawaran sepanjang hari.
    """
)
