# Поработайте с переменными, создайте несколько, выведите на экран.\
# Запросите у пользователя некоторые числа и строки и
# сохраните в переменные, затем выведите на экран.

a = 7
b = 8
print('Данные ',a,b)

name = input('Как Вас зовут? ')
age = int(input('Сколько Вам лет? '))
country = input('В какой стране вы живете? ')
year = int(input('В каком году вы родились? '))
print(f'Вас зовут {name}. Вам {age} лет. Вы родились в стране {country} в {year} году' )


# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах '))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - hour * 3600 - minute * 60
print(f'Время в формате чч:мм:сс {hour}:{minute}:{second}')


# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите однозначное число '))
summa = 3 * number + 2 * (number * 10) + number * 100
print(f'Сумма n+nn+nnn = {summa}')


# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.


number = int(input('Введите целое число '))
k = 0
max = number % 10
while number > 0:
    num = number % 10
    if num > max:
        max = num
    k += 1
    number=number // 10
print(f'Максимальная цифра в числе {max}')


# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.


plus = float(input('Введите сумму выручки фирмы '))
minus = float(input('Введите издержки фирмы '))
if plus > minus:
    print(f'Фирма прибыльная с рентабельностью {plus / minus}')
    num = int(input('Введите количество сотрудников'))
    print(f'Прибыль на одного сотрудника {plus / num}')
elif plus == minus:
    print(f'Фирма работает в ноль')
else:
    print(f'Фирма убыточная')


# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

a = float(input('Сколько километров пробежал спортсмен в первый день? '))
b = float(input('Сколько километров спортсмен хочет бегать? '))
k = 0
while b > a:
    a = a + 0.1 * a
    k += 1
print(f'Через {k} дней спортсмен начнет бегать не менеe {b} километров')

