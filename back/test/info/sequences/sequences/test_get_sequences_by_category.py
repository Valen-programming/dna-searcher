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
        name="papiloma",
        mutation="A",
        mut_location="10",
        information="virus regogido del paciente de un hospital en Bélgica",
    )
    sequence2 = Sequence(
        id="002",
        sequence="TTTGGGCCCGGG",
        category="bacteria",
        name="salmonella",
        mutation="A",
        mut_location="10",
        information=" bacteria procedente del norte de España ",
    )
    sequence3 = Sequence(
        id="003",
        sequence="TTTGGGCCCGGG",
        category="bacteria",
        name="salmonella",
        mutation="A",
        mut_location="10",
        information=" bacteria procedente del sur de Francia",
    )
    sequence4 = Sequence(
        id="004",
        sequence="TTTGGGCCCGGG",
        category="bacteria",
        name="salmonella",
        mutation="A",
        mut_location="10",
        information=" bacteria procedente del sur de Holanda ",
    )

    sequence_repository.save(sequence1)
    sequence_repository.save(sequence2)
    sequence_repository.save(sequence3)
    sequence_repository.save(sequence4)

    response = client.get("/api/categories/bacteria")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": "002",
            "sequence": "TTTGGGCCCGGG",
            "category": "bacteria",
            "name": "salmonella",
            "mutation": "A",
            "mut_location": "10",
            "information": " bacteria procedente del norte de España ",
        },
        {
            "id": "003",
            "sequence": "TTTGGGCCCGGG",
            "category": "bacteria",
            "name": "salmonella",
            "mutation": "A",
            "mut_location": "10",
            "information": " bacteria procedente del sur de Francia",
        },
        {
            "id": "004",
            "sequence": "TTTGGGCCCGGG",
            "category": "bacteria",
            "name": "salmonella",
            "mutation": "A",
            "mut_location": "10",
            "information": " bacteria procedente del sur de Holanda ",
        },
    ]
