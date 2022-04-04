import random
string = 'La casa solitaria de la montaña'
string = string.split()
final = ''


def main(palabra):
    count = 0
    count2 = 0
    num = 0
    chose = 0

    a = {'0': ['M', 'U', 'R', 'C', 'I', 'E', 'L', 'A', 'G', 'O'],
         '1': ['H', 'I', 'P', 'O', 'T', 'E', 'N', 'U', 'S', 'A'],
         '2': ['E', 'S', 'C', 'U', 'P', 'I', 'T', 'A', 'J', 'O'],
         '3': ['S', 'U', 'D', 'O', 'R', 'I', 'E', 'N', 'T', 'A']}
    
    for i in a.items():
        count = 0

        for letra in palabra:
            count += i[1].count(letra)
        if count > count2:
            count2 = count
            chose = num
        if count == count2:
            if random.choice([True, False]):
                chose = num
        num += 1
    crip = str(chose)
    for i in palabra:
        try:
          c = a[str(chose)].index(i)
        except:
            c = i
        crip += str(c)
    print(crip)
    return crip


for palabra in string:
    final += main(palabra.upper())
    final += ' '
print(final)