# --- Блок вывода на экран
print("""Hi!
    I am program for your pocket
       for end of the shoping just input -1""")

valuta = "money"

# --- Блок ввода
# --- Инитиализация переменных
summa = 0
count = 0
buy = 0

summa = int(input("Input volume of cash for today purchased: "))

# --- Инициализируем переменную с начальной суммой денег
startSumma = summa

# --- Блок обработки
while (summa > 0 and buy != -1):
    print("Balance:", summa, valuta)
    buy = int(input("Input purchase value: "))

    if (buy > summa):
        print("-" * 40)
        print("Value of purchase can't be  more than your balance")
        print("-" * 40)
    elif (buy > 0):
        summa -= buy
        count += 1
        if (summa < 200 and summa > 0):
            print("Attention! Remains only", summa, valuta + "!", " Be carefull with your money")
        print("*" * 20)
# --- Финальный вывод
print("You spent:" , startSumma - summa, valuta)
print("You made ", count, "purchases.")

        
