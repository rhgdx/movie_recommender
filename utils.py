"""
Here live other stuff, e.g., unpickled 
"""
import pandas as pd
from fuzzywuzzy import fuzz


Movies = [
    "Tarzan",
    "300",
    "Dumbo",
    "12 Angry Men",
    "Kung Fu Panda",
]


def recommend_movies(user_ratings, num_recommendations=5):
    rating_matrix = pd.read_csv(
        "./rating_matrix.csv",
    )
    active_user_ratings = pd.Series(0, index=rating_matrix.columns)
    for movie, rating in user_ratings.items():

        def get_similarity(x):
            similarity = fuzz.ratio(x, movie)
            return similarity

        matched_movie = max(rating_matrix.columns, key=get_similarity)
        active_user_ratings[matched_movie] = rating
    similarity_scores = rating_matrix.dot(active_user_ratings)
    similarity_scores = similarity_scores.sort_values(ascending=False)
    unseen_movies = rating_matrix.columns[
        rating_matrix.loc[similarity_scores.index[0]] == 0
    ].tolist()
    most_similar_users = similarity_scores[1:6].index
    similar_users_ratings = rating_matrix.loc[most_similar_users, unseen_movies]
    average_ratings = similar_users_ratings.mean()
    recommended_movies = average_ratings.sort_values(ascending=False)
    recommended_movie_ids = recommended_movies.index[:num_recommendations]
    return recommended_movie_ids
