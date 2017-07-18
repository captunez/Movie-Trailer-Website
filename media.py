class Movie():
    """
    This class stores movie data such as movie title, movie poster image
    and movie poster image
    """
    # Constructor for Class Movie
    def __init__(self, title, poster_image_url, trailer_youtube_url):

        self.title = title   # movie title
        self.poster_image_url = poster_image_url    # movie poster image URL
        # movie trailer Youtube URL
        self.trailer_youtube_url = trailer_youtube_url