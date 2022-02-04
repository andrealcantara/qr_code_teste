import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

_KEY = "RfUjXnZr4u7x!A%D*G-KaPdSgVkYp3s5"

class AESCipher(object):

    def __init__(self):
        self.bs = AES.block_size
        self.key = hashlib.sha256(_KEY.encode()).digest()

    def encrypt(self, raw):
        raw = pad(raw.encode(), self.bs)
        iv = get_random_bytes(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:self.bs]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:]), self.bs).decode("UTF-8")

