from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import urlsafe_b64encode, urlsafe_b64decode

def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def aes_256_encrypt(key, iv, plaintext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    padded_data = pad(plaintext.encode('utf-8'))
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return urlsafe_b64encode(ciphertext).decode('utf-8')

def aes_256_decrypt(key, iv, ciphertext):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
        decryptor = cipher.decryptor()

        decoded_ciphertext = urlsafe_b64decode(ciphertext.encode('utf-8'))
        padded_data = decryptor.update(decoded_ciphertext) + decryptor.finalize()
        return unpad(padded_data).decode('utf-8')


