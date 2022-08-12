"""Напишите инструкцию Python, которая вычитает переменную down _payment (предоплата) из
переменной total (итоговая сумма) и присваивает результат переменной due"""
down_payment = int(input("Введите предоплату:"))
total = int(input("Введите итоговую сумму:"))
due = total - down_payment
print(due)