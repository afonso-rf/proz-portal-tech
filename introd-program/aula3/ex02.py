'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
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
    

#### Banner
sublinha('*')
print(f'{"CALCULADORA":^80}') #
sublinha('*')

while True:
    print('Escolha uma das operações abaixo para caulcular.')
    sublinha('-')
    print('( 1 ) - Soma')
    print('( 2 ) - Subtração')
    print('( 3 ) - Multiplicação')
    print('( 4 ) - Divisão')
    print('( 0 ) - Sair')
    sublinha('=')
    calc = 0
    resp = int(input('Informe a operação desejada: '))
    if resp == 0:
        break
    elif  0 < resp < 5:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número:  '))
        sublinha('-')
        if resp == 1:
            calc = calculadora(num1, num2, '+')
            operador = '+'
        elif resp == 2:
            calc = calculadora(num1, num2, '-')
            operador = '-'
        elif resp == 3:
            calc = calculadora(num1, num2, 'x')
            operador = 'x'
        elif resp == 4:
            calc = calculadora(num1, num2, '/')
            operador = '/'
        print('O resuntado de', num1, operador, num2,'é:', calc)
        sublinha('-')
        input('Tecle "Enter" para continuar...')
        sublinha('=')
    else:
        print('Opção invalida! Tente novamente.')
        print()
        input('Tecle "Enter" para continuar...')
print()
print('Encerrando o programa...')
print('Obrigado e volte sempre!!!')