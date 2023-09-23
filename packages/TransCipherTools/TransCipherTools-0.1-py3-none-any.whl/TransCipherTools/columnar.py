import math
def encrypt(msg, key):
    cipher = ""
    key_index = 0
    message_length = len(msg)
    message_list = list(msg)
    sorted_key = sorted(list(key))
    columns = len(key)
    rows = int(math.ceil(message_length / columns))
    padding_length = (rows * columns) - message_length
    message_list.extend('_' * padding_length)
    matrix = [message_list[i: i + columns] for i in range(0, len(message_list), columns)]

    for _ in range(columns):
        current_key_index = key.index(sorted_key[key_index])
        cipher += ''.join([row[current_key_index] for row in matrix])
        key_index += 1
    return cipher

def decrypt(cipher, key):
    decrypted_msg = ""
    key_index = 0
    cipher_length = len(cipher)
    cipher_list = list(cipher)
    columns = len(key)
    rows = int(math.ceil(cipher_length / columns))
    sorted_key = sorted(list(key))
    decrypted_matrix = []
    
    for _ in range(rows):
        decrypted_matrix += [[None] * columns]

    for _ in range(columns):
        current_key_index = key.index(sorted_key[key_index])
        for j in range(rows):
            decrypted_matrix[j][current_key_index] = cipher_list[j + key_index * rows]
        key_index += 1

    try:
        decrypted_msg = ''.join(sum(decrypted_matrix, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    padding_count = decrypted_msg.count('_')

    if padding_count > 0:
        return decrypted_msg[: -padding_count]

    return decrypted_msg
