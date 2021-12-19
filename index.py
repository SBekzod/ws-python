import requests
import pprint

api_key = '947ef8e02ab59c3bf38081308f1da3b1'
url = f'https://api.themoviedb.org/3/movie/550?api_key={api_key}'
r = requests.get(url)
# print(r.content)
# print(r['poster_path'])
# pprint.pprint(r.json())
data = r.json()
poster = data['poster_path']
print(poster)

url_sec = f'https://image.tmdb.org/t/p/w500/{poster}'
r_two = requests.get(url_sec)
print(r_two.status_code)


