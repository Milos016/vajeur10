a = 1
b = 3

def ime(i):
    input('Ime: '+i)
    return ('Welcome' +i)

while a > 0:   # ova zanka se bo neskončno izvajala ker je a vedno več kot 0
    b += a
    a += a     
    print(b)

