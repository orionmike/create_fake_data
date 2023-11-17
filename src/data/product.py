
import random
from faker import Faker
from data.utils import get_random_number, get_slug
from database.database import session_maker
from database.models_product import CategoryProduct, Product


def create_category_list(user_count: int, delete=True) -> None:

    with session_maker() as session:

        if not delete:
            session.query(CategoryProduct).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        for _ in range(user_count):

            category = CategoryProduct()

            category.name = f'Категория {get_random_number(3)}'
            category.slug = get_slug(category.name)
            category.is_published = True
            category.description = faker.paragraph(nb_sentences=1)

            session.add(category)

        session.commit()


def create_product_list(product_count: int, delete=True) -> None:

    with session_maker() as session:

        if not delete:
            session.query(Product).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        category_list = session.query(CategoryProduct).all()
        session.commit()

        for _ in range(product_count):

            random_category = random.choice(category_list)

            product = Product()

            product.name = f'Товар {get_random_number(4)}'
            product.slug = get_slug(product.name)

            product.category_id = random_category.id
            product.price = random.randint(100, 1000)
            product.is_published = True
            product.description = faker.paragraph(nb_sentences=1)

            session.add(product)

        session.commit()
