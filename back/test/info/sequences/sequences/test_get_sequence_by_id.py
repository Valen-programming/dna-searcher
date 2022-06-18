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
        category="virus",
        name="salmonella",
        mutation="A",
        mut_location="10",
        information=" virus procedente del norte de europa",
    )

    sequence_repository.save(sequence1)
    response = client.get("/api/sequences/001")

    assert response.status_code == 200
    assert response.json == {
        "id": "001",
        "sequence": "TTTGGGCCCGGG",
        "category": "virus",
        "name": "salmonella",
        "mutation": "A",
        "mut_location": "10",
        "information": " virus procedente del norte de europa",
    }
