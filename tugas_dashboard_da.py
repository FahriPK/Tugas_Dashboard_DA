import pandas as pd
import plotly.express as px
import streamlit as st

# Data preprocessing
data = pd.read_excel("datasets.xlsx", sheet_name="Worksheet")

# Filter hanya data "Diperiksa" dan "Melanggar"
filtered_data = data[data['status_pemeriksaan'].isin(['Diperiksa', 'Melanggar'])]

# Streamlit UI
st.title("Dashboard Pemeriksaan Kendaraan BPTD")
st.write("Visualisasi jumlah kendaraan diperiksa dan melanggar berdasarkan wilayah BPTD.")

# Widgets
selected_year = st.selectbox(
    "Pilih Tahun",
    options=filtered_data['tahun'].unique(),
    index=0
)

threshold_value = st.slider(
    "Filter Jumlah Kendaraan (≥)",
    min_value=int(filtered_data['jumlah'].min()),
    max_value=int(filtered_data['jumlah'].max()),
    value=int(filtered_data['jumlah'].min()),
    step=100
)

# Filter data berdasarkan input
filtered = filtered_data[
    (filtered_data['tahun'] == selected_year) & 
    (filtered_data['jumlah'] >= threshold_value)
]

# Plot chart
fig = px.bar(
    filtered,
    x='wilayah_bptd',
    y='jumlah',
    color='status_pemeriksaan',
    barmode='group',
    labels={'jumlah': 'Jumlah Kendaraan', 'wilayah_bptd': 'Wilayah BPTD'},
    title=f"Data Pemeriksaan Tahun {selected_year} (Jumlah ≥ {threshold_value})"
)

# Display chart
st.plotly_chart(fig)
