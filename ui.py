import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"  
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_url
        else:
            return "Poster not available"
    except requests.exceptions.RequestException:
        return "Poster not available"



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names ,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('/Users/jadoo/Documents/project_2025/all_movies/movies.pkl','rb'))
similarity = pickle.load(open('/Users/jadoo/Documents/project_2025/matrix/similarity_matrix.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        if recommended_movie_posters[0] != "Poster not available":
            st.image(recommended_movie_posters[0])
        else:
            st.warning("Poster not available.")
    with col2:
        st.text(recommended_movie_names[1])
        if recommended_movie_posters[1] != "Poster not available":
            st.image(recommended_movie_posters[1])
        else:
            st.warning("Poster not available.")

    with col3:
        st.text(recommended_movie_names[2])
        if recommended_movie_posters[2] != "Poster not available":
            st.image(recommended_movie_posters[2])
        else:
            st.warning("Poster not available.")
    with col4:
        st.text(recommended_movie_names[3])
        if recommended_movie_posters[3] != "Poster not available":
            st.image(recommended_movie_posters[3])
        else:
            st.warning("Poster not available.")
    with col5:
        st.text(recommended_movie_names[4])
        if recommended_movie_posters[4] != "Poster not available":
            st.image(recommended_movie_posters[4])
        else:
            st.warning("Poster not available.")









