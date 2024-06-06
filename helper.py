import requests
import pickle

import pandas as pd
df = pd.read_csv('Data/movies.csv')
similarity_indexed = pickle.load(open('similarity.pkl', 'rb'))


API_KEY = 'aed0f7f5a89450f11167d5e0254cff70' 
BASE_URL = 'https://api.themoviedb.org/3'
IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

# Function to fetch data
def fetch_movie_details(movie_id):
    movie_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"

    movie_response = requests.get(movie_url)

    if movie_response.status_code == 200:
        movie_data = movie_response.json()

        title = movie_data.get('title', 'N/A')
        poster_path = movie_data.get('poster_path', 'N/A')
        poster_url = f"{IMAGE_BASE_URL}{poster_path}" if poster_path else 'N/A'
    
        return {
            'id': movie_id,
            'title': title,
            'poster' : poster_url
        }
    else:
        return None
    

# Functions to convert df index to id and vice versa
def id_to_index(id):
    return df[df['id'] == id].index[0]

def index_to_id(index):
    return df['id'][index]


# Function to recommand movies from id
def recommand(id, start_rank = 0, end_rank = 12):
    movies = []

    # Find index of given id
    try:
        index = id_to_index(id)
    except:
        return 'Invalid id'
    movies_rec = similarity_indexed[index][start_rank:end_rank]
    for m in movies_rec:
        movies.append(index_to_id(m))
    return movies


# Function that recommand movie by name, and returns name, poster and id of recommanded movie
def recommand_by_name(movie, start_rank = 0, end_rank = 13):
    id = df[df['title'] == movie]['id'].iloc[0]
    recommanded_ids = recommand(id, start_rank, end_rank)

    res = []
    for i in recommanded_ids:
        res.append(fetch_movie_details(i))
    
    return res