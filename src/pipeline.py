import pandas as pd
import numpy as np
from datetime import datetime
TMDB_API_KEY = "58ec81c997837a91a219ed2b46e63240"
def create_features(df, training=True):
    df = df.copy()

    # =========================
    # TRAINING ONLY CLEANING
    # =========================
    if training:
        df = df.dropna(subset=["vote_average", "vote_count", "popularity", "release_date"])
    else:
        df = df.dropna(subset=["vote_count", "popularity", "release_date"])

    # =========================
    # DATE FEATURES
    # =========================
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df = df.dropna(subset=["release_date"])

    df["release_year"] = df["release_date"].dt.year
    df["release_month"] = df["release_date"].dt.month

    # =========================
    # ENGINEERING
    # =========================
    df["film_age"] = (2026 - df["release_year"]).clip(lower=0)

    df["log_vote_count"] = np.log1p(df["vote_count"])
    df["log_popularity"] = np.log1p(df["popularity"])

    df["engagement_ratio"] = df["vote_count"] / (df["popularity"] + 1)
    df["votes_per_year"] = df["vote_count"] / (df["film_age"] + 1)

    # =========================
    # DROP RAW COLUMNS
    # =========================
    df = df.drop(columns=[
        "title",
        "genre_ids",
        "original_language",
        "release_date"
    ], errors="ignore")

    return df