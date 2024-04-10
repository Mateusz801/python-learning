class User:
    # Constructor specifies what should be when objet is created
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Mateusz")
user_2 = User("002", "Zygmunt")
user_1.follow(user_2)

