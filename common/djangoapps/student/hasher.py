import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from django.conf import settings


class AESCipher(object):

    def __init__(self, key, iv=b'X\x04\xa76\xe9\x9e\x19Sx\xe3CE*/\xb1.'):
        """
        default use [settings.SECRET_KEY]
        if user want to use custom, just like this.
        eg. key = hashlib.sha256(settings.AES_KEY).digest()

        # iv = Random.new().read(AES.block_size)
        # use settings iv instead of random to produce same result
        """
        self.key = hashlib.sha256(key).digest()
        self.iv = iv

    def encrypt(self, raw):
        if raw is None:
            return raw

        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(self.iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        if enc is None:
            return enc

        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        bs = AES.block_size
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
