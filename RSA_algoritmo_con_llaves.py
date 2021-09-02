


""""
funcion para encontrar el primo relativo
"""

numero_evaluar = int (input ("introduzca el valor de z:"))
valor_de_p = int(input("introduzca el valor de p"))
valor_de_q = int(input("introduzca el valor de p"))
contador = 0
while contador < numero_evaluar :
    numeros_contenidos =0
    while numeros_contenidos < numero_evaluar:
        es_primo_relativo = (numeros_contenidos * contador) % numero_evaluar
        if es_primo_relativo == 1 :
            print( "mod (", contador,"*" ,numeros_contenidos,"," ,numero_evaluar, ") =",es_primo_relativo,"es numero primo relavivo de", numero_evaluar)
        numeros_contenidos = numeros_contenidos +1
    contador = contador +1
    
    
   
   
