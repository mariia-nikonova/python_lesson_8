file = open('Исходный файл.txt', 'r', encoding = 'utf-8')
#with open('Исходный файл.txt', 'r', encoding = 'utf-8') as file:
str = input("Введите номер строки: ")
s = int(str)

def copy (f, n):
    data = f.readlines()
    r=data[n]
    f.close() 
    print(r)
    return (r)

copy(file,s)