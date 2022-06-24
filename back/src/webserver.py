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

    @app.route("/api/sequences/<id>", methods=["GET"])
    def get_sequence_by_id(id):
        sequence_with_info = repositories["sequence"].get_sequence_by_id(id)
        return object_to_json(sequence_with_info), 200

    @app.route("/api/sequences/<id>", methods=["PUT"])
    def edit_sequence_and_its_information(id):
        data = request.json
        sequence_with_info = Sequence(**data)
        repositories["sequence"].edit_sequence(id, sequence_with_info)
        return ("", 200)

    @app.route("/api/categories", methods=["GET"])
    def get_categories():
        categories = repositories["category"].get_categories()
        return object_to_json(categories)

    @app.route("/api/categories/<category>", methods=["GET"])
    def get_sequence_by_category(category):
        sequence_with_info = repositories["sequence"].get_sequence_by_category(category)
        return object_to_json(sequence_with_info), 200

    return app
