import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

df_Saham = pd.read_csv("DaftarSahamm.csv", sep=';', on_bad_lines='skip')

st.write("## Preview data: ")
st.dataframe(df_Saham.head())
st.dataframe(df_Saham.tail())

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

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

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data Bar Last Price: ")
fig = px.bar(df_Saham,
             x="Name",
             y="LastPrice",
             title="Distribusi Jumlah Shares per Perusahaan",
             color="LastPrice")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    Berdasarkan grafik Shares, terlihat bahwa jumlah saham tiap perusahaan memang bervariasi cukup besar. Sebagian besar perusahaan berada pada kisaran jumlah saham yang menengah, sementara hanya sedikit yang memiliki jumlah saham sangat tinggi hingga tampak menonjol sebagai outlier. Perbedaan ini wajar karena tiap perusahaan punya kebutuhan modal dan skala bisnis yang berbeda. Secara sederhana, grafik ini menunjukkan bahwa mayoritas emiten bergerak dengan kapasitas yang relatif stabil, sementara beberapa perusahaan besar menjadi “penarik rentang” data karena ukuran sahamnya yang jauh lebih besar.
    """
)

st.write("────────────────────⋆⋅☆⋅⋆────────────────────⋯⋅๑┈•✦")

st.write("## Data Chart Listing Board: ")
fig = px.pie(df_Saham,
             names="ListingBoard",
             title="Proporsi Saham per ListingBoard")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    Dapat terlihat dari diagram pie di atas ini menunjukkan bahwa sebagian besar perusahaan tercatat di **Papan Pengembangan** dan **Papan Utama**, yang bersama-sama mendominasi hampir seluruh proporsi data. Sementara itu, **Papan Akselerasi** hanya ditempati sedikit perusahaan sehingga porsinya tampak sangat kecil. Gambaran ini wajar karena banyak perusahaan sudah berada pada tahap bisnis yang lebih stabil atau sedang berkembang, sedangkan hanya sebagian kecil yang masih berada pada fase awal. Secara sederhana, grafik ini menunjukan bahwa mayoritas emiten kini “bermain” di level yang lebih matang, sementara beberapa lainnya masih berada di tahap percepatan menuju pertumbuhan yang lebih besar.
    """
)