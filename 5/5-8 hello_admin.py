users_list = ['vadim', 'igor', 'admin', 'vitaly', 'leonid']

for user in users_list:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + user.title() + ', thank you for logging in again')