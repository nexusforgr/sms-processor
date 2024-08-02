from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from base64 import urlsafe_b64encode, urlsafe_b64decode


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=100000)


def encrypt_message(message: str, password: str) -> str:
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_message = cipher.encrypt(message.encode())
    return urlsafe_b64encode(salt + iv + encrypted_message).decode()


def decrypt_message(encrypted_message: str, password: str) -> str:
    encrypted_message_bytes = urlsafe_b64decode(encrypted_message)
    salt = encrypted_message_bytes[:16]
    iv = encrypted_message_bytes[16:32]
    encrypted_text = encrypted_message_bytes[32:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_message = cipher.decrypt(encrypted_text)
    return decrypted_message.decode()