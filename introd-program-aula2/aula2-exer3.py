'''
CODE PARK SUBSTITUTO : é o PRIMEIRO!

Aprender a executar laços de repetição 

Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é 
supersticioso e optou por não ter um 13ro andar. 
Escreva um código que imprima todos os números exceto o número 13. Escreva mais dois códigos que 
resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição 
aprendidos. Como desafio, imprima eles em ordem decrescente (20, 19, 18...
'''
#Resposta:
print('Imprimindo números para os andares. ')

## 1º codigo
print('1º Impressão.')
print('-' * 30)
for i in range(1, 21):
    if i == 13:
        print('Pula!')
    else:
        print(i, 'º andar')

print('-' * 30)
print()
###################
## 2º codigo
print('2º Impressão')
print('-' * 30)
andar = 0
while andar < 20:
    andar += 1
    if andar == 13:
        print('Pula!!')
    else:
        print(andar, 'º Andar')
        
print('-' * 30)
print()
##################
## 3º codigo
print('3º Impressão')
print('-' * 30)
for i in range(21):
     if i == 0 or i == 13:
         continue
     print(i, 'º andar')

print('-' * 30)
print()
##################
## 4º codigo
print('4º Impressão')
print('-' * 30)
for i in range(20, 0, -1):
    if i == 13:
        print('Pula!!!!')
    else:
        print(i, 'ºAndar.')
print('-' * 30)
print('ACABOU!!!')