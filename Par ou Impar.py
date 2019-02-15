#Author: Braian
from random import randint
from time import sleep
ganhou = 0
print('●▬▬▬▬▬▬▬▬▬▬▬********▬▬▬▬▬▬▬▬▬▬▬●')
print('  ░░░░░░ Par ou impar? ░░░░░░ ')
print('●▬▬▬▬▬▬▬▬▬▬▬********▬▬▬▬▬▬▬▬▬▬▬●')

while True:
	parimpar = str(input(" \nPar ou Impar? → "))
	if parimpar == 'sair':
		break
	parimpar = parimpar.capitalize()
	while parimpar != 'Par' and parimpar != 'Impar':
		parimpar = str(input(" \nDigite novamente - Par ou Impar? → "))
	user_input = int(input("Digite um valor: "))
	print("O computador está pensando...")
	sleep(0.2)
	print(" \n18%")
	sleep(0.2)
	print("48%")
	sleep(0.2)
	print("79%")
	sleep(0.2)
	print("100% - Completo!\n ")
	cpu_input = randint(0, 5)
	total = user_input+cpu_input
	if parimpar ==  'Par' and total%2==0:
		ganhou+=1
		print(f' \nVocê ganhou, pois o computador jogou o numero {cpu_input} e você {user_input}, que tem o total {total}, ou seja, um numero PAR!!')
		sleep(0.2)
		print(" \n[*] +1 PONTO")
	elif parimpar == 'Impar' and total%2==0:
		print(f' \nVocê perdeu, pois o computador jogou o numero {cpu_input} e você {user_input}, que tem o total {total}, ou seja, um numero PAR!!')
		sleep(0.2)
		print(" \n[*] GameOver :( ")
		print(f' \nVocê ganhou {ganhou} vezes !')
		break
	elif parimpar =='Par' and total%2!=0:
		print(f' \nVocê perdeu, pois o computador jogou o numero {cpu_input} e você {user_input}, que tem o total {total}, ou seja, um numero IMPAR!!')
		sleep(0.2)
		print(" \n[*] GameOver :( ")
		print(f' \nVocê ganhou {ganhou} vezes !')
		break
	elif parimpar =='Impar' and total%2!=0:
		ganhou+=1
		print(f' \nVocê ganhou, pois o computador jogou o numero {cpu_input} e você {user_input}, que tem o total {total}, ou seja, um numero IMPAR!!')
		sleep(0.2)
		print(" \n[*] +1 PONTO")



