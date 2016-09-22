import random

if __name__ == '__main__':
  list_of_movies = []
  with open('./data/download/movie_titles.txt') as input_stream:
    for line in input_stream:
      new_movie = line.split(',')[2]
      list_of_movies.append(new_movie)

  print(len(list_of_movies))
  random_movies = random.sample(list_of_movies, 5)
  for movie in random_movies:
    print(movie)
