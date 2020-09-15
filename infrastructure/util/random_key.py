import random
import string


def generate_random_key(length: int) -> str:
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def generate_outing_uuid() -> str:
    return "outing-" + generate_random_key(12)
