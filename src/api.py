import requests

TMDB_API_KEY = "58ec81c997837a91a219ed2b46e63240"

def get_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "vote_count": data.get("vote_count"),
        "popularity": data.get("popularity"),
        "release_date": data.get("release_date"),
        "genre_ids": "|".join(str(g["id"]) for g in data.get("genres", [])),
        "original_language": data.get("original_language"),
        "title": data.get("title"),
        "vote_average": data.get("vote_average")
    }