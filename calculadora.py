#coding: utf-8
print('')
print('###############################')
print('##### Calculadora simples #####')
print('###############################')
print('')
def Adição(x, y):
	return(x + y)
	
def Subtração(x, y):
	return(x - y)

def Divisão(x, y):
	return(x / y)

def Multiplicação(x, y):
	return(x * y)
	pass
print('')
print('[*] Selecione o numero da respectiva operação! [*]')
print('Adição: [1]')
print('Subtração: [2]') 
print('Divisão: [3]')
print('Multiplicação: [4]')
print('')

escolha = int(input('[*] Qual operação deseja?: '))
print('')
num1 = int(input('[*] Numero: '))
print('')
num2 = int(input('[*] Numero: '))

if escolha == 1:
	print('')
	print("A soma de", num1,"+",num2,"=", Adição(num1,num2))

elif escolha == 2:
	print('')
	print("A diferença de", num1,"-",num2,"=", Subtração(num1,num2))
	
elif escolha == 3:
	print('')
	print("A divisão de", num1,"/",num2,"=", Divisão(num1,num2))
elif escolha == 4:
	print('')
	print("A multiplicação de", num1,"*",num2,"=", Multiplicação(num1,num2))
else:
	print('')
	print('>>>>>[*] Error [*]<<<<<')
	

quit()


