from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    age: int


class UserSource:

    def __init__(self) -> None:
        self.users = {}

    def add(self, user: User):
        self.users[user.username] = user

    def load_by_username(self, username: str):
        return self.users.get(username)
