import requests
import csv
import time

API_KEY = "58ec81c997837a91a219ed2b46e63240"
BASE_URL = "https://api.themoviedb.org/3"

OUTPUT_FILE = "movies.csv"

FIELDS = [
    "id", "title", "release_date", "popularity",
    "vote_average", "vote_count", "genre_ids",
    "original_language"
]

def fetch_page(page):
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": API_KEY,
        "page": page
    }

    try:
        r = requests.get(url, params=params, timeout=10)

        if r.status_code != 200:
            print("ERROR:", r.status_code, r.text)
            return []

        data = r.json()
        return data.get("results", [])

    except Exception as e:
        print("REQUEST ERROR:", e)
        return []


def save_batch(rows, file, header=False):
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)

        if header:
            writer.writeheader()

        for row in rows:
            writer.writerow(row)


def transform(movie):
    return {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "release_date": movie.get("release_date"),
        "popularity": movie.get("popularity"),
        "vote_average": movie.get("vote_average"),
        "vote_count": movie.get("vote_count"),
        "genre_ids": "|".join(map(str, movie.get("genre_ids", []))),
        "original_language": movie.get("original_language")
    }


def run_scraper(pages=250):
    batch = []
    first = True

    for page in range(1, pages + 1):
        print(f"Fetching page {page}...")

        movies = fetch_page(page)

        if not movies:
            print("No data → stopping")
            break

        for m in movies:
            batch.append(transform(m))

        # 💾 ukládání po 50 řádcích
        if len(batch) >= 50:
            save_batch(batch, OUTPUT_FILE, header=first)
            first = False
            batch = []
            print("Saved 50 rows")

        time.sleep(0.3)  # anti-rate-limit

    # poslední zbytek
    if batch:
        save_batch(batch, OUTPUT_FILE, header=first)

    print("DONE")


run_scraper(250)