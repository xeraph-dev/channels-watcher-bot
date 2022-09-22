import json
import os
from pyrogram.types import User


class AppUser:
    id: int
    username: int

    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username

    def __iter__(self):
        yield from {
            "id": self.id,
            "username": self.username,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class Database:
    __FILE = "database.json"
    __users: dict[int, AppUser] = {}
    __invited_users: list[str] = []

    def __new__(cls):
        if not hasattr(cls, "instance"):
            mode = "r"
            if not os.path.exists(cls.__FILE):
                mode = "a"
            with open(cls.__FILE, mode) as file:
                content = file.read() or "{}"
                cls.__db = json.loads(content)

            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    @property
    def invited_users(self):
        return self.__invited_users

    @property
    def users(self):
        return self.__users.values()

    def user_exists(self, user: User):
        return self.is_user_acceted(user) or self.is_user_invited(user)

    def is_user_invited(self, user: User):
        return user.username in self.__invited_users

    def is_user_acceted(self, user: User):
        return user.id in self.__users

    def invite_user(self, username: str):
        if not username in self.__invited_users:
            self.__invited_users.append(username)
            self.save()

    def uninvite_user(self, username: str):
        if username in self.__invited_users:
            self.__invited_users.remove(username)
            self.save()

    def accept_invitation(self, user: User):
        if user.username in self.__invited_users:
            self.__invited_users.remove(user.username)
            self.__users[user.id] = AppUser(user)
        elif user.id in self.__users:
            self.__users[user.id].username = user.username

    def delete_user(self, id: int):
        if id in self.__users:
            self.__users.pop(id)
            self.save()

    def save(self):
        with open(self.__FILE, "w") as file:
            file.write(str(self))

    def __iter__(self):
        users = {}
        for user in self.__users.values():
            users[user.id] = dict(user)
        yield from {
            "users": users,
            "invited_users": self.__invited_users,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
