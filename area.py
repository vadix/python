# coding=utf-8
import math

figure = input()

if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    print(math.sqrt(p*((p - a)*(p - b)*(p - c))))


if figure == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)

if figure == "круг":
    a = float(input())
    print(3.14 * a * a)