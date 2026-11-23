#1
a = input("Введи значение: ")
print("Значение:", a, "Тип данных:", type(a))
num = int(a)
print("Значение:", num, "Тип данных:", type(num))
st = str(num)
print("Значение:", st, "Тип данных:", type(st))
#2
b = int(input("число: "))
print(-abs(b))
#3
cap = int(input("Вместимость для пассажиров: "))
on = int(input("Сколько уже пассажиров: "))
wait = int(input("Ожидающих посадку: "))

free = cap - on
if wait > free:
    print("пассажиров осталось: ", wait - free)
else:
    print("пассажиров осталось: ", 0)
#4
print(f"Привет, {input("имя: ")}")
#5
print(int(input("Введите число 1: ")) * int(input("Введите число 2: ")))


