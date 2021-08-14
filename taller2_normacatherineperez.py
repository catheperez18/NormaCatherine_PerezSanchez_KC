# -*- coding: utf-8 -*-
"""taller2_normacatherineperez.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AW8UzZa7QewskiHl6O_LnA8xVK_tVYKK

#Taller 2 - Norma Catherine Perez Sanchez

###Numeros palíndromos:
####Escriba una función que reciba un numero entero (positivo) o un String y entregue como
####respuesta si la entrada es o no un palíndromo.
"""

igual, aux = 0, 0
texto = input("Ingrese el texto o número: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto es un palindromo")
else:
  print("El texto no es un palindromo")

"""###Numeros primos:
####Escriba una función que reciba como entrada un número y determine si es o no un numero primo. 
"""

def primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def solucion():
    num = int(input('Escribe el número: '))
    resultado = primo(num)

    if resultado is True:
        print('El número es primo')
    else:
        print('El número no es primo')

if __name__ == '__main__':
    solucion()

"""###Numeros primos 3:
####El primo de Mersenne es un numero primo de la forma 2 𝑝 − 1, una de las propiedades de los primos de Mersenne es que p debe ser también un número primo, escriba una función que imprima la cantidad de numeros que el usuario solicite, Ejemplo: si el usuario ingreso 3 los primeros primos de Mersenne deberían ser 3, 7 y 31. 
"""

import math
 
def primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return numero
 
def mamersenne(func):
    for i in range(2,numero+1):
        potencia=(math.pow(2,i))
        if (potencia-1) == numero:
            print('El número {} es Mersenne'.format(numero))
            break
    else:
        print('El número {} es primo, pero no Mersenne'.format(numero))
 
numero=int(input('Introduce un número: '))
mamersenne(primo(numero))

"""###Máximo común divisor:
####Escriba una función que reciba dos numeros y retorne el cálculo de su máximo común divisor. 
"""

num1 =int(input("Escriba el primer número: "))
num2 =int(input("Escriba el segundo número: "))

A = max(num1, num2)
B = min(num1, num2)

while B:
    mcd = B
    B = A % B
    A = mcd
mcm =  (num1 * num2) // mcd

print('El Maximo comun divisor de {0} y {1} es: {2}'.format(num1, num2, mcd))

"""###Numeros romanos:
####Escriba una función que reciba un numero y retorne como resultado el numero romano de dicho número. 
"""

import math 
Unidad= ["","I","II","III","IV","V","VI","VII","VIII","IX"]
Decena= ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
Centena= ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
N= int(input("Ingresar un número entero:"))
u= N % 10
d=int(math.floor(N/10))%10
c=int(math.floor(N/100))
if(N>=100):
print(Centena[c]+Decena[d]+Unidad[u])
else:
if(N>=10)
print(Decena[d]+Unidad[u])
else:
print(Unidad[u])