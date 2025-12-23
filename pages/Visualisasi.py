import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import yfinance as yf
from IPython.display import display

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
  Dari hasil grafik bar untuk variabel LastPrice di atas terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang tergolong tinggi, sementara itu saham dengan harga rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah(rendah).
    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Tampilan data keseluruhan ")


df_Saham['Kode Saham'] = df_Saham['Kode Saham'].astype(str).str.strip()

kolom_harga = ['Open Price', 'Tertinggi', 'Terendah', 'Penutupan']
df_Saham[kolom_harga] = df_Saham[kolom_harga].apply(pd.to_numeric, errors='coerce')

ticker_symbol = st.selectbox(
    "Pilih Kode Saham",
    sorted(df_Saham['Kode Saham'].astype(str).str.strip().unique())
)

df_ticker = df_Saham[df_Saham['Kode Saham'] == ticker_symbol].copy()
df_ticker = df_ticker.reset_index(drop=True)
df_ticker['Observasi'] = df_ticker.index + 1

if st.checkbox("Tampilkan Grafik"):

    pilihan_atribut = st.multiselect(
        "Pilih atribut harga:",
        kolom_harga
    )

    if pilihan_atribut:

        df_melt = df_ticker.melt(
            id_vars='Observasi',
            value_vars=pilihan_atribut,
            var_name='Variabel',
            value_name='Harga'
        )

        fig = px.line(
            df_melt,
            x='Observasi',
            y='Harga',
            color='Variabel',
            title=f"Harga Saham {ticker_symbol}"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Pilih minimal satu atribut harga.")