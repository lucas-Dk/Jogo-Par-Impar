#Bibliotecas usadas
import random
import time

#variável de vitória
v = 0

#para repetir sempre que o usuario ganhar
while True:
  player = int(input('\nInforme um valor: '))
  pc = random.randint(0, 10)
  total = player + pc
  par_impar = str(input('\nVocê quer par ou ímpar? [P/I]: ')).upper()[0]

#validação de escolha
  while par_impar.strip() not in 'P' and par_impar.strip() not in 'I':
    par_impar = str(input('\nVocê quer par ou ímpar? [P/I]: ')).upper()[0]

#saída de dados
  print('\nBatendo dados...')
  time.sleep(3)    
  print('\nVocê jogou {} e o pc jogou {}, a soma foi {}\n'.format(player, pc, total))

#verifição de resultados 
  if total %2 == 0:
    print('Deu par\n')
  else:
    print('Deu impar\n')

#Pela escolha, retornará a saída par
  if par_impar == 'P':
    if total %2 == 0:
      print('\033[1;32mJogador ganhou\033[m\n')
      v = v + 1
    else:
      print('\033[1;33mComputador ganhou\033[m\n')

#Pela escolha retornará a saída ímpar
  elif par_impar == 'I':
    if total %2 == 1:
      print('\033[1;32mJogador ganhou\033[m\n')
      v = v + 1
    else:
      print('\033[1;33mComputador ganhou\033[m\n')

  again = str(input('Deseja jogar novamente? [S/N]: ')).upper()[0]

#Validação de escolha
  while again.strip() not in 'S' and again.strip() not in 'N':
    again = str(input('\nInforme uma opção valida! Deseja jogar novamente? [S/N]: ')).upper()[0]

#Retirá sempre que o player ganhar
  if again.strip() in 'S':
    print('\nReiniciando...')
    time.sleep(2)

#Player escolheu sair
  elif again in 'N':
    print('\nEncerrando...')
    time.sleep(2)
    break

#Saída de vitórias
print('\n\033[1;32mVitorias player [{}]\033[m\n'.format(v))
