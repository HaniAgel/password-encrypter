from hashlib import sha512
from random import choice
from string import ascii_letters

SALT_LENGTH = 32

def encrypt(password):
    salt = "".join((choice(ascii_letters) for letter in range(SALT_LENGTH)))
    hashed_password = sha512(password.encode() + salt.encode()).hexdigest()
    return (hashed_password, salt)

def main():
    password = input("Enter password: ")

if __name__ == "__main__":
	main()
