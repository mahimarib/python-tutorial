from movie import Movie
import fresh_tomatoes

toy_story_title = 'Toy Story'
toy_story_storyline = 'Toys come to life'
toy_story_poster = 'https://en.wikipedia.org/wiki/File:Toy_Story.jpg'
toy_story_trailer_url = 'https://www.youtube.com/watch?v=KYz2wyBy3kc'

avatar_title = 'Avatar'
avatar_story_line = 'A marine on an alien planet'
avatar_poster = 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg'
avatar_trailer_url = 'https://www.youtube.com/watch?v=uZNHIU3uHT4'

school_of_rock_title = 'School of Rock'
school_of_rock_storyline = 'Using rock music to learn'
school_of_rock_poster = 'https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg'
school_of_rock_trailer_url = 'https://www.youtube.com/watch?v=3PsUJFEBC74'

ratatouille_title = 'Ratatouille'
ratatouille_storyline = 'A rat is a chef in Paris'
ratatouille_poster = 'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg'
ratatouille_trailer_url = 'https://www.youtube.com/watch?v=uVeNEbh3A4U'

midnight_in_paris_title = 'Midnight in Paris'
midnight_in_paris_storyline = 'Going back in time to meet the authors'
midnight_in_paris_poster = 'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg'
midnight_in_paris_trailer_url = 'https://www.youtube.com/watch?v=wuOUdZjuCIA'

hunger_games_title = 'Hunger Games'
hunger_games_storyline = 'A really real reality show'
hunger_games_poster = 'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg'
hunger_games_trailer_url = 'https://www.youtube.com/watch?v=LrXIG4oK7Ew'

toy_story = Movie(toy_story_title, toy_story_storyline,
                  toy_story_poster, toy_story_trailer_url)

avatar = Movie(avatar_title, avatar_story_line,
               avatar_poster, avatar_trailer_url)

school_of_rock = Movie(school_of_rock_title, school_of_rock_storyline,
                       school_of_rock_poster, school_of_rock_trailer_url)

ratatouille = Movie(ratatouille_title, ratatouille_storyline,
                    ratatouille_poster, ratatouille_trailer_url)


midnight_in_paris = Movie(midnight_in_paris_title,
                          midnight_in_paris_storyline,
                          midnight_in_paris_poster,
                          midnight_in_paris_trailer_url)

hunger_games = Movie(hunger_games_title, hunger_games_storyline,
                     hunger_games_poster, hunger_games_trailer_url)

movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
