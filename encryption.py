def encrypt_char(ch, shift1, shift2):

    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        if pos <= 12:  # a-m
            shift = shift1 * shift2
            new_pos = (pos + shift) % 26
        else:  # n-z
            shift = shift1 + shift2
            new_pos = (pos - shift) % 26
        return chr(new_pos + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        if pos <= 12:  # A-M
            new_pos = (pos - shift1) % 26
        else:  # N-Z
            new_pos = (pos + (shift2 ** 2)) % 26
        return chr(new_pos + ord('A'))

    else:
        return ch


def decrypt_char(ch, shift1, shift2):

    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        if pos <= 12:
            shift = shift1 * shift2
            new_pos = (pos - shift) % 26
        else:
            shift = shift1 + shift2
            new_pos = (pos + shift) % 26
        return chr(new_pos + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        if pos <= 12:
            new_pos = (pos + shift1) % 26
        else:
            new_pos = (pos - (shift2 ** 2)) % 26
        return chr(new_pos + ord('A'))

    else:
        return ch


def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as infile, open("encrypted_text.txt", "w") as outfile:
        for line in infile:
            encrypted_line = ""
            for ch in line:
                encrypted_line += encrypt_char(ch, shift1, shift2)
            outfile.write(encrypted_line)


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile, open("decrypted_text.txt", "w") as outfile:
        for line in infile:
            decrypted_line = ""
            for ch in line:
                decrypted_line += decrypt_char(ch, shift1, shift2)
            outfile.write(decrypted_line)


def verify_decryption():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        if f1.read() == f2.read():
            print("Decryption successful: Files match.")
        else:
            print("Decryption failed: Files do not match.")


shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypt_file(shift1, shift2)
decrypt_file(shift1, shift2)
verify_decryption()