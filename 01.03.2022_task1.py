
# Task1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секудах:
# до минуты: <s> сек;
# до часа: <m> мин <S> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях:<d> дн <h> час <m> мин <s> сек;

# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration 4153
# 1 час 9 мин 13 сек
# duration 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input('Введите время в секундах: '))
days = duration // (60 * 60 * 24)
hours = (duration-days * (60 * 60 * 24)) // (60 * 60)
minutes = (duration-days * (60 * 60 * 24) - hours * (60 * 60)) // 60
secunds = duration - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print(days, 'дн', hours, 'час', minutes, 'мин', secunds, 'сек')








