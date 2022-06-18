import sqlite3


class Sequence:
    def __init__(
        self, id, sequence, category, name, mutation, mut_location, information
    ):
        self.id = id
        self.sequence = sequence
        self.category = category
        self.name = name
        self.mutation = mutation
        self.mut_location = mut_location
        self.information = information

    def to_dict(self):
        return {
            "id": self.id,
            "sequence": self.sequence,
            "category": self.category,
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
            id varchar,
            sequence varchar,
            category varchar,
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
        (id,sequence,category,name, mutation, mut_location, information) 
        values 
        ( :id, :sequence,:category, :name, :mutation, :mut_location, :information)
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, new_sequence.to_dict())

        conn.commit()

    def new_sequence_matcher(self, sequence):
        sql = """ SELECT * FROM sequences WHERE sequence = :sequence"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"sequence": sequence})
        data = cursor.fetchone()
        sequence_info = Sequence(**data)
        return sequence_info

    def get_sequence_by_id(self, id):
        sql = """SELECT * FROM sequences WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        data = cursor.fetchone()
        sequence_info = Sequence(**data)
        return sequence_info

    def edit_sequence(self, id, event):
        sql = """UPDATE sequences
            SET id= :id, sequence= :sequence, category= :category,name= :name, mutation= :mutation, mut_location = :mut_location, information = :information
            WHERE id = :id 
            """

        conn = self.create_conn()
        cursor = conn.cursor()
        params = event.to_dict()
        params["id"] = id
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def get_sequence_by_category(self, category):
        sql = """SELECT * FROM sequences WHERE category = :category"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"category": category})
        data = cursor.fetchall()

        sequences = []
        for item in data:
            sequence_with_info = Sequence(**item)
            sequences.append(sequence_with_info)

        return sequences
