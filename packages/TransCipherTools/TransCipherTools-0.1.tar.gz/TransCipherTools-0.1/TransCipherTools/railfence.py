def encrypt(text, num_rails):
    enc = [""] * num_rails
    rail_pattern = [[" " for _ in text] for _ in range(num_rails)]
    row, direction = 0, 1

    for i, char in enumerate(text):
        enc[row] += char
        rail_pattern[row][i] = char
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    print("Rail Fence Pattern (Encryption):")
    for row in rail_pattern:
        print(''.join(row))

    encrypted_text = ''.join(enc)
    return encrypted_text

def decrypt(ciphertext, num_rails):
    rail_pattern = [[" " for _ in range(len(ciphertext))] for _ in range(num_rails)]
    row, direction = 0, 1

    for i in range(len(ciphertext)):
        rail_pattern[row][i] = "*"
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if rail_pattern[i][j] == "*":
                rail_pattern[i][j] = ciphertext[index]
                index += 1

    plaintext = ""
    row, direction = 0, 1

    for i in range(len(ciphertext)):
        plaintext += rail_pattern[row][i]
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    return plaintext


