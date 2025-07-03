import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv('Movies.csv')
all_genres = ['All'] + sorted(movies_data['genre'].unique())

st.sidebar.title('Menu')
option = st.sidebar.selectbox('Choose Option:', all_genres)

if option == 'All':
    current_df = movies_data.sort_values('genre')
else:
    current_df = movies_data[movies_data['genre'] == option]


st.dataframe(current_df, hide_index=True)
