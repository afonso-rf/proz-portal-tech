'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 
e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou 
completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o 
erro e continuará perguntando até que um valor correto seja preenchido.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse 
projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
'''

# Resposta:

# Função Opcional
def banner():
    print('#' * 80)
    print(f'#{"Consulte sua Idade atual":^78}#')
    print('#' * 80)
    
banner()
print()
print('Qual seu nome?')
nome = input('>> ').strip().title()
idade = 0
while True:
    try:
        ano = int(input('Em que ano você nasceu? ').strip())
        if 1922 < ano < 2021:
           idade = 2022 - ano
           break
        else:
            print('Ano invalido! Digite o ano correto.')
    except Exception as error:
      print('Erro! Por favor, digite somente números inteiros.')

print('=' * 80)
print(f'Olá {nome}!\nVocê tem {idade} anos.')
print('=' * 80)
print(f'Obrigado e até mais!')
