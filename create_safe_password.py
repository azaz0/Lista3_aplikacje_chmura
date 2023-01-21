import random
import string


def generate_password():
    # cyfry
    digits = string.digits
    # znaki specjalne
    special_characters = string.punctuation
    # długość hasła od 8 znaków w zwyż
    # dla przykładu ustawione na 24 znaki maks.
    set_password_length = random.randint(8, 24)
    # wielkie i małe litery z tablicy ASCII
    ascii_letters = string.ascii_letters

    # 'lista'-string zawierający wszystkie elementy
    expected_characters = ascii_letters + digits + special_characters

    # losowe wybieranie znaków z listy expected_characters
    password = "".join(
        random.choice(expected_characters) for i in range(set_password_length))

    return password


# Wykorzystanie list comprehension
print("Generated passwords (test for 1000 password): \n", [generate_password() for i in range(1000)])
