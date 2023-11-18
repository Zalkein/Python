#project1 Calculator

while True:
 pregunta = input("Que quieres hacer?(indicar el numero)\n1 sumar\n2 restar\n3 dividir\n4 multiplicar\n5 Potencia de 2 operadores\n")

 if pregunta == '1':
    numero1 = int(input("Indique el numero: " ))
    numero2 = int(input("Indique el numero2: " ))
    print("El resultado de su suma es:", numero1+numero2)

 elif pregunta == '2':
    numero1 = int(input("Indique el numero: " ))
    numero2 = int(input("Indique el numero2: " ))
    print("El resultado de su resta es: ", numero1-numero2)

 elif pregunta == '3':
    numero1 = int(input("Indique el numero: " ))
    numero2 = int(input("Indique el numero2: " ))
    print("El resultado de su division es:", numero1/numero2)

 elif pregunta == '4':
    numero1 = int(input("Indique el numero: " ))
    numero2 = int(input("Indique el numero2: " ))
    print("El resultado de su multiplicacion es: ", numero1*numero2)

 elif pregunta == '5':
    numero1 = int(input("Indique el numero: " ))
    numero2 = int(input("Indique el numero2: " ))
    print("El resultado de su potencia es:", numero1**numero2)

 else:
   print("No has aprendido a leer o como va la cosa?")
