import hashlib
import random
import string


def hash_str(word,salt = ''):
    return hashlib.sha256((salt + word).encode()).hexdigest()

def get_random_salt(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

if __name__ == "__main__":
    print(hash_str('This is a test'))

