# vrinda goel

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def encode(password):
    encode_pass = ''
    for i in password:
        number = str(int(i) + 3)
        encode_pass += number
    return encode_pass


def decode(password):
    decoded_pass = ''
    for i in password:
        decoded_num = str(int(i) - 3)
        decoded_pass += decoded_num
    return decoded_pass


def main():
    while True:
        menu()
        selection = int(input("Please enter an option: "))
        password = input("Please enter your password to encode: ")

        if selection == 1:
            print("Your password has been encoded and stored!")
        elif selection == 2:
            encoded_password = encode(password)
            decoded_password = decode(password)
            print(f"The encoded password is {encoded_password} and the original password is {decoded_password}.")
        elif selection == 3:
            exit()
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
