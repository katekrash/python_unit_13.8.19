tickets_quantity = int(input("Количество билетов:"))  # запрашиваем количество билетов на мероприятие
count = 0  # значение для счета
cost = 0  # стоимость билетов
if tickets_quantity > 1:
    for count in range(tickets_quantity):  # в этом цикле собираем  информацию для расчета стоимости 
        count += 1
        age = int(input(f"Введите возраст {count}:"))
        if age < 18:
            pass
        elif age >= 18 and age < 25:
            cost += 990
        else:
            cost += 1390

elif tickets_quantity == 0:
    pass

else:
    age = int(input("Введите возраст:"))
    if age < 18:
        pass
    elif age >= 18 and age < 25:
        cost += 990
    else:
        cost += 1390

if count >= 3:
    cost = (cost - (cost * 0.1))
else:
    pass
print(f"Полная стоимость {cost} рублей")  # выводим полную стоимость