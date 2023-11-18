from flask import Flask, jsonify, request
from scraper import *
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MovieSearch(Resource):
    def get(self, movieName):
        a = searchShow(movieName)
        return jsonify({"data": a})


class ShowLinks(Resource):
    def get(self):
        # Extract movie link from headers
        movieLink = request.headers.get("link")

        # Perform your logic with the movieLink (e.g., getWatchLinks(movieLink))
        a = getWatchLinks(movieLink)
        return jsonify({"data": a})


api.add_resource(MovieSearch, "/moviesearch/<string:movieName>")
api.add_resource(ShowLinks, "/showlinks")

if __name__ == "__main__":
    app.run(debug=True)
