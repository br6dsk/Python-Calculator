#Author: Braian
print("[*] ########## [*]")
print("[*] Peso Ideal [*]")
print("[*] ########## [*]")
print('')
print('   [*] Digite em CM. Ex: 1,70m = 170cm    ')
print('')
altura_em_cm = int(input('Qual sua altura?: '))
print('')
sexo = str(input('[H] para masculino, [M] para feminino: '))
if sexo =='M' or 'm':
    print('')
    print('Seu peso idel M é', ((altura_em_cm-100)-(altura_em_cm-150)/2))
    print('')
elif sexo =='H' or 'h':
    print('')
    print('Seu peso idel M é', ((altura_em_cm - 100) - (altura_em_cm - 150) / 4))
    print('')