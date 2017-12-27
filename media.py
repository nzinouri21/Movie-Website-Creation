import webbrowser
#Things we want the class movie to remember:
#   1.Title
#   2.Storyline
#   3.Poster image
#   4.YouTube trailer

#Based on "Google Python Style Guide", when defining a class name,
#the first letter should be upper-case
class Movie():
    """ This class provides a way to store movie related information. """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
