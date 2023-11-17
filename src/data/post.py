import random
from faker import Faker
from data.utils import get_random_number, get_slug
from database.database import session_maker
from database.models_post import CategoryPost, Post, Tag, AssociationPostTag
from database.models_user import User


def create_category_post_list(count_category: int, delete=True) -> None:

    with session_maker() as session:
        if not delete:
            session.query(CategoryPost).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        for _ in range(count_category):

            category = CategoryPost()

            category.name = f'Категория постов {get_random_number(3)}'
            category.slug = get_slug(category.name)
            category.is_published = True
            category.description = faker.paragraph(nb_sentences=2)

            session.add(category)
            session.commit()


def create_tag_list(count_tag: int, delete=True) -> None:

    with session_maker() as session:
        if not delete:
            session.query(Tag).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        for _ in range(count_tag):

            tag = Tag()

            tag.name = faker.word()
            tag.slug = get_slug(tag.name)
            tag.is_published = True
            tag.description = faker.paragraph(nb_sentences=1)

            session.add(tag)
            session.commit()


def create_post_list(count_post: int, delete=True) -> None:

    with session_maker() as session:
        if not delete:
            session.query(Post).delete()
            session.commit()
            session.query(AssociationPostTag).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        category_list = session.query(CategoryPost).all()
        tag_list = session.query(Tag).all()
        user_list = session.query(User).all()
        session.commit()

        for _ in range(count_post):

            random_category = random.choice(category_list)
            random_user = random.choice(user_list)

            post = Post()

            post.name = faker.paragraph(nb_sentences=1)
            post.slug = get_slug(post.name)
            post.category_id = random_category.id

            post.user_id = random_user.id
            post.is_published = True

            post.prewiew_text = faker.paragraph(nb_sentences=2)
            post.full_text = faker.paragraph(nb_sentences=5)

            session.add(post)
            session.commit()

            random_tag_list = set(random.choices(tag_list, k=4))

            for tag in random_tag_list:
                post.tags.append(tag)

            session.commit()
