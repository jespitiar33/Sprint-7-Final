import pandas as pd
import streamlit as st
import plotly.express as px
import nbformat

car_data = pd.read_csv(r'C:\Users\admin\Documents\Docs JJER\Sprint 7 Final\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # escribir un mensaje
    t.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    fig = px.scatter(df, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
