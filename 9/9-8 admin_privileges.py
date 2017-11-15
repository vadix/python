class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("User " + self.first_name.title() + " " + self.last_name.title() + "\n"+ str(self.age) + " years old" + "\ngender " + self.sex)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + " !")

class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        print(admin.privileges)

admin = Admin('bad', 'motherfucker', 32, 'male')


user = User('vadim', 'molchanov', 34, 'male')
user1 = User('ivan', 'petrov', 28, 'male')
user2 = User('klava', 'sidoroda', 32, 'female')
user.describe_user()
user1.greet_user()
user2.describe_user()
admin.show_privileges()
