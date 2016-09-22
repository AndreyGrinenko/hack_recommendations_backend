import urllib
import urllib2

PREDICT_URL = 'http://185.147.83.57:5000/'

if __name__ == '__main__':
  # sending_data = urllib.urlencode({'userId': '12', 'movieId': '1'})
  # request = urllib2.Request(PREDICT_URL, sending_data)

  sending_data = urllib.urlencode({'userId': '1'})
  request = urllib2.Request(PREDICT_URL + 'request_movies', sending_data)

  # sending_data = urllib.urlencode({'userId': '1', 'movieId': '16'})
  # request = urllib2.Request(PREDICT_URL + 'post_movie', sending_data)

  response = urllib2.urlopen(request)
  print(response.read())

  # request = urllib2.Request(PREDICT_URL)
  # response = urllib2.urlopen(request)
  # print(response.read())

