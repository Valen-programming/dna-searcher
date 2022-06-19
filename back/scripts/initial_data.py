import sys

sys.path.insert(0, "")

import sqlite3

from src.domain.sequence import SequenceRepository, Sequence

database_path = "data/database.db"

sequence1 = Sequence(
    id="001",
    sequence="TTTGGGCCCGGG",
    category="virus",
    name="Viruela",
    mutation="A",
    mut_location="3",
    information=" virus procedente del norte de europa",
)

sequence2 = Sequence(
    id="002",
    sequence="TTTAAACCCGGG",
    category="virus",
    name="Epstein barr",
    mutation="B",
    mut_location="3",
    information=" virus procedente del sudeste asiatico ",
)
sequence3 = Sequence(
    id="003",
    sequence="AAAGGGCCCGGG",
    category="virus",
    name="Papiloma",
    mutation="A",
    mut_location="1",
    information=" virus procedente del continente americano",
)

sequence4 = Sequence(
    id="004",
    sequence="GGGAAACCCGGG",
    category="virus",
    name="VIH",
    mutation="B",
    mut_location="1",
    information=" virus procedente de las islas Fidgi",
)
# bacterias--------------------------------------------
sequence5 = Sequence(
    id="005",
    sequence="TTTGGGCCCGGG",
    category="bacteria",
    name="E.coli",
    mutation="A",
    mut_location="3",
    information=" Extraida del estomago de una vaca en Indonesia",
)

sequence6 = Sequence(
    id="006",
    sequence="TTTAAACCCGGG",
    category="bacteria",
    name="Salmonella",
    mutation="B",
    mut_location="3",
    information=" Extraida de un paciente de síntomas muy graves en el norte de España ",
)
sequence7 = Sequence(
    id="007",
    sequence="AAAGGGCCCGGG",
    category="bacteria",
    name="E.coli",
    mutation="B",
    mut_location="1",
    information=" Extraída de un paciente al sur de Francia, sintomatología media",
)
# Hongos-----------------------------------------
sequence8 = Sequence(
    id="008",
    sequence="TTTGGGCCCGGG",
    category="hongo",
    name="Rizopus stolonifer",
    mutation="A",
    mut_location="3",
    information="Moho recogido en las muestras de la fábrica Bimbo",
)

sequence9 = Sequence(
    id="009",
    sequence="TTTAAACCCGGG",
    category="hongo",
    name="Saccharomyces cerevisiae",
    mutation="B",
    mut_location="3",
    information=" Levadura recogida en la fábrica de cervezas Keller ",
)
sequence10 = Sequence(
    id="0010",
    sequence="AAAGGGCCCGGG",
    category="hongo",
    name="Dermatofito",
    mutation="B",
    mut_location="1",
    information=" Hongo extraído de las muestras de piel de un paciente con pie de atleta en el sur de Alemania",
)
# plantas-------------------------------
sequence11 = Sequence(
    id="0011",
    sequence="TTTGGGCCCGGG",
    category="planta",
    name="Vitis vinifera",
    mutation="A",
    mut_location="3",
    information="Planta de los viñedos de la Rioja",
)

sequence12 = Sequence(
    id="0012",
    sequence="TTTAAACCCGGG",
    category="planta",
    name="Humulus lupulus",
    mutation="B",
    mut_location="3",
    information=" Planta de Lúpulo procedente de los cultivos de Toledo destinado a la fabricación de cerveza  ",
)
sequence13 = Sequence(
    id="0013",
    sequence="AAAGGGCCCGGG",
    category="planta",
    name="Saccharum officinarum",
    mutation="B",
    mut_location="1",
    information=" Planta de caña de azúcar de las plantaciones azucareras de Cuba",
)
# Animales---------------------------------
sequence14 = Sequence(
    id="0014",
    sequence="TTTAAACCCGGG",
    category="animal",
    name="Mus musculus",
    mutation="B",
    mut_location="3",
    information=" Ratón de campo de la Península Ibérica  ",
)
sequence15 = Sequence(
    id="0015",
    sequence="AAAGGGCCCGGG",
    category="animal",
    name="lupus nomen",
    mutation="B",
    mut_location="1",
    information=" Lobo del paruqe nacional de Yellowstone en Norte América",
)
# Humanos--------------------------------------------------------
sequence16 = Sequence(
    id="0016",
    sequence="TTTAAACCCGGG",
    category="humano",
    name="Homo neanderthalensis",
    mutation="B",
    mut_location="3",
    information=" Muestra extraída de restos arqueológicos que datan del año 100.000 antes de cristo, hallados en unas cuevas al sur de Francia  ",
)
sequence17 = Sequence(
    id="0017",
    sequence="AAAGGGCCCGGG",
    category="humano",
    name="Homo sapiens",
    mutation="B",
    mut_location="1",
    information=" Muestra de un individuo del norte de europa con enfermedad de chrome avanzada",
)


sequence_repository = SequenceRepository(database_path)
sequence_repository.save(sequence1)
sequence_repository.save(sequence2)
sequence_repository.save(sequence3)
sequence_repository.save(sequence4)

sequence_repository.save(sequence5)
sequence_repository.save(sequence6)
sequence_repository.save(sequence7)

sequence_repository.save(sequence8)
sequence_repository.save(sequence9)
sequence_repository.save(sequence10)

sequence_repository.save(sequence11)
sequence_repository.save(sequence12)
sequence_repository.save(sequence13)

sequence_repository.save(sequence14)
sequence_repository.save(sequence15)

sequence_repository.save(sequence16)
sequence_repository.save(sequence17)
