import string
import random

def idCreator(password_len = 5, caracteres = string.ascii_letters):
    return("".join(random.choice(caracteres) for _ in range(password_len)))

