class User:
    def __init__(self, name, username, followers=0, posts=0):
        self.name = name 
        self.username = username
        self._followers = followers
        self.posts = posts

    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, followers):
        self._followers = followers

    def describe_user(self):
        print(f"{self.username} posted {self.posts} posts and has {self._followers} followers")
    
    def greet_user(self):
        print(f"Hi! {self.name}")


user1 = User("AbdulSalam", "nova", 5, 3)
user1.describe_user()

print(user1.followers)

user1.followers = 43

user1.describe_user()

