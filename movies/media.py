import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ This is the constructor for the movie class """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function opens a browser window and displays the movie's trailer """
        
        webbrowser.open(self.trailer_youtube_url)
