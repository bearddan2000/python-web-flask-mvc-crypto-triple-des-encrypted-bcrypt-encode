from flask_bcrypt import Bcrypt
from security.encrypt import PasswordCipher

class Encode:
    pc = PasswordCipher()
    bcrypt = Bcrypt()

    def hash_password(self, password):
        password = self.pc.encrypt(password)
        return self.bcrypt.generate_password_hash(password)

    def verify(self, hash, password):
        return self.bcrypt.check_password_hash(hash, self.pc.encrypt(password)) #  True
