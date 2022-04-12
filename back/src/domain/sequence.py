import sqlite3


class Sequence:
    def __init__(self, sequence, name, mutation, mut_location, information):
        self.sequence = sequence
        self.name = name
        self.mutation = mutation
        self.mut_location = mut_location
        self.information = information

    def to_dict(self):
        return {
            "sequence": self.sequence,
            "name": self.name,
            "mutation": self.mutation,
            "mut_location": self.mut_location,
            "information": self.information,
        }


class SequenceRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
        CREATE TABLE if not exists sequences (
            sequence varchar,
            name varchar,
            mutation varchar,
            mut_location varchar,
            information varchar)"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def save(self, new_sequence):
        sql = """ INSERT INTO sequences 
        (sequence,name, mutation, mut_location, information) 
        values 
        ( :sequence, :name, :mutation, :mut_location, :information)
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "sequence": new_sequence.sequence,
                "name": new_sequence.name,
                "mutation": new_sequence.mutation,
                "mut_location": new_sequence.mut_location,
                "information": new_sequence.information,
            },
        )

        conn.commit()

    def new_sequence_matcher(self, sequence):
        sql = """ SELECT * FROM sequences WHERE sequence = :sequence"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"sequence": sequence})
        data = cursor.fetchall()

        sequences = []
        for item in data:
            contact = Sequence(**item)
            sequences.append(contact)

        return sequences
