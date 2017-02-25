import webbrowser

class Movie():
    #pre-defined class variable called __doc__
    """This class provides a way to store movie related information"""
    #class variable for all instances to access. Can share this list.
    #All caps because it's a constant. See google python style guide
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
