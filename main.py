import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    movie = get_random_movie()

    contentb = "<h1>Tommorrow's Movie!</h1>"
    contentb += "<ul>"
    contentb += "<li>" + movie + "</li>"
    contentb += "</ul>"

    return content + contentb

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ["Finding Nemo", "Mad Max", "Super Man", "Willy Wanka and the Chocolate Factory", "Shart attack"]
    list_end = len(movie_list)-1
    # TODO: randomly choose one of the movies, and return it
    moive_pick = random.randint(0,list_end)
    return movie_list[moive_pick]


app.run()
