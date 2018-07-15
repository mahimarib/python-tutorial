from movie import Movie

toy_story_title = "Toy Story"
toy_story_storyline = "Toys come to life"
toy_story_poster = "https://en.wikipedia.org/wiki/File:Toy_Story.jpg"
toy_story_trailer_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc"

avatar_title = "Avatar"
avatar_story_line = "A marine on an alien planet"
avatar_poster = "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg"
avatar_trailer_url = "https://www.youtube.com/watch?v=uZNHIU3uHT4"

school_of_rock_title = "School of Rock"
school_of_rock_storyline = "Using rock musicc to learn"
school_of_rock_poster = "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg"
school_of_rock_trailer_url = "https://www.youtube.com/watch?v=3PsUJFEBC74"

toy_story = Movie(toy_story_title, toy_story_storyline,
                  toy_story_poster, toy_story_trailer_url)

avatar = Movie(avatar_title, avatar_story_line,
               avatar_poster, avatar_trailer_url)

school_of_rock = Movie(school_of_rock_title, school_of_rock_storyline,
                       school_of_rock_poster, school_of_rock_trailer_url)

# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
