import sqlite3


class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
        }


class CategoryRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql1 = """
            create table if not exists categories (
                category_id varchar PRIMARY KEY,
                category_name text
                );

            create table if not exists sequencescategories (
                id VARCHAR,
                category_id VARCHAR,
                FOREIGN KEY (id) REFERENCES sequences(id),
                FOREIGN KEY (category_id) REFERENCES categories(category_id)
				
                )
          
            """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.executescript(sql1)
        conn.commit()
        conn.close()

    def get_categories(self):
        sql = """select * from categories """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        categories = [Category(**item) for item in data]
        conn.close()
        return categories

    def save(self, categories):
        sql = """insert into categories (category_id,category_name) values (:category_id, :category_name) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, categories.to_dict())
        # self.save_event_categories(cursor, event_id, categories)
        conn.commit()
        conn.close()
