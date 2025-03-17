class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        print("New user being created")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_1.follow(user_2)
print(f"Name: {user_1.name} | Id: {user_1.id} | Followers: {user_1.followers} | Following: {user_1.following}")
print(f"Name: {user_2.name} | Id: {user_2.id} | Followers: {user_2.followers} | Following: {user_2.following}")