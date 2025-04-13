import random
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_otp():
    capitals = random.choices(string.ascii_uppercase, k=2)
    specials = random.choices("!@#$%^&*", k=2)
    digits =random.choices(string.digits, k=2)

    otp_list = capitals + specials + digits
    random.shuffle(otp_list)
    otp = ''.join(otp_list)
    return otp


def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.public_key().export_key()
    return private_key, public_key


def encrypt_otp(otp, public_key_pem):
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    encrypt_otp = cipher.encrypt(otp.encode())
    return base64.b64encode(encrypt_otp).decode()


def decrypt_otp(encrypted_otp_b64, private_key_pem):
    encrypted_otp = base64.b64decode(encrypted_otp_b64)
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_otp = cipher.decrypt(encrypted_otp)
    return decrypted_otp.decode()


otp = generate_otp()
print(f"OTP: {otp}\n")

private_key, public_key = generate_rsa_keys()
encrypt_otp = encrypt_otp(otp, public_key)
print(f"Encrypted OTP: {encrypt_otp}\n")

decrypted_otp = decrypt_otp(encrypt_otp, private_key)
print(f"Decrypte OTP: {decrypted_otp}")
