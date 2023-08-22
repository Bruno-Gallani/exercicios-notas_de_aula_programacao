'''
Projeto desenvolvido durante a realização do curso.
'''

def computador_escolhe_jogada (n, m):
  jogada = n % (m + 1)
  if ((n - jogada) % (m + 1) == 0):
    jogada = jogada
  else:
    jogada = m
  return jogada

def usuario_escolhe_jogada (n, m):
  jogada = int(input("Quantas peças você vai tirar? "))
  while (jogada > m or jogada > n or jogada < 1):
    print("""Oops! Jogada inválida! Tente de novo.

""")
    jogada = int(input("Quantas peças você vai tirar? "))
  return jogada

def partida():
  opcao = input("""Bem-vindo ao jogo do NIM! Escolha:
  
1 - para jogar uma partida isolada
2 - para jogar um campeonato
""")
  
  if opcao == "1":
    print("""
Voce escolheu uma partida isolada!
""")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
      print("\nVocê começa!\n")
      jogador = "usuario"
    else:
      print("\nComputador começa!\n")
      jogador = "pc"

    while n > 0:
      if jogador == "usuario":
        jogada = usuario_escolhe_jogada(n, m)
        n = n - jogada
        print("Você tirou", jogada, "peças.")
        jogador = "pc"
      else:
        jogada = computador_escolhe_jogada(n, m)
        n = n - jogada
        print("O computador tirou", jogada, "peças.")
        jogador = "usuario"
      if n != 0:
        print("Agora restam", n, "peças no tabuleiro.\n")

    if jogador == "usuario":
      print("Fim do jogo! O computador ganhou!")
    else:
      print("Você ganhou!")

  elif opcao == "2":
    print("""
Voce escolheu um campeonato!
""")
    campeonato()

def campeonato():
  i = 1
  placarUsuario = placarPc = 0

  while i <= 3:
    print("**** Rodada %d ****\n" %i)
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
      print("\nVocê começa!\n")
      jogador = "usuario"
    else:
      print("\nComputador começa!\n")
      jogador = "pc"

    while n > 0:
      if jogador == "usuario":
        jogada = usuario_escolhe_jogada(n, m)
        n = n - jogada
        print("Você tirou", jogada, "peças.")
        jogador = "pc"
      else:
        jogada = computador_escolhe_jogada(n, m)
        n = n - jogada
        print("O computador tirou", jogada, "peças.")
        jogador = "usuario"
      if n != 0:
        print("Agora restam", n, "peças no tabuleiro.\n")

    if jogador == "usuario":
      print("Fim do jogo! O computador ganhou!\n")
      placarPc = placarPc + 1
    else:
      print("Você ganhou!\n")
      placarUsuario = placarUsuario + 1
    i = i + 1
  print("""**** Final do campeonato! ****

Placar: Você %d X %d Computador""" %(placarUsuario, placarPc))

partida()
