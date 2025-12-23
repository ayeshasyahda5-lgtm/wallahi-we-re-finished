import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import yfinance as yf


df_Saham = pd.read_csv("Ringkasan Saham-20251222.csv", sep=';', on_bad_lines='skip')

st.write("## Preview data: ")
st.dataframe(df_Saham.head())
st.dataframe(df_Saham.tail())

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data Open Price ")
fig=px.histogram(
    df_Saham,
    x='Nama Perusahaan',
    y='Open Price',
)
st.plotly_chart(fig)

st.markdown(
    """
    Dari hasil grafik bar yang menampilkan data harga pembukaan memperlihatkan perbedaan yang cukup mencolok pada nilai pembukaan antar berbagai perseroan. Sebagian besar perusahaan memperlihatkan harga pembukaan yang lumayan kecil, namun ada segelintir perusahaan yang terlihat memiliki harga pembukaan sangat tinggi. Kecenderungan ini menandakan bahwa situasi awal dalam transaksi saham tidak sama untuk setiap perusahaan.

Perbedaan harga pembukaan ini menggambarkan beragam ekspektasi pasar di permulaan tiap hari transaksi. Perseroan dengan harga pembukaan tinggi umumnya merupakan entitas usaha yang lebih besar atau lebih dipercaya pasar, sedangkan yang harganya rendah cenderung menunjukkan kegiatan jual beli yang kurang intensif atau nilai sahamnya lebih kecil.
    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data Close Price ")
fig=px.histogram(
    df_Saham,
    x='Nama Perusahaan',
    y='Penutupan',
)
st.plotly_chart(fig)

st.markdown(
    """
  Dari hasil grafik bar harga penutupan memperlihatkan corak yang mirip dengan harga pembukaan, yaitu kebanyakan perseroan berkumpul pada angka harga yang rendah dan cuma segelintir yang memiliki harga penutupan tinggi. Hal ini menandakan bahwa di penghujung suatu transaksi, sebaran harga saham antar perusahaan masih didominasi oleh perseroan dengan harga yang kecil.

Kesamaan pola antara harga pembukaan dan penutupan mengisyaratkan bahwa pergerakan harga selama satu hari transaksi tidak begitu drastis. Harga penutupan merefleksikan hasil akhir dari pertemuan antara minat beli dan jual sepanjang hari itu, sehingga bagan ini memberikan gambaran mengenai kedudukan akhir pasar bagi setiap perusahaan.
    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data High Price ")
fig=px.histogram(
    df_Saham,
    x='Nama Perusahaan',
    y='Tertinggi',
)
st.plotly_chart(fig)

st.markdown(
    """
  Dari hasil grafik bar yang menampilkan harga paling tinggi menampakkan peningkatan nilai yang cukup besar pada beberapa perusahaan dibandingkan sisanya. Ada beberapa batang dalam bagan ini yang terlihat jauh menjulang, menandakan bahwa saham dari perusahaan tersebut melonjak harganya secara mencolok selama sesi transaksi berlangsung.

Perubahan pada harga puncak ini merefleksikan beda minat pasar terhadap saham-saham tertentu. Perusahaan dengan nilai puncak yang tinggi menandakan bahwa sahamnya sangat diminati, meski tidak semua perusahaan mampu menjaga harga itu sampai pasar tutup.
    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data Low Price ")
fig=px.histogram(
    df_Saham,
    x='Nama Perusahaan',
    y='Terendah',
)
st.plotly_chart(fig)

st.markdown(
    """
  Dari hasil grafik bar harga paling rendah menunjukkan batas minimal harga saham yang tercatat selama proses jual beli. Pola yang terlihat pada bagan ini memperlihatkan bahwa kebanyakan perusahaan punya harga dasar yang lumayan rendah dan nilainya berdekatan, sedangkan hanya segelintir perusahaan yang memperlihatkan nilai harga dasar yang lebih tinggi.

Hal ini mengartikan bahwa tekanan jual atau penurunan harga lebih terasa pada perusahaan dengan nilai saham yang kecil. Sebaliknya, perusahaan yang harga dasarnya tetap tinggi cenderung memperlihatkan stabilitas harga yang lebih oke selama transaksi berlangsung.
    """
)


st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Tampilan data keseluruhan ")


df_Saham['Kode Saham'] = df_Saham['Kode Saham'].astype(str).str.strip()

kolom_harga = ['Open Price', 'Tertinggi', 'Terendah', 'Penutupan']
df_Saham[kolom_harga] = df_Saham[kolom_harga].apply(pd.to_numeric, errors='coerce')

if st.checkbox("Tampilkan Grafik"):

    pilihan_atribut = st.multiselect(
        "Pilih atribut harga:",
        kolom_harga,
        default=kolom_harga
    )

    if pilihan_atribut:

        df_melt = df_Saham.melt(
            id_vars='Kode Saham',
            value_vars=pilihan_atribut,
            var_name='Variabel',
            value_name='Harga'
        )

        fig = px.line(
            df_melt,
            x='Kode Saham',
            y='Harga',
            color='Variabel',
            markers=True,
            title="Perbandingan Harga Saham Berdasarkan Kode Saham"
        )

        fig.update_layout(
            xaxis_title="Kode Saham",
            yaxis_title="Harga"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Pilih minimal satu atribut harga.")