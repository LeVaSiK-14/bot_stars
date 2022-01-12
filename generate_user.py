import string
import random

from config import max_users


class GenerateUser:
    def __init__(self, amount_users, max_users):
        self.amount_users = amount_users
        self.max_users = max_users

    def generate_user(self):
        users = []
        if self.amount_users > self.max_users:
            raise ValueError(
                {"Error": f"You can generate max {self.max_users} users!"})
        else:
            for user in range(self.amount_users):
                user = {}
                username = "".join(
                    [random.choice(string.ascii_letters) for _ in range(10)])
                password = "".join(
                    [random.choice(string.ascii_letters) for _ in range(10)])
                user["username"] = username
                user["password"] = password
                users.append(user)
            return users


generate_users = GenerateUser(3, max_users).generate_user()
