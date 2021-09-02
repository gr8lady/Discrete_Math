


""""
funcion de encriptacion usando RSA
"""


valor_de_p = int(input("introduzca el valor de p: "))
valor_de_q = int(input("introduzca el valor de q: "))
llave_publica = valor_de_p * valor_de_q
print("la llave publica es: ", valor_de_p, "*", valor_de_q, "= ", llave_publica)
numero_evaluar = (valor_de_p -1) *(valor_de_q -1)
print("numero a evaluar es (p-1)*(q-1): ", numero_evaluar)
contador = 0
while contador < numero_evaluar :
    numeros_contenidos =0
    while numeros_contenidos < numero_evaluar:
        es_primo_relativo = (numeros_contenidos * contador) % numero_evaluar
        if es_primo_relativo == 1 :
            print( "mod (", contador,"*" ,numeros_contenidos,"," ,numero_evaluar, ") =",es_primo_relativo,"es numero primo relavivo de", numero_evaluar)
        numeros_contenidos = numeros_contenidos +1
    contador = contador +1
valor_de_e = int(input("introduzca el valor de que se aun primo relativo e: "))
residuo_llave_privada = numero_evaluar % valor_de_e
print("residuo de la llave privada = ", residuo_llave_privada)
cociente_llave_privada = round(numero_evaluar / valor_de_e)
print("cociente de la llave privada = ", cociente_llave_privada)
es_primo_relativo =0
contador =0
while contador < numero_evaluar :
    numeros_contenidos =0
    while numeros_contenidos < numero_evaluar:
        es_primo_relativo = (numeros_contenidos * contador) % numero_evaluar
        if es_primo_relativo == 1 and  contador == valor_de_e:
            print( "mod (", contador,"*" ,numeros_contenidos,"," ,numero_evaluar, ") =",es_primo_relativo,"la llave privada es: ", numeros_contenidos)
            llave_privada= numeros_contenidos
        numeros_contenidos = numeros_contenidos +1
    contador = contador +1
print("la llave privada es: ", llave_privada)
print("la llave publica pq es: ", llave_publica)
print("la llave publica e es: ", valor_de_e)

   
