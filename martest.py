import requests

api_key = '947ef8e02ab59c3bf38081308f1da3b1'
url = f'https://api.themoviedb.org/3/movie/550?api_key={api_key}'
r = requests.get(url)
print(r.text)

