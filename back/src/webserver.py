from flask import Flask, request
from flask_cors import CORS
from src.domain.sequence import Sequence

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/wii", methods=["GET"])
    def first_connection_with_webserver():
        return "wiii i finaly learned how this works"

    @app.route("/api/alignments", methods=["POST"])
    def get_new_sequence_matched_with_database_sequence():
        body = request.json
        sequence = body["sequence"]
        matched_sequence = repositories["sequence"].new_sequence_matcher(sequence)
        return object_to_json(matched_sequence), 200

    @app.route("/api/sequences", methods=["POST"])
    def save_new_sequence_and_its_information():
        data = request.json
        sequence_with_info = Sequence(**data)
        repositories["sequence"].save(sequence_with_info)
        return ("", 200)

    return app
