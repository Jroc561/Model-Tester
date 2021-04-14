from os import getenv
from flask import Flask, render_template, request
from dotenv import load_dotenv
from .models import 


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html', title="Home")

    @app.route("/music", methods = ["GET", "POST"]) 
    def input():
        """ 
        Input user's favorite song.
        Return list of recommended songs.
        """
        if request.method == "GET":
            track_artist = to_list(df)
            return render_template('input.html', data=track_artist)
        
        if request.method == "POST":
            input = request.form.get("input")
            index = df.loc[df.isin([input]).any(axis=1)].index.tolist()
            index = index[0]
            model = song_model(index)
            return render_template('output_song.html', output_song=input, recommended_song=model)

    return app