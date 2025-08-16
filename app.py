import pandas as pd 
import streamlit as st
import plotly as pl
import plotly.express as px

#Limpieza dataframe
def clean_csv(df):
    """ Limpieza extraida del analisis EDA"""
    df.fillna(0,inplace=True)
    df_clean = df.drop_duplicates()
    return df_clean 

df = pd.read_csv("vehicles_us.csv")

df_final = clean_csv(df)
st.title("probando_aplicacion")

df = pd.read_csv("vehicles_us.csv")
# Creando Aplicacion:
st.header("Clase 3 del Sprint 7 - Prueba de Streamlit") 
st.dataframe(df)



car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show()

# Visualizacion distribucion del precio de los vehiculos
fig = px.histogram(car_data, x='price', title='Distribución de precios de vehículos')
fig.show()

# Filtrado para mejor visualizacion
filtered_data = car_data[car_data['price'] < 50000]
fig = px.histogram(filtered_data, x='price', title='Precios < $50,000')
fig.show()


# Título de la app
st.title("Explorador de Datos de Vehículos")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar texto informativo
st.write("Haz clic en el botón para construir un histograma de los precios de los vehículos.")

# Botón para generar el histograma
if st.button("Mostrar histograma", key="btn_histograma"):
    st.write("Aquí va el histograma")
    # Crear histograma con Plotly
    fig = px.histogram(car_data, x='price', title='Distribución de precios de vehículos')
    
    # Mostrar el gráfico en la app
    st.plotly_chart(fig)

    # Título de la aplicación
st.title("Explorador de Datos de Vehículos")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar texto informativo
st.write("Explora los datos de vehículos de segunda mano en EE. UU.")

# Botón para mostrar histograma
if st.button("Mostrar histograma"):
    st.write("Histograma de los precios de vehículos")
    fig_hist = px.histogram(car_data, x='price', title='Distribución de precios de vehículos')
    st.plotly_chart(fig_hist)

    # Botón para mostrar gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    st.write("Gráfico de dispersión: Precio vs Kilometraje")
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Precio vs Kilometraje',
                             labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)'},
                             hover_data=['model_year', 'condition'])
    st.plotly_chart(fig_scatter)