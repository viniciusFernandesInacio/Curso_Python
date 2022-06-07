from re import X

#O laço FOR do python funciona com o FOR IT de outras linguagens.
carros=['HRV','Golf','Argo','Focus']

for x in carros:
    if(x=='Golf'):
        print('VW')
    if(x=='Focus'):
        break    
    print(x) 
print('Fim do programa.')       