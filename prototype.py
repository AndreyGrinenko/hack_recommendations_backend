import os
import glob
import numpy

NUMBER_OF_MOVIES = 1000
NUMBER_OF_USERS = 10 ** 4

if __name__ == '__main__':
  ratings = numpy.zeros((17770, 2650000), dtype=numpy.uint8)
  sorted_files = sorted(glob.glob('./data/download/training_set/*.txt'))[:NUMBER_OF_MOVIES]
  for file_name in sorted_files:
    print(file_name)
    with open(file_name) as input_stream:
      input_stream.readline()
      movie_id = int(file_name.split('/')[-1][3:-4])
      for line in input_stream:
        user_id = int(line.split(',')[0])
        rating = int(line.split(',')[1])
        ratings[movie_id, user_id] = rating

  # numpy.set_printoptions(threshold=numpy.nan)
  # print(ratings[:50,:50])
  # raw_input()

  # numpy.save('./data/ratings.npy', ratings)

  # ratings = numpy.load('./data/ratings.npy')

  similarity_table = numpy.zeros((NUMBER_OF_MOVIES + 1, NUMBER_OF_MOVIES + 1))
  for movie_id in xrange(1, NUMBER_OF_MOVIES + 1, 1):
    for user_id in xrange(NUMBER_OF_USERS):
      if ratings[movie_id, user_id] != 0:
        # print(list(ratings[0:NUMBER_OF_MOVIES, user_id]))
        # raw_input()
        for similar_id in xrange(1, 1 + NUMBER_OF_MOVIES, 1):
          if ratings[similar_id, user_id] != 0 and similar_id != movie_id:
            similarity_table[similar_id, movie_id] += 1

  numpy.set_printoptions(threshold=numpy.nan)
  print(similarity_table)[:10]

  for i in xrange(4):
    print('')

  id_to_title = dict()
  with open('./data/download/movie_titles.txt') as input_stream:
    for line in input_stream:
      movie_id = int(line.split(',')[0])
      movie_title = line[:-1].split(',')[2]
      id_to_title[movie_id] = movie_title

  # for test_id in xrange(1, 51, 1):
  #   movie_title = id_to_title[test_id]
  #   similar_id = numpy.argmax(similarity_table[:, test_id])
  #   similar_title = ['none' if similar_id == 0 else id_to_title[similar_id]]
  #   print(test_id, similar_id)
  #   print(movie_title, similar_title)
  #   raw_input()

  with open('./data/similarity_output.txt', 'w') as output_stream:
    for movie_id in xrange(1, NUMBER_OF_MOVIES + 1, 1):
      similar_id = numpy.argmax(similarity_table[:, movie_id])
      output_stream.write(str(movie_id) + ',' + str(similar_id) + '\n')

