
import random
import string

from faker import Faker
from slugify import slugify

from database.database import session_maker
from database.models import User

GENDER_TUPLE = ('m', 'f')


def get_name(fake: Faker, gender: str) -> tuple:
    if gender == 'm':
        return fake.first_name_male(), fake.last_name_male()
    if gender == 'f':
        return fake.first_name_female(), fake.last_name_female()


def get_random_str(start: int, finish: int) -> str:

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(start, finish)))


def get_phone() -> str:
    return '+79' + ''.join(random.choice(string.digits) for _ in range(9))


def get_slug(line_str: str) -> str:

    result = line_str.replace('й', 'j')
    result = slugify(result)
    result = result.replace('ia', 'ya')
    return result


def get_email(person: tuple) -> str:
    return f'{get_slug(person[0])}_{get_slug(person[1])}@{get_random_str(3,5)}.{get_random_str(2,3)}'


def create_users(user_count: int, delete=None) -> None:

    with session_maker() as session:

        if delete:
            session.query(User).delete()
            session.commit()

        faker = Faker(['ru_RU'])

        for _ in range(user_count):

            user = User()

            person = get_name(faker, random.choice(GENDER_TUPLE))

            user.first_name, user.last_name = person

            user.email = get_email(person)
            user.phone = get_phone()
            user.address = faker.address()

            user.is_active = True

            session.add(user)

        session.commit()
