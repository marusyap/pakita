# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу: (выработка в
# часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
# значений необходимо запускать скрипт с параметрами.


from sys import argv
script_name, time, stavka, premiya = argv
time = int(time)
stavka = float(stavka)
premiya = int(premiya)

zp=time*stavka+premiya
print(f'Заработная плата сотрудника  {zp}')