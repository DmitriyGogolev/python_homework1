"""1. Персональные данные. Напишите программу, которая выводит приведенную ниже информацию:
• ваше имя;
• ваш адрес проживания, с городом, областью и почтовым индексом;
• ваш номер телефона;
• вашу специализацию в учебном заведении."""


name = str(input("введите ваше имя: "))
location = str(input("введите ваш ваш адрес проживания, с городом, областью и почтовым индексом: "))
tele_number = str(input("введите ваш номер телефона: "))
profession = str(input("введите вашу специализацию в учебном заведении: "))

print("Ваши данные: ", name, location, tele_number, profession, sep='\n')