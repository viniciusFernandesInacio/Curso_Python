x=1 #int
x="python" #str
x=15.6 #float
x=True #boll
n1=5;n2=2;x=complex(n1, n2)
x=["carro","barco","aviao",1,58.3,True] #list / array
x=("carro","barco","aviao",1,58.8,False) #tupla
x=range(0,100,1) #list
x={ #dict
    "canal":"Curso",
    "chave":"Pythin",
    "nome":"Bruno"
}
x={5,7,4,5,7,4,8} #set / não repete os valores.
x=frozenset({5,7,4,5,7,4,8}) #set / frozenset bloqueia o set impedindo que sejam usados quaisquer metodos.

print("Valor da variavel: "+str(x))
print("Tipo da variavel: "+str(type(x)))