import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=fa67831dc8a218eadde0a2fe094eba17')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].original_title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

with open('movies.pkl', 'rb') as file:
    movies_pkl_df = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

movies = pd.DataFrame(movies_pkl_df)
movies_list = movies['original_title'].values

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox("What movie have you watched before?", movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    # with col1:
    #     st.markdown(f"##### {names[0]}")
    #     st.image(posters[0])
    #
    # with col2:
    #     st.markdown(f"##### {names[1]}")
    #     st.image(posters[1])
    #
    # with col3:
    #     st.markdown(f"##### {names[2]}")
    #     st.image(posters[2])
    #
    # with col4:
    #     st.markdown(f"##### {names[3]}")
    #     st.image(posters[3])
    #
    # with col5:
    #     st.markdown(f"##### {names[4]}")
    #     st.image(posters[4])

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
