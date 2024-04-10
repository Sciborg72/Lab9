
def encode(password):
    encoded_password = ''
    for char in password:
        if char.isdigit():
            encoded_password += str((int(char) + 3) % 10)
    return encoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print('')
        choice = (input("Please enter an option: "))
        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Encoded password:", encoded_password)
        elif choice == '2':
            encoded_password = input("Please enter your password to decode: ")
            original_password = decode(encoded_password)
            print("Decoded password:", original_password)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()


