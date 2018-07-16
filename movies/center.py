from movie import Movie
import fresh_tomatoes

toy_story = Movie('Toy Story', 'Toys come to life',
                  'https://en.wikipedia.org/wiki/File:Toy_Story.jpg',
                  'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = Movie('Avatar', 'A marine on an alien planet',
               'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
               'https://www.youtube.com/watch?v=uZNHIU3uHT4')

school_of_rock = Movie('School of Rock', 'Using rock music to learn',
                       'https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg',
                       'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = Movie('Ratatouille', 'A rat is a chef in Paris',
                    'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                    'https://www.youtube.com/watch?v=uVeNEbh3A4U')

midnight_in_paris = Movie('Midnight in Paris',
                          'Going back in time to meet the authors',
                          'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                          'https://www.youtube.com/watch?v=wuOUdZjuCIA')

hunger_games = Movie('Hunger Games', 'A really real reality show',
                     'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                     'https://www.youtube.com/watch?v=LrXIG4oK7Ew')

movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
