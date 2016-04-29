import media
import fresh_tomatoes

sw_empire = media.Movie("Star Wars: The Empire Strikes Back",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

big_trouble = media.Movie("Big Trouble in Little China",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

ironman = media.Movie("Iron Man",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

conan = media.Movie("Conan the Barbarian",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/Conan_the_Barbarian_by_Renato_Casaro.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

monsters_inc = media.Movie("Monsters, Inc.",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

kung_fu_panda = media.Movie("Kung Fu Panda",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

movies = [sw_empire, big_trouble, ironman, conan, monsters_inc, kung_fu_panda]
fresh_tomatoes.open_movies_page(movies)
