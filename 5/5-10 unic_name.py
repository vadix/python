current_users =['admin', 'vadix', 'gleb', 'timo', 'nastya']
new_users = ['tanya', 'Admin', 'Stas', 'Vadix', 'lena']

for current_user in current_users:
    if current_user.title() in new_users:
        print(current_user + " take new name")
    else:
        print(current_user + " ok")