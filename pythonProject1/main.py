import summa

print("Добрый вечер!")

a='programs'
print(len(a))

# суммы и разница
first, second = 8, 13
summ = first + second
diff = first - second
print(summ, diff)


#логическа
print(bool(4+6 and 4-6))

#Среде-арифметическое
first,second,third = 11, 9, 7
mean = (first+second+third)/3
print(mean)

# Простые строчки
first_string,second_string='Вторник', 'Понедельник'
print(second_string +', '+ first_string)

a, b, c = 4, 8, 6
f = (a * b) + (a * c)
print(f ** 3 // 2)
