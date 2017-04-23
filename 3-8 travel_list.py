travel_list = ['Gruzia', 'Japan', 'Holland', 'USA', 'Norway'] #сохраните страны в списке, не по алфавату
print(travel_list) #выведите как список
print(sorted(travel_list)) #вывод с функцией sorted
print(travel_list) #список все еще прежний
print(sorted(travel_list, reverse=True)) #вывод в обратном порядке
print(travel_list) #список все еще прежний
travel_list.reverse() #вывод с функцией reverse
print(travel_list) #список изменился
travel_list.reverse() #вывод с функцией reverse
print(travel_list) #список снова изменился и стал прежним
travel_list.sort()
print(travel_list)
travel_list.sort(reverse=True)
print(travel_list)