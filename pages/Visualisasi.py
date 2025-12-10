import pandas as pd
import numpy as np

# Membuat dataset ekonomi bersih
np.random.seed(42)
rows = 300

data = pd.DataFrame({
    "Tahun": np.random.choice(range(2010, 2025), rows),
    "PDB": np.random.normal(12000, 800, rows).round(2),        # Produk Domestik Bruto
    "Inflasi": np.random.normal(3.5, 0.8, rows).round(2),      # Inflasi %
    "IHSG": np.random.normal(6500, 300, rows).round(2)         # Indeks Harga Saham Gabungan
})

data.to_csv("data_ekonomi.csv", index=False)

data.head()

import streamlit as st
import pandas as pd
import altair as alt

st.title("Visualisasi Data Ekonomi Indonesia")


# app_box_scatter.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data_ekonomi.csv")

st.title("Visualisasi Data Ekonomi — Scatter & Box Plot")

st.subheader("Preview Data")
st.dataframe(df)


# Box plot: Distribusi Inflasi, PDB, IHSG
st.subheader("Box Plot — Distribusi Variabel Numerik")
fig2, ax2 = plt.subplots(figsize=(6,4))
sns.boxplot(data=df[["PDB","Inflasi","IHSG"]], ax=ax2)
ax2.set_title("Box Plot PDB / Inflasi / IHSG")
ax2.set_xticklabels(["PDB","Inflasi","IHSG"])
st.pyplot(fig2)

