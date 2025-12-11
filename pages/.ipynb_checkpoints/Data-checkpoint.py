import streamlit as st
import pandas as pd
import plotly.express as px

# --- Title ---
st.title("Visualisasi Data Ekonomi Interaktif")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("data_ekonomi.csv")

df = load_data()

st.subheader("Preview Data")
st.write(df.head())

# --- Sidebar Filter ---
st.sidebar.header("Filter Visualisasi")

numerical_columns = df.select_dtypes(include="number").columns.tolist()

selected_x = st.sidebar.selectbox("Pilih kolom X", numerical_columns)
selected_y = st.sidebar.selectbox("Pilih kolom Y", numerical_columns)

chart_type = st.sidebar.radio(
    "Jenis Grafik",
    ["Scatter Plot", "Line Chart", "Bar Chart"]
)

# --- Plot ---
st.subheader("Grafik Interaktif")

if chart_type == "Scatter Plot":
    fig = px.scatter(df, x=selected_x, y=selected_y, title=f"{selected_x} vs {selected_y}")

elif chart_type == "Line Chart":
    fig = px.line(df, x=selected_x, y=selected_y, title=f"{selected_x} vs {selected_y}")

elif chart_type == "Bar Chart":
    fig = px.bar(df, x=selected_x, y=selected_y, title=f"{selected_x} vs {selected_y}")

st.plotly_chart(fig, use_container_width=True)

# --- Extra: Statistik ---
st.subheader("Statistik Deskriptif")
st.write(df.describe())