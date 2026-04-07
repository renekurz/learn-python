class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

    def print_user(self):
        print(f"id: {self.id}\nusername: {self.name}\nfollower: {self.follower}\nfollowing: {self.following}")

user_1 = User("001", "max")
user_2 = User("002", "jack")

user_1.follow(user_2)

user_1.print_user()
user_2.print_user()
