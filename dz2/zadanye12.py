#Задача 12: Петя и Катя – брат и сестра. Петя – студент,
#а Катя – школьница. Петя помогает Кате по математике.
#Он задумывает два натуральных числа X и Y (X,Y≤1000),
#а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P.
#Помогите Кате отгадать задуманные Петей числа.
sum = int(input("Введите сумму чисел: "))
mult = int(input("Введите произведение чисел: "))
for i in range(1,1000):
    for j in range(1,1000):
        if i + j == sum and i * j == mult:
            x = i
            y = j
print(f"Вы загадали числа {x} и {y}.")
            
    
    
