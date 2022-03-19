curso="Curso de Python"


#print(curso[9:15])
#print(curso.strip())  #remove os espaços da string
#print(curso.lower().strip())   #converte a string para letras minusculas
#print(curso.upper())   #converte a string para letras maiusculas 
#print(curso.replace("Python","SQL"))  #troca objetos da array
a=curso.split(" ")    #remove tudo que estiver entre "" e divide o restante em uma array
print(a[0])
print("Tamanho: " + str(len(curso)))