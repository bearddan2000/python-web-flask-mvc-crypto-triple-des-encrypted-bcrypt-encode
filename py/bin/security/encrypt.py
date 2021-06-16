from des import DesKey

class PasswordCipher:

    def encrypt(self, raw):
        # DES 8 bit
        key = DesKey(b"A quick brown fox jumped")
        # password should be length div by 8, 16, 24
        raw = bytes(raw, encoding='utf-8')
        return key.encrypt(raw, padding=True)
