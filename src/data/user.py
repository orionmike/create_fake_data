
import random
import string
import uuid

from faker import Faker

from data.utils import get_random_string, get_slug
from database.database import session_maker
from database.models_user import User

GENDER_TUPLE = ('m', 'f')


def get_name(fake: Faker, gender: str) -> tuple:
    if gender == 'm':
        return fake.first_name_male(), fake.last_name_male()
    if gender == 'f':
        return fake.first_name_female(), fake.last_name_female()


def get_phone() -> str:
    return '+79' + ''.join(random.choice(string.digits) for _ in range(9))


def get_email(person: tuple) -> str:
    return f'{get_slug(person[0])}_{get_slug(person[1])}@{get_random_string(3,5)}.{get_random_string(2,3)}'


def create_user_list(user_count: int, delete=True) -> None:

    with session_maker() as session:

        if not delete:
            session.query(User).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        for _ in range(user_count):

            user = User()

            user.uuid_user = str(uuid.uuid4())

            person = get_name(faker, random.choice(GENDER_TUPLE))
            user.first_name, user.last_name = person

            user.email = get_email(person)
            user.phone = get_phone()
            user.address = faker.address()

            user.is_active = True

            session.add(user)

        session.commit()
