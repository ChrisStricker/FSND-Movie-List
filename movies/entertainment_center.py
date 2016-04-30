import media
import fresh_tomatoes

#Build a list Movie objects 
sw_empire = media.Movie("The Empire Strikes Back",
                        "It's the second movie released, but the fifth in the series",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=4_46P3Dzvvw")

big_trouble = media.Movie("Big Trouble in Little China",
                        "Jack Burton must battle battle an ancient evil",
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg",
                        "https://www.youtube.com/watch?v=1P0A8pS1JF8")

ironman = media.Movie("Iron Man",
                        "After escaping enemy territory, Tony Stark wants to save the world",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=tbMG2yTDXSY")

conan = media.Movie("Conan the Barbarian",
                        "A boy sold into slavery becomes a man seeking revenge against the warlord who killed his family",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/Conan_the_Barbarian_by_Renato_Casaro.jpg",
                        "https://www.youtube.com/watch?v=z5wwd1VkPd4")

monsters_inc = media.Movie("Monsters, Inc.",
                        "When a human girl wanders into the monster world, two friends must get her back home",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                        "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

kung_fu_panda = media.Movie("Kung Fu Panda",
                        "An enthusiastic panda is chosen to fulfill an ancient prophecy",
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                        "https://www.youtube.com/watch?v=ODRUUJ81D3I")

movies = [sw_empire, big_trouble, ironman, conan, monsters_inc, kung_fu_panda]

# The function open_movies_page will take the list of movies, create an html file, and display it in a browser.
fresh_tomatoes.open_movies_page(movies)
