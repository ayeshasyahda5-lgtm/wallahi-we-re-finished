import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
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

df_Saham = df.reset_index(drop=True)
df['Observasi'] = df.index + 1
dropdown_kode = widgets.Dropdown(
    options=sorted(df['Kode Perusahaan'].unique()),
    description='Kode Saham:',
    value=sorted(df['Kode Perusahaan'].unique())[0]
)

def plot_multiline_no_date(kode):
    data = df[df['Kode Perusahaan'] == kode]

    nama = data['Nama Perusahaan'].iloc[0]

    plt.figure(figsize=(14,6))

    plt.plot(data['Observasi'], data['Open Price'], label='Open Price')
    plt.plot(data['Observasi'], data['Tertinggi'], label='High')
    plt.plot(data['Observasi'], data['Terendah'], label='Low')
    plt.plot(data['Observasi'], data['Penutupan'], label='Close')

    plt.title(f"Perbandingan Harga Saham {nama} ({kode})")
    plt.xlabel("Urutan Observasi")
    plt.ylabel("Harga Saham")
    plt.legend()
    plt.grid(True)

    plt.show()

interactive_plot = widgets.interactive(
    plot_multiline_no_date,
    kode=dropdown_kode
)

display(interactive_plot)

