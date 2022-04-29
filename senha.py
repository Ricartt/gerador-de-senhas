import random 

min = 'abcdefghijklmnopqrstuvwxyz'
maiusc = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
simb = '[]{}() *&:;=+_-@!"#'

print(' --------------- Gerador de senhas --------------- ')
qtd = input('Digite o tamanho da senha: ')
qtdInt = int(qtd)
length = qtdInt
todo = min + maiusc + num + simb
 
passwordTodo = " ".join(random.sample(todo, length))

maiuscNum = maiusc + num
passwordMaiusNum = " ".join(random.sample(maiuscNum, length))

maiuscMin = maiusc + min 
passwordMaiusMin = " ".join(random.sample(maiuscMin, length))

print('')
print(' --------------- Senhas Geradas --------------- ')
print('password com letras, numeros e simbolos = '  + passwordTodo)
print('password com números e letras miúsculas = ' + passwordMaiusNum)
print('password com letras maiúsculas e minusculas = ' + passwordMaiusMin)
