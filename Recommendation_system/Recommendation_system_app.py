import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load the precomputed data
with open('movie_list.pkl', 'rb') as file:
    movies = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# Streamlit app
st.title('Movie Recommendation System')
st.write('Enter a movie title to get recommendations:')

# Get user input
movie_title = st.text_input('Movie Title')

def recommend(movie):
    # Check if the movie exists in the dataset
    if movie in movies['title'].values:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
        return recommended_movies
    else:
        return ['Movie not found in the dataset.']

if st.button('Get Recommendations'):
    recommendations = recommend(movie_title)
    st.write('**Recommended Movies:**')
    for rec in recommendations:
        st.write(f'- {rec}')


#streamlit run Recommendation_system_app.py