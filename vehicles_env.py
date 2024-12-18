import pandas as pd
import streamlit as st
import plotly.express as px
import nbformat

car_data = pd.read_csv(r'C:\Users\admin\Documents\Docs JJER\Sprint 7 Final\vehicles_us.csv')

print(car_data)