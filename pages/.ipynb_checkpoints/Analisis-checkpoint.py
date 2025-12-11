import streamlit as st

st.title("Analisis Data")
st.write("### Berikut adalah hasil Analisis data kami: ")

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.markdown(
    """
   Berdasarkan box plot yang menampilkan variabel **PDB**, **Inflasi**, dan **IHSG**, terlihat bahwa masing-masing indikator memiliki tingkat variasi yang berbeda.

Pertama, **PDB menunjukkan persebaran nilai yang paling luas**, terlihat dari ukuran box yang besar dan whisker yang panjang. Ini mengindikasikan bahwa PDB mengalami fluktuasi yang lebih tinggi dibandingkan variabel lainnya. Adanya beberapa *outlier* pada nilai yang lebih tinggi juga menunjukkan bahwa terdapat periode tertentu ketika pertumbuhan ekonomi melonjak melampaui kondisi normal. Meskipun demikian, sebagian besar nilai PDB tetap berkumpul dalam satu rentang yang jelas, menandakan adanya kecenderungan stabil setelah fluktuasi.

Kedua, **Inflasi menunjukkan persebaran yang sangat sempit**. Box plot yang sangat kecil menandakan bahwa inflasi bergerak dalam rentang yang sangat stabil pada periode analisis. Meski terdapat sedikit *outlier*, secara keseluruhan inflasi tidak mengalami pergerakan yang signifikan, sehingga dapat dikatakan bahwa kondisi harga berada dalam keadaan terkontrol.

Ketiga, **IHSG memperlihatkan variasi menengah**, lebih tinggi dari inflasi namun lebih rendah dari PDB. Rentang interkuartilnya cukup jelas, menunjukkan stabilitas nilai pasar saham secara umum. Kehadiran *outlier* di atas nilai median menunjukkan bahwa ada beberapa periode ketika pasar saham mengalami kenaikan tajam, kemungkinan dipengaruhi oleh sentimen positif atau faktor eksternal tertentu.

Secara keseluruhan, analisis box plot ini memperlihatkan bahwa ketiga indikator tidak menunjukkan pola ekstrem yang dapat mengganggu stabilitas ekonomi, meskipun masing-masing memiliki tingkat dinamika yang berbeda.
    """
)