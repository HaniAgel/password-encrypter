from hashlib import sha512

INPUT_FILE = "password.txt"

def get_password(filename):
    password, salt = open(filename, "r").read().split()
    return (password, salt)

def main():
    password = input("Enter password: ")
    hashed_password, salt = get_password(INPUT_FILE)

if __name__ == "__main__":
    main()
