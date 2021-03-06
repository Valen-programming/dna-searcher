from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.sequence import SequenceRepository, Sequence


def test_should_matched_a_new_sequence_with_a_database_sequence():

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

    sequence2 = Sequence(
        id="002",
        sequence="TTTAAACCCGGG",
        category="virus",
        name="e.coli",
        mutation="B",
        mut_location="10",
        information=" virus procedente del sudeste asiatico  blab blab bla",
    )
    sequence_repository.save(sequence1)
    sequence_repository.save(sequence2)

    response = client.post("/api/alignments", json={"sequence": "TTTAAACCCGGG"})

    # assert response.status_code == 200
    assert response.json == {
        "id": "002",
        "sequence": "TTTAAACCCGGG",
        "category": "virus",
        "name": "e.coli",
        "mutation": "B",
        "mut_location": "10",
        "information": " virus procedente del sudeste asiatico  blab blab bla",
    }
