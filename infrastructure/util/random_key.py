import random
import string


def random_key_generate(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
