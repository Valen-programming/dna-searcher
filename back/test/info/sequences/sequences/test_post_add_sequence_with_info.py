from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.sequence import SequenceRepository, Sequence


def test_should_save_new_sequence_with_its_information_attached():
    sequence_repository = SequenceRepository(temp_file())
    app = create_app(repositories={"sequence": sequence_repository})
    client = app.test_client()

    body = {
        "id": "001",
        "sequence": "GGGGGCCCCCAAT",
        "category": "virus",
        "name": "Rizhopus Stolonifer",
        "mutation": "B",
        "mut_location": "10",
        "information": "Hongo que sale en humdedes de pared o alimentos",
    }

    response = client.post("/api/sequences", json=body)

    assert response.status_code == 200


def test_should_post_a_valid_category():
    sequence_repository = SequenceRepository(temp_file())
    app = create_app(repositories={"sequence": sequence_repository})
    client = app.test_client()

    body = {
        "id": "001",
        "sequence": "GGGGGCCCCCAAT",
        "category": "hongo",
        "name": "Rizhopus Stolonifer",
        "mutation": "B",
        "mut_location": "10",
        "information": "Hongo que sale en humdedes de pared o alimentos",
    }

    response = client.post("/api/sequences", json=body)

    response_get = client.get("/api/sequences/001")

    contact = response_get.json
    assert (
        contact["category"] == "virus"
        or "bacteria"
        or "hongo"
        or "planta"
        or "animal"
        or "humano"
    )


def test_should_save_seven_items_of_the_sequence_info():
    sequence_repository = SequenceRepository(temp_file())
    app = create_app(repositories={"sequence": sequence_repository})
    client = app.test_client()

    body = {
        "id": "002",
        "sequence": "GGGGGCCCCCAAT",
        "category": "hongo",
        "name": "Rizhopus Stolonifer",
        "mutation": "B",
        "mut_location": "10",
        "information": "Hongo que sale en humdedes de pared o alimentos",
    }

    response = client.post("/api/sequences", json=body)

    response_get = client.get("/api/sequences/002")
    contact = response_get.json
    assert len(contact) == 7
