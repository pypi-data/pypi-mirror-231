import random
import string


def password_generator(
    length=8, characters=string.ascii_letters + string.digits + string.punctuation
):
    """
    Membuat pssword secara acak

    ```python
    print(password_generator())
    ```
    """
    # if characters is None:
    #     characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv

    print(password_generator(iargv[1] or 8))
