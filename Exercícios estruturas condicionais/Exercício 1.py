#Author: Braian
print('[*] ###################### [*] ')
print('[*]  Sensor de Temperatura [*]')
print('[*] ###################### [*] ')
print('')
Temperatura = int(input('Qual temperatura atual?: '))
if Temperatura <=1000:
    print('')
    print('[*] Temperatura normal! [*]')
    print('[*] Sem risco [*]')
    print('')
elif Temperatura <=2000:
    print('')
    print('[*] Temperatura crítica! [*]')
    print('[*] Iniciar refrigeração [*]')
    print('')
    quit()
