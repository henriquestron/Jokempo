from random import randint
from time import sleep

itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)


print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua opção: '))
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURA!!!')
sleep(0.5)

print('-='*25)
print('O computador escolheu {} e voce escolheu {}.' .format(itens[computador], itens[jogador]))
print('-='*25)


if(computador == 0): #PEDRA
   if(jogador == 0):
      print('Empate')
   elif(jogador == 1):
      print('Você Ganhou!')
   elif(jogador == 2):
      print('Computador Ganhou!')
   else:
      print('Opção Invalida!')

elif(computador == 1):  #PAPEL   
   if(jogador == 0):
      print('Você Perdeu!')
   elif(jogador == 1):
      print('EMPATE!')
   elif(jogador == 2):
      print('Você Ganhou!')
   else:
      print('Opção Invalida!') 

elif(computador == 2):  #TESOURA
   if(jogador == 0):
      print('Você Ganhou!')
   elif(jogador == 1):
      print('Computador Ganhou!')
   elif(jogador == 2):
      print('EMPATE!')
   else:
      print('Opção Invalida!') 
   
avalie = int(input('Dê a sua nota para o programa: '))

if(avalie > 5):
   print('Obrigado, sua nota incentiva muito o criador a continuar criando programas melhores!')
elif(avalie <= 5):
   print('Os de verdade eu sei quem são viu 😔✊!!')

reinicie = int(input('Gostaria de tentar novamente? Abra o programa novamente! O criador não conseguiu criar um código para reiniciar o sistema!!'))
