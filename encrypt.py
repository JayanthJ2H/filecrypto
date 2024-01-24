from algorithm import aes_256_encrypt
import binascii


def encryption(filename, encryption_key_hex, iv_hex):

    encryption_key = binascii.unhexlify(encryption_key_hex)
    iv = binascii.unhexlify(iv_hex)

    try:

        with open(filename, 'r') as file:
            plaintext_message = file.read()

        encrypted_message = aes_256_encrypt(encryption_key, iv, plaintext_message)

        with open("encrypted_message.txt", 'w') as file:
            file.write(encrypted_message)
        print("outputfile: encrypted_message.txt")
        print(f'Encrypted Message: {encrypted_message}')
    
    except FileNotFoundError:
        print(f"File not found: '{filename}' does not exist")
        exit(1)
    except Exception as e:
        print(f"Wrong input file: Check your files")
        exit(1)
    



