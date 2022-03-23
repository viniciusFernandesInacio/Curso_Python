a=20
b=5
res=0
op="+"

if op=="+":  #se usa o == para comparação
    res=a+b

if op=="-":
    res=a-b

if op=="*":
    res=a*b

if op=="/":
    res=a/b

print(str(a) + op + str(b) + " = " + str(res))                