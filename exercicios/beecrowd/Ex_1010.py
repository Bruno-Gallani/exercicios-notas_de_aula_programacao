'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

codigo_1, numero_1, valor_1 = input().split()
codigo_1, numero_1, valor_1 = int(codigo_1), int(numero_1), float(valor_1)

codigo_2, numero_2, valor_2 = input().split()
codigo_2, numero_2, valor_2 = int(codigo_2), int(numero_2), float(valor_2)

valor_total = (valor_1 * numero_1) + (valor_2 * numero_2)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
