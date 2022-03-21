cidade="Curitiba"
dia=19
mes="Dezembro"
ano=2022
canal="CFB Cursos"
data="{}, {} de {} de {}\n \"{}\"" # \n é usado como quebra linha   # \ é usado para imprimir ""
                                                                    #\', \", \n, \r, \t, \b
#res=palavra.upper in texto.upper()
print(data.format(cidade,dia,mes,ano,canal))