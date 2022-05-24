from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.sequence import SequenceRepository, Sequence


def test_should_save_new_sequence_with_its_information_attached():
    sequence_repository = SequenceRepository(temp_file())
    app = create_app(repositories={"sequence": sequence_repository})
    client = app.test_client()

    sequence1 = Sequence(
        id="001",
        sequence="TTTGGGCCCGGG",
        name="virus",
        mutation="A",
        mut_location="10",
        information=" virus procedente del norte de europa",
    )

    sequence_repository.save(sequence1)
    body = {
        "id": "001",
        "sequence": "TTTGGGCCCAAA",
        "name": "virus",
        "mutation": "A",
        "mut_location": "10",
        "information": " virus procedente del norte de europa",
    }
    response_put = client.put("/api/sequences/001", json=body)
    assert response_put.status_code == 200

    response_get = client.get("/api/sequences/001")
    assert response_get.json == {
        "id": "001",
        "sequence": "TTTGGGCCCAAA",
        "name": "virus",
        "mutation": "A",
        "mut_location": "10",
        "information": " virus procedente del norte de europa",
    }
