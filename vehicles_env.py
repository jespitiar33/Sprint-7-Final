import pandas as pd
import streamlit as st
import plotly.express as px
import nbformat

car_data = pd.read_csv('vehicles_us.csv')

print(car_data)