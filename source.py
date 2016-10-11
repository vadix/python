#!/usr/local/bin/python
# coding: utf-8

from datetime import datetime, date, time

today_date = date.today()
print("сегодня")
print(today_date) #не сообразил как сделать на одной строке(
print()
deadline_date = date(2016, 12, 31) #вроде можно получать дату вводом пользователя, но сходу не сработало

print("осталось")
days_left = datetime.toordinal(deadline_date) - datetime.toordinal(today_date)

print(days_left)

current_weight = input()
goal_weight = 90.0






weight_left = current_weight - goal_weight
weight_loose_per_day = weight_left / days_left
round_weight = round(weight_loose_per_day,2)
print(round_weight)