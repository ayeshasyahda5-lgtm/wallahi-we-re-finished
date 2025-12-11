import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Visualisasi Data Ekonomi", layout="wide")

st.title("📊 Visualisasi Interaktif Data Ekonomi Indonesia")

# --- Load Data ---
uploaded_file = st.file_uploader("Upload file data_ekonomi.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";")

    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    # --- Filter Tahun ---
    st.subheader("🔎 Filter Tahun")
    years = sorted(df["Tahun"].unique())
    selected_years = st.multiselect("Pilih Tahun:", years, default=years)

    filtered_df = df[df["Tahun"].isin(selected_years)]

    # --- Line Chart ---
    st.subheader("📈 Line Chart (PDB / Inflasi / IHSG)")
    y_option = st.selectbox("Pilih variabel Y:", ["PDB", "Inflasi", "IHSG"])

    line_chart = (
        alt.Chart(filtered_df)
        .mark_line(point=True)
        .encode(
            x="Tahun:O",
            y=f"{y_option}:Q",
            tooltip=["Tahun", y_option]
        )
        .interactive()
    )
    st.altair_chart(line_chart, use_container_width=True)

    # --- Scatter Plot ---
    st.subheader("📉 Scatter Plot Interaktif")
    x_scatter = st.selectbox("X Axis:", ["PDB", "Inflasi", "IHSG"], index=0)
    y_scatter = st.selectbox("Y Axis:", ["PDB", "Inflasi", "IHSG"], index=1)

    scatter_plot = (
        alt.Chart(filtered_df)
        .mark_circle(size=80)
        .encode(
            x=f"{x_scatter}:Q",
            y=f"{y_scatter}:Q",
            color="Tahun:O",
            tooltip=["Tahun", x_scatter, y_scatter]
        )
        .interactive()
    )
    st.altair_chart(scatter_plot, use_container_width=True)

else:
    st.info("Silakan upload file **data_ekonomi.csv** terlebih dahulu.")