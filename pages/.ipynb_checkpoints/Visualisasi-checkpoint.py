import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

df_Saham = pd.read_csv("DaftarSahamm.csv", sep=';', on_bad_lines='skip')

st.write("## Preview data: ")
st.dataframe(df_Saham.head())
st.dataframe(df_Saham.tail())

st.write("## Data Chart Last Price: ")
fig=px.histogram(
    df_Saham,
    x='LastPrice',
)
st.plotly_chart(fig)

st.markdown(
    """
  Jadi distribusi LastPrice terlihat jelas lebih dominan miring ke kiri yang artinya kebanyakan perusahaan justru punya harga saham yang cukup tinggi, sementara yang harganya rendah hanya sedikit. Batangnya lebih menumpuk di sisi kanan grafik, lalu makin tipis ke arah kiri. Secara sederhana, grafik ini menunjukkan bahwa di kumpulan data ini, perusahaan berharga saham tinggi jauh lebih banyak dibandingkan yang murah.
    """
)

st.write("## Data Bar Last Price: ")
fig = px.bar(df_Saham,
             x="Name",
             y="LastPrice",
             title="Distribusi Jumlah Shares per Perusahaan",
             color="LastPrice")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
  Jadi berdasarkan itu
    """
)

st.write("## Data Chart Listing Board: ")
fig = px.pie(df_Saham,
             names="ListingBoard",
             title="Proporsi Saham per ListingBoard")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
  Jadi berdasarkan ini
    """
)