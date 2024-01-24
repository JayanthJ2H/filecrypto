from algorithm import aes_256_decrypt
import binascii 

def decryption(filename, encryption_key_hex, iv_hex):
    try:
        encryption_key = binascii.unhexlify(encryption_key_hex)
        iv = binascii.unhexlify(iv_hex)

        with open(filename, 'r') as file:
            encrypted_message = file.read()

        decrypted_message = aes_256_decrypt(encryption_key, iv, encrypted_message)

        with open("decrypted_message.txt", 'w') as file:
            file.write(decrypted_message)
        print("outputfile: decrypted_message.txt")
        print(f'Decrypted Message: {decrypted_message}')
    
    except FileNotFoundError:
        print(f"File not found: '{filename}' not found")

    except Exception as e:
        print(f"Input file of keyfile is invalid")
