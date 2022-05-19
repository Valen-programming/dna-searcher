import sys

sys.path.insert(0, "")

import sqlite3

from src.domain.sequence import SequenceRepository, Sequence

database_path = "data/database.db"

sequence1 = Sequence(
    id="001",
    sequence="TTTGGGCCCGGG",
    name="virus",
    mutation="A",
    mut_location="3",
    information=" virus procedente del norte de europa",
)

sequence2 = Sequence(
    id="002",
    sequence="TTTAAACCCGGG",
    name="virus",
    mutation="B",
    mut_location="3",
    information=" virus procedente del sudeste asiatico ",
)
sequence3 = Sequence(
    id="003",
    sequence="AAAGGGCCCGGG",
    name="virus",
    mutation="A",
    mut_location="1",
    information=" virus procedente del continente americano",
)

sequence4 = Sequence(
    id="004",
    sequence="GGGAAACCCGGG",
    name="virus",
    mutation="B",
    mut_location="1",
    information=" virus procedente de las islas Fidgi",
)


sequence_repository = SequenceRepository(database_path)
sequence_repository.save(sequence1)
sequence_repository.save(sequence2)
sequence_repository.save(sequence3)
sequence_repository.save(sequence4)
