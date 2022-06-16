import sqlite3
from src.webserver import create_app
from src.domain.info import InfoRepository
from src.domain.sequence import SequenceRepository
from src.domain.categories import CategoryRepository


database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "sequence": SequenceRepository(database_path),
    "category": CategoryRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
