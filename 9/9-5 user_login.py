class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("User " + self.first_name.title() + " " + self.last_name.title() + "\n"+ str(self.age) + " years old" + "\ngender " + self.sex)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + " !")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('vadim', 'molchanov', 34, 'male')
# user1 = User('ivan', 'petrov', 28, 'male')
# user2 = User('klava', 'sidoroda', 32, 'female')
# user.describe_user()
# user1.greet_user()
# user2.describe_user()

print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)