import random
import time


hacer = input("Que quieres hacer?\n1: Contar caracteres\n2: Calcular\n3: Generar password aleatoria(Solo con los simbolos #@)\n4: Contar palabras\n5: Juego\n")
if hacer == '1':
    while True:
     palabra = input("Ingrese la frase/palabra para contar las letras: ")
     letras = len(palabra)
     print("Letras de su palabra/frase:", letras)

elif hacer == '2':
   while True:
    pregunta = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n')
    numero1 = int(input("Indique el primer numero: "))
    numero2 = int(input('Indique el segundo numero: '))
    if pregunta == '1':
     print("resultado:", numero1+numero2)
    elif pregunta == '2':
     print("resultado:", numero1-numero2)
    elif pregunta == '3':
     print("resultado:", numero1*numero2)
    elif pregunta == '4':
     print("resultado:", numero1/numero2)
    elif pregunta == '5':
     print("resultado:", numero1**numero2)
    else:
        print("Y si aprendes a leer?")

elif hacer == '3':
  while True:
    print("Tu password sera: ")

    chars = "abcdefghijklmnopqrstuvwxyz1234567890@#"

    password = ""
    for x in range(16):
        password += random.choice(chars)
    
    print(password)

    input("Presione enter para crear otra...")

elif hacer == '4':
  while True:
    frase = input("Ingrese una frase: ")

    palabras = frase.split()

    cantidad_palabras = len(palabras)

    print(f"La frase tiene {cantidad_palabras} palabra(s).")

elif hacer == '5':
  hora = int(input("Que hora es(poner solo los primeros dos digitos):"))
  numero1 = int(input("Ponga aqui 1 numero:"))
  numero2 = int(input("Ponga aqui 1 numero:"))
  pregunta = input("Si la suma de esos 2 numeros es igual a los 2 primero digitos de tu hora ganas, si no pierdes. Aceptas?\n")
  pregunta.lower()
  if pregunta == 'no':
    exit()
  elif pregunta == 'si':
    if numero1+numero2 == hora:
      print("Ganaste! Ganaras algo MUY especial...")
      time.sleep(0.5)
      print("Espera...")
      time.sleep(0.5)
      print("Espera...")
      time.sleep(0.5)
      print("Espera...")
      time.sleep(1)
      print(" / \__")
      print("(    @\___")
      print(" /         O")
      print("/   (_____/")
      print("Felicidades ahora...")
      time.sleep(0.5)
      input("Presiona enter para cerrar")
    elif numero1+numero2 != hora:
      print("Perdistes")
      time.sleep(0.5)
      exit()


