import hashlib
import random


class User:
    def __init__(self, username: str, salt: bytes, password_hash: bytes):
        self.username = username
        self.salt = salt
        self.password_hash = password_hash

    @staticmethod
    def create_user(username: str, password: str):
        salt = random.randbytes(32)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, 100000
        )
        return User(username, salt, password_hash)

    def update_username(self, username: str):
        self.username = username

    def update_password(self, password: str):
        self.salt = random.randbytes(32)
        self.password_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), self.salt, 100000
        )

    def check_password(self, password: str) -> bool:
        return self.password_hash == hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), self.salt, 100000
        )


class UserPool:
    def __init__(self):
        self.users = []

    def add_user(self, username: str, password_hash: str):
        for user in self.users:
            if user.username == username:
                raise ValueError("User already exists")
        self.users.append(User.create_user(username, password_hash))

    def remove_user(self, username: str):
        user = self.get_user(username)
        if user is not None:
            self.users.remove(user)

    def get_user(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user
        return None
