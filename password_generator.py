import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length for the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
