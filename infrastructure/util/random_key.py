import random

def generate_random_key_only_hex(length: int) -> str:
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    return "".join(random.choice(letters) for _ in range(length))

def generate_random_key_only_int(length: int) -> str:
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return "".join(random.choice(letters) for _ in range(length))

def generate_outing_uuid() -> str:
    return "outing-" + generate_random_key_only_int(12)

def generate_confirm_code() -> str:
    return "confirm-" + generate_random_key_only_int(12)