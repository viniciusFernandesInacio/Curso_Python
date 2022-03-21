carros=["golf","opala","fusca","bmw"]
carros.append("polo")
carros.append("fusion")
carros.append("kombi")
carros2=["147","marajo","caravan"]

carros3=carros+carros2
carros.remove("fusion")  #.remove deleta itens na array
del carros[2]            #del deleta itens na array
carros2=list(carros)     #list() copia array

print(str(len(carros)) + " carros na lista")