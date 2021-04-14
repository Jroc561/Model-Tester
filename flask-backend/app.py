from os import getenv
from flask import Flask, render_template, request
from dotenv import load_dotenv
from .models import to_list


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html', title="Home")

    @app.route("/input", methods = ["GET", "POST"]) 
    def input():
        """ 
        Input user's NFT.
        Return reccomended value.
        """
        if request.method == "GET":
            NFT_id = to_list(df)
            return render_template('input.html', data=NFT_id)
        
        if request.method == "POST":
            input = request.form.get("input")
            index = df.loc[df.isin([input]).any(axis=1)].index.tolist()
            index = index[0]
            model = song_model(index)
            return render_template('output_song.html', output_song=input, recommended_song=model)

    return app