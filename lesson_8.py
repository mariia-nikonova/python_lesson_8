file1 = open('Исходный файл.txt', 'r', encoding = 'utf-8')
str = input("Введите номер строки: ")
s = int(str)

def copy (f, n):
    data = f.readlines()
    r=data[n]
    f.close() 
    return (r)
row = copy(file1,s)

file2 = open('Новый файл.txt', 'a', encoding = 'utf-8')
file2.write(row)
file2.close()
file2 = open('Новый файл.txt', 'r', encoding = 'utf-8')
print(*file2)
file2.close()
