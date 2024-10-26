import pickle
import pandas as pd
import streamlit as st
import requests


# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7153e80398c4889b0fdc08931b01e9d9&language=en-US".format(
        movie_id)
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


# Function to recommend movies based on similarity
def recommend(movie):
    # Find the movie index in the DataFrame
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    # Get similarity scores for the selected movie
    distances = similarity[movie_index]

    # Sort movies based on similarity scores (excluding the first movie, which is itself)
    movies_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Prepare lists to store recommended movie names and posters
    recommended_movie_names = []
    recommended_movie_posters = []

    # Fetch the top 5 most similar movies
    for i in movies_list_sorted:
        movie_id = movies_list.iloc[i[0]].movie_id  # Fetch the movie_id from movies_list DataFrame
        recommended_movie_names.append(movies_list.iloc[i[0]].title)  # Append movie title
        recommended_movie_posters.append(fetch_poster(movie_id))  # Append movie poster URL

    return recommended_movie_names, recommended_movie_posters


# Streamlit header and input
st.header('Movie Recommender System')

# Load preprocessed data
movies_list = pickle.load(open('movies.pkl', 'rb'))  # Load movies as DataFrame
similarity = pickle.load(open('similarity1.pkl', 'rb'))  # Load similarity matrix

# Extract movie titles from the DataFrame
movies = movies_list['title'].values

# Movie selection dropdown
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies
)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    # Display recommended movie names and posters in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
