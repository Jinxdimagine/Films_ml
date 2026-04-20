import streamlit as st
import pandas as pd
import joblib
from pipeline import create_features
from api import get_movie

# load model + features
model = joblib.load("models/xgb_model.pkl")
features = joblib.load("models/features.pkl")

st.title(" TMDB Movie Rating Predictor")

# input
movie_id = st.text_input("Enter TMDB Movie ID")

if st.button("Predict rating"):

    # získání dat z API
    data = get_movie(movie_id)

    # kontrola
    if not data or data.get("vote_count") is None:
        st.error("Movie not found!")
    else:
        # vytvoření dataframe
        input_df = pd.DataFrame([{
            "vote_count": data["vote_count"],
            "popularity": data["popularity"],
            "release_date": data["release_date"],
            "genre_ids": data["genre_ids"],
            "original_language": data["original_language"],
            "vote_average": 0  # dummy pro pipeline
        }])

        # feature engineering (STEJNÝ jako training!)
        input_df = create_features(input_df, training=False)

        # zarovnání na training features
        input_df = input_df.reindex(columns=features, fill_value=0)

        # predikce
        prediction = model.predict(input_df)[0]

        # výstup
        st.success(f" Predicted rating: {prediction:.2f}")

        # bonus info
        st.write(f" {data.get('title', 'Unknown title')}")
        st.write(f" Actual rating: {data.get('vote_average', 'N/A')}")

        # debug (můžeš klidně smazat)
        st.json(data)