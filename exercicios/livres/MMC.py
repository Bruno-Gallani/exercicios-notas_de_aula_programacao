'''
Calcule o mmc entre x e y. Não esquecer de importar a biblioteca: import math
O seu programa deve
1) Ler x (inteiro)
2) Ler y (inteiro)
3) Imprimir o mmc entre x e y
Note que o mmc deve ser um número inteiro. Imprima sua resposta
usando este comando: print("%d" %resposta)
'''

import math
# não foi utilizada

x = int(input())
y = int(input())

def mmc(x, y):
  divisor = 2
  # valor inicial de divisor
  mmc = 1
  # o número 1 é o elemento neutro multiplicativo,
  # logo, definimos ele como o valor inicial
  while x != 1 or y != 1:
    if x % divisor == 0 and y % divisor == 0:
      y /= divisor
      x /= divisor
      mmc *= divisor
      continue
    elif x % divisor == 0:
      x /= divisor
      mmc *= divisor
      continue
    elif y % divisor == 0:
      y /= divisor
      mmc *= divisor
      continue
    else:
      divisor += 1
  return mmc

resposta = mmc(x, y)

print("%d" %resposta)
