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
  Dari hasil grafik bar untuk variabel Open Price di atas terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang tergolong tinggi, sementara itu saham dengan harga rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah(rendah).
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
  Dari hasil grafik bar untuk variabel Close Price di atas terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang tergolong tinggi, sementara itu saham dengan harga rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah(rendah).
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
  Dari hasil grafik bar untuk variabel High Price di atas terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang tergolong tinggi, sementara itu saham dengan harga rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah(rendah).
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
  Dari hasil grafik bar untuk variabel Low Price di atas terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang tergolong tinggi, sementara itu saham dengan harga rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah(rendah).
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