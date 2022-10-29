'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números 
da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a 
seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse 
projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
'''

### Resposta:

# Função opcional 
def sublinha (caracter:str):
    print(caracter * 80)

# Função Calculadora
def calculadora (num1:int, num2:int, operador:str):
    ## Soma
    if operador == '+':
        return num1 + num2
    
    ## Subtração
    elif operador == '-':
        return num1 - num2
    
    ## Multiplicação
    elif operador in 'xX':
        return num1 * num2
    
    ## Divisão
    elif operador == '/':
        if num2 == 0:
            return 0
        else:
            return num1 / num2

    else:
        return 'Operador invalido'

# Banner
sublinha('*')
print(f'{"CALCULADORA":^80}')
sublinha('*')
print('Digite dois números e informe a operação desejada.')
sublinha('-')
print('( + ) - Soma')
print('( - ) - Subtração')
print('( x ) - Multiplicação')
print('( / ) - Divisão')
sublinha('=')

# Interação com o usuario
num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))
operador = str(input('Qual a operação? ')).lower()

sublinha('=')
print()

# Resultado
if operador in '+-xX/':
    print('O resultado de ', num1, operador, num2, 'é:', calculadora(num1, num2, operador))
else:
    print('Operador invalido! Tente novamente')
sublinha('_')