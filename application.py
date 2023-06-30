from flask import Flask, render_template, request
from recommenders import random_recommender
from utils import recommend_movies

# Flask main object that handles the web application and the server
app = Flask(__name__)


@app.route(
    "/", methods=["GET"]
)  # <- routing with decorator: mapping Url to what is been displayed on the screen
def landing_page():
    # return "Welcome to the Decisions recommender"
    return render_template("land_page.html")


@app.route("/", methods=["POST"])
def recommendations_page():
    user_scores = {}
    form_data = request.form
    for i in range(1, 4):
        movie = form_data[f"movie{i}"]
        rating = form_data[f"rating{i}"]
        user_scores[movie] = int(rating)
    user_rec = recommend_movies(user_scores)
    # return "Movies: " + ", ".join(user_rec) + "\n"
    return render_template("recommend.html", movie_list=user_rec)


@app.route("/recommendation")
def results():
    print(request.args)
    return "recommend.html"


if __name__ == "__main__":
    # It starts up the
    # in-built development Flask server
    app.run(
        debug=True,
    )
