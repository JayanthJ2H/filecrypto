import hashlib
import argparse
from encrypt import encryption
from decrypt import decryption 

def check(file):
    try:
        with open(file, 'rb') as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            return hash
    except FileNotFoundError:
        print(f"File not found: '{file}' does not exist")
        exit(1)
    except Exception as e:
        print(f"Wrong input file: Check your files")
        exit(1)

try:
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using a key image.")
    parser.add_argument("-e", "--encrypt", help="Encrypt a file", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Decrypt a file", action="store_true")
    parser.add_argument("-f", "--file", help="Path to the file", required=True)
    parser.add_argument("-k", "--key", help="Path to the key image", required=True)

    args = parser.parse_args()

    image = args.key
    key = check(image)
    seperate = len(key) // 2
    first_half = key[:seperate]
    second_half = key[seperate:]

    if args.encrypt:
        encryption(args.file, first_half, second_half)
    elif args.decrypt:
        decryption(args.file, first_half, second_half)
    else:
        print("Please specify either --encrypt or --decrypt")

except argparse.ArgumentError:
    print("Sample usage: imgcrypt.py -e -f flag.txt -k image.jpg")
