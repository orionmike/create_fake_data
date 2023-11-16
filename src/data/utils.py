
import random
import string
from slugify import slugify


def get_slug(line_str: str) -> str:
    result = line_str.replace('й', 'j')
    result = slugify(result)
    result = result.replace('ia', 'ya')
    return result


def get_random_string(start: int, finish: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(start, finish)))


def get_random_number(count_digit: int) -> str:
    return ''.join(random.choice(string.digits) for _ in range(count_digit))
