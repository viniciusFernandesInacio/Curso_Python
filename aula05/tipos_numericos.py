import random


num_i=10
num_f=5.2
num_c=1j

num_r=[
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
    ]

x=num_r

print("Valor: " + str(num_r[0]) + " Tipo: " + str(type(x)))