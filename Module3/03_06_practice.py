level = int(input("Введите количество уровней пирамиды: "))
summa = 0
count_level = 1
while count_level <= level:
    summa = summa + count_level ** 2
    count_level += 1
print(summa)

# "Пирамида"
# Задание
# Из остатков кирпичей Сергей сложил пирамиду.
# На вершине пирамиды лежит один кирпич, на втором сверху ряду два кирпича,
# на третьем - три, и т.д., в нижнем ряду пирамиды количество кирпичей равно
# количеству уровней пирамиды. После этого он написал на каждом кирпиче по
# числу, равному количеству кирпичей на этом уровне, т.е. на верхнем уровне 1,
# на втором уровне 2, и т.д.
# Определите сумму чисел написанных на кирпичах.
#
# Формат входных данных
# Дано одно целое положительное число — количество уровней в пирамиде
#
# Формат выходных данных
# выведите сумму чисел написанных на кирпичах
#
# Решение задачи