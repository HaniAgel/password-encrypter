from hashlib import sha512
from random import choice
from string import ascii_letters

SALT_LENGTH = 32
OUTPUT_FILE = "password.txt"

def encrypt(password):
    salt = "".join((choice(ascii_letters) for letter in range(SALT_LENGTH)))
    hashed_password = sha512(password.encode() + salt.encode()).hexdigest()
    return (hashed_password, salt)

def main():
    password = input("Enter password: ")
    hashed_password, salt = encrypt(password)
    output = open(OUTPUT_FILE, "w")
    output.write("%s %s" %(hashed_password, salt))
    output.close()

if __name__ == "__main__":
	main()
