import media
import fresh_tomatoes

# Boss Baby movie: movie title, poster image and movie trailer
boss_baby = media.Movie(
    "The Boss Baby",
    "https://i.ytimg.com/vi/RBfCQuQqgNs/movieposter.jpg",
    "https://www.youtube.com/watch?v=RBfCQuQqgNs&list=PLHPTxTxtC0ibCJB1vtN_-cwL5X-yPiPyO&feature=c4-overview-vl")  # noqa

# Going in Style movie: movie title, poster image and movie trailer
going_in_style = media.Movie(
    "Going in Style",
    "https://i.ytimg.com/vi/N8ATvx7LT0c/movieposter.jpg",
    "https://www.youtube.com/watch?v=RBfCQuQqgNs&list=PLHPTxTxtC0ibCJB1vtN_-cwL5X-yPiPyO&feature=c4-overview-vl")  # noqa

# Ghost in the Shell movie: movie title, poster image and movie trailer
ghost_in_shell = media.Movie(
    "Ghost in the Shell",
    "https://i.ytimg.com/vi/0nbIdLz2Azo/movieposter.jpg",
    "https://www.youtube.com/watch?v=N8ATvx7LT0c&list=PLHPTxTxtC0ibCJB1vtN_-cwL5X-yPiPyO&feature=c4-overview-vl")  # noqa

# Gifted movie: movie title, poster image and movie trailer
gifted = media.Movie(
    "Gifted",
    "https://i.ytimg.com/vi/j3phtzCWAgg/movieposter.jpg",
    "https://www.youtube.com/watch?v=j3phtzCWAgg&list=PLHPTxTxtC0ibCJB1vtN_-cwL5X-yPiPyO&feature=c4-overview-vl")  # noqa

movies = [boss_baby, going_in_style, ghost_in_shell, gifted]
fresh_tomatoes.open_movies_page(movies)

