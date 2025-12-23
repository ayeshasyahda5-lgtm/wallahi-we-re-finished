import streamlit as st

st.title("Analisis Data")
st.write("### hasil Analisis Dataset Saham: ")

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.markdown(
    """
   Berdasarkan analisis visual harga pembukaan, penutupan, tertinggi, dan terendah, dapat dipahami bahwa pola harga saham di antara perusahaan menunjukkan adanya ketimpangan yang cukup signifikan. Grafik tersebut mengilustrasikan bahwa hanya sejumlah kecil perusahaan memiliki harga saham yang sangat tinggi, sedangkan sebagian besar perusahaan beroperasi dalam kisaran harga yang lebih rendah. Pola ini menunjukkan bahwa nilai pasar dan aktivitas tidak tersebar merata di antara perusahaan-perusahaan yang diperiksa.

Kehadiran beberapa perusahaan dengan harga saham yang tinggi menunjukkan konsentrasi nilai ekonomi pada aspek tertentu. Perusahaan dengan harga saham yang tinggi biasanya memiliki ukuran yang lebih besar, tingkat kepercayaan dari pasar yang lebih tinggi, serta tingkat perdagangan yang lebih aktif dibandingkan dengan yang lain. Sebaliknya, perusahaan dengan harga saham rendah mencerminkan skala bisnis yang lebih kecil atau kurangnya ketertarikan dari pasar.

Kesamaan dalam pola antara grafik harga pembukaan dan penutupan menunjukkan bahwa dalam satu hari perdagangan, pasar tampak bergerak dalam suasana yang cukup stabil. Ini menandakan bahwa tidak ada guncangan besar yang secara drastis mempengaruhi pandangan pasar tentang perusahaan-perusahaan tersebut dalam jangka waktu pendek. Dengan kata lain, harapan awal pasar tetap relatif sama hingga akhir sesi perdagangan.

Perbedaan yang lebih mencolok terlihat pada grafik harga tertinggi dan terendah. Jarak antara harga tertinggi dan terendah mencerminkan tingkat variasi harga yang dialami oleh setiap perusahaan. Perusahaan yang menunjukkan perbedaan besar antara harga tertinggi dan terendah menunjukkan adanya dinamika perdagangan yang lebih hidup, di mana terjadi pergeseran antara permintaan dan penawaran. Sementara perusahaan dengan selisih harga yang kecil mencerminkan situasi perdagangan yang lebih stabil dan tenang.

Secara keseluruhan, variasi harga yang tampak pada keempat grafik mencerminkan perbedaan karakteristik perusahaan dalam merespons aktivitas pasar. Perbedaan ini tidak hanya menunjukkan variasi nilai saham, tetapi juga menggambarkan perbedaan intensitas aktivitas ekonomi, tingkat kepercayaan pasar, dan stabilitas perdagangan antar perusahaan.
    """
)
