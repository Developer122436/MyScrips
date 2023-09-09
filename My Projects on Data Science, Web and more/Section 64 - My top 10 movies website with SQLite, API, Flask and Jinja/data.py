import requests

url = "https://api.themoviedb.org/3/movie/550?api_key=f841b381713312e703c4efa41b025774"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODQxYjM4MTcxMzMxMmU3MDNjNGVmYTQxYjAyNTc3NCIsInN1YiI6IjY0ZmNiMzM2ZWZlYTdhMDBmZDE5OTg2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aNGDj-SNNVl2UnVIN2r_dmZn7Z7x8RIV0qxgMJJVv7c"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)