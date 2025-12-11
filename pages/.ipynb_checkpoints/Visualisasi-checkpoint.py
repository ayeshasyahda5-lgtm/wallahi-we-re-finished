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
  Jadi berdasarkan yang ini
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

st.write("## Data Chart Last Price: ")
fig = px.pie(df_Saham,
             names="ListingBoard",
             title="Proporsi Saham per Listing Board")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
  Jadi berdasarkan ini
    """
)