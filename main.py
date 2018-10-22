import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    moviea = get_random_movie()
    movieb = get_random_movie()
    
    tommorrow_movie = check_if_same(moviea, movieb)
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + moviea + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
  

    contentb = "<h1>Tommorrow's Movie!</h1>"
    contentb += "<ul>"
    contentb += "<li>" + tommorrow_movie + "</li>"
    contentb += "</ul>"

    return content + contentb

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ["Finding Nemo", "Mad Max", "Super Man", "Willy Wanka and the Chocolate Factory", "Shart attack"]
   
    # TODO: randomly choose one of the movies, and return it
    moive_pick = random.choice(movie_list)
    return moive_pick

def check_if_same(moviea, movieb):
    #insures that tommorrows movie is not the same as Today's movie
    if moviea == movieb:
        while moviea == movieb:
            movieb = get_random_movie()
        
        return movieb

    else:
        return movieb


app.run()
