import random
import string

length = 20

def random_key_generate():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
