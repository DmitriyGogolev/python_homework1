"""  5. Пройденное расстояние. Допустим, что несчастные случаи или задержки отсутствуют,
тогда расстояние, проходимое автомобилем по автостраде, можно вычислить на основе
формулы:
расстояние= скорость х время.
Автомобиль движется со скоростью 70 км/ч. Напишите программу, которая показывает:
• расстояние, которое автомобиль пройдет за 6 часов;
• расстояние, которое автомобиль пройдет за 1 О часов;
• расстояние, которое автомобиль пройдет за 15 часо  """

speed = 70
time, time2, time3 = 6, 10, 15
path_length, path_length2, path_length3 = speed * 6, speed * 10, speed * 15
print("Расстояние за 6ч:", path_length, 'км', '\n', "Расстояние за 10ч:", path_length2, 'км', '\n', "Расстояние за 15ч:", path_length3,'км')