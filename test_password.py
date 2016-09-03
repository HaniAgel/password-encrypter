from hashlib import sha512

INPUT_FILE = "password.txt"

def get_password(filename):
    password, salt = open(filename, "r").read().split()
    return (password, salt)

def test_password(password, hashed_password, salt):
    return hashed_password = sha512(password.encode() + salt.encode())

def main():
    password = input("Enter password: ")
    hashed_password, salt = get_password(INPUT_FILE)

if __name__ == "__main__":
    main()
