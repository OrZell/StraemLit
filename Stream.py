import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv('Movies.csv')
all_genres = sorted(movies_data['genre'].unique())
all_columns = movies_data.columns

st.sidebar.title('Menu')
option = st.sidebar.selectbox('Choose Option:', ['All'] + all_genres)
st.sidebar.title('Menu')
sortBy = st.sidebar.selectbox('Sort By:', all_columns)


df_by_genre = movies_data.sort_values('genre') if option == 'All' else movies_data[movies_data['genre'] == option]


st.dataframe(df_by_genre.sort_values(sortBy), hide_index=True)
