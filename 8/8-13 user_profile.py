def buid_profile(first, last, **user_info):
    """"Строит словарь с информацией о пользователе."""
    profile= {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = buid_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)