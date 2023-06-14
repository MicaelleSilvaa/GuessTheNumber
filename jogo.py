# ////////////////////////////////////////////////////////////////////////////////////
import random as r

aleatorio1=r.randint(1,10)
print('\n///////////ADVINHE O NÚMERO!///////////\n')

while True:
  chute=int(input('Informe um número entre 0 e 10: '))
  if chute==aleatorio1:
    print(f'Acertou, o número sorteado é: {aleatorio1}')
    break
  else:
    if chute>aleatorio1:
     print('Tente novamente, o número é menor!')
    elif chute<aleatorio1:
      print('Tente novamente, o número é maior!')
