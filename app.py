import pandas as pd
import streamlit as st
import pickle
import requests
import pandas
def recommend(movies):
    movie_index = movies1[movies1['title'] == movies].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=  []
    for i in movies_list:
        movie_id =i[0]
        #fetch poster from api
        recommended_movies.append(movies1.iloc[i[0]].title)
    return recommended_movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies1=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
st.title("MOVIE RECOMMENDER SYSTEM")


selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies_list)

if st.button('Recommend'):
    recomendations = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)
