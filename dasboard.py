import pandas as pd
import streamlit as st

st.title("Dashboard de Ventas")

# Cargar los datos
df = pd.read_csv('ventas.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'])

# ---------------- FILTRO ----------------
regiones = ["Todas"] + sorted(df['Region'].unique().tolist())
region = st.selectbox("Filtrar por región:", regiones)

if region != "Todas":
    df = df[df['Region'] == region]

# ---------------- KPIs ----------------
total_ventas = df['Ventas'].sum()
total_unidades = df['Cantidad'].sum()
ticket_promedio = df['Ventas'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Ventas totales", f"${total_ventas:,.2f}")
col2.metric("Unidades vendidas", int(total_unidades))
col3.metric("Ticket promedio", f"${ticket_promedio:,.2f}")

# ---------------- COMPARACIÓN: ventas por producto ----------------
st.subheader("Comparación de ventas por producto")
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()
st.bar_chart(ventas_por_producto)

# ---------------- TENDENCIA: ventas en el tiempo ----------------
st.subheader("Tendencia de ventas en el tiempo")
ventas_por_fecha = df.groupby('Fecha')['Ventas'].sum()
st.line_chart(ventas_por_fecha)

# ---------------- EVIDENCIA: ventas por vendedor ----------------
st.subheader("Ventas por vendedor")
ventas_por_vendedor = df.groupby('Vendedor')['Ventas'].sum()
st.bar_chart(ventas_por_vendedor)

# ---------------- INSIGHT ----------------
producto_mejor = ventas_por_producto.idxmax()
vendedor_mejor = ventas_por_vendedor.idxmax()

st.subheader("Insight")
st.write(
    f"El producto que más vende es **{producto_mejor}**, "
    f"con ${ventas_por_producto.max():,.2f} en ventas totales."
)
st.write(f"El vendedor con más ventas es **{vendedor_mejor}**.")

# ---------------- RECOMENDACIÓN ----------------
st.subheader("Recomendación")
st.write(
    f"Hay que ingresar más **{producto_mejor}**, es el que más dinero deja. "
    f"Y ya que **{vendedor_mejor}** es el que más vende, no estaría mal preguntarle "
    f"qué está haciendo bien para que los demás le copien."
)
