import re
import random 

def main():
    palabra = input("ingresa una palabra: ")
    palabra = palabra.lower()
    palabra = re.sub(" ","",palabra)
    palabra_reves = palabra[::-1]

    if palabra == palabra_reves:
        print("La palabra ingresada es palindromo")
    else:
        print("La palabra ingresada NO ES palindromo")

def mil():
    for numero in range(1000):
        print (f"{numero} pasada de for")

def ciclos_f ():
    for contador in range(100):
        if contador % 2 != 0:
            continue
        print(contador)

def es_primo():
    contador = 0
    primos = [1]
    cantidad = int(input("ingresa un numero: "))
    for numero in range(1,cantidad+1):
        for primo in primos:
            if numero % primo == 0:
                contador += 1
            
        if contador > 2:
            contador = 0
            continue
        else:
            primos.append(numero)
            contador = 0

    print(primos)


def juego():
    numero_R = random.randrange(1000)
    numero = int(input("ingresa un numero: "))
    while numero_R != numero:
        if numero_R > numero:
            print("piensa un numero mas grande")
        else:
            print("piensa un numero mas pequeño")
        numero = int(input("ingresa un numero: "))
    print("!GANASTE¡¡¡¡")


if __name__ == '__main__':
    juego()