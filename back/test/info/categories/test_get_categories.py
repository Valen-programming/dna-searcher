from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.categories import CategoryRepository, Category


def test_should_get_categories():

    categories_repository = CategoryRepository(temp_file())
    app = create_app(repositories={"category": categories_repository})
    client = app.test_client()

    categoria_1 = Category(category_id="cat-1", category_name="Virus")
    categoria_2 = Category(category_id="cat-2", category_name="Bacteria")
    categoria_3 = Category(category_id="cat-3", category_name="Hongo")
    categoria_4 = Category(category_id="cat-4", category_name="Planta")
    categoria_5 = Category(category_id="cat-5", category_name="Animal")
    categoria_6 = Category(category_id="cat-6", category_name="Humano")

    categories_repository.save(categoria_1)
    categories_repository.save(categoria_2)
    categories_repository.save(categoria_3)
    categories_repository.save(categoria_4)
    categories_repository.save(categoria_5)
    categories_repository.save(categoria_6)

    response = client.get("/api/categories")

    assert response.json == [
        {
            "category_id": "cat-1",
            "category_name": "Virus",
        },
        {
            "category_id": "cat-2",
            "category_name": "Bacteria",
        },
        {
            "category_id": "cat-3",
            "category_name": "Hongo",
        },
        {
            "category_id": "cat-4",
            "category_name": "Planta",
        },
        {
            "category_id": "cat-5",
            "category_name": "Animal",
        },
        {
            "category_id": "cat-6",
            "category_name": "Humano",
        },
    ]
