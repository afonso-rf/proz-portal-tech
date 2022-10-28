#!/usr/bin/python3
'''
Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
'''
print('=' * 80)
print('Consulta para melhor categoria de habilitação para o velículo.')
print('=' * 80)
print()
quant_rodas = int(input('Quantas rotas tem o veículo (entre 2 a 4)? '))
peso_veiculo = float
quant_pessoas = int
resposta = str

if 2 <= quant_rodas <= 3:
    resposta = f'A categoria de habilitação para o veículo de {quant_rodas} rodas é: A'
    
elif quant_rodas >= 4:
    peso_veiculo = float(input('Qual o peso bruto do veículo (Kg)? ' ))
    quant_pessoas = int(input('Quantas pessoas o veículo comporta? '))
    if quant_rodas == 4 and peso_veiculo <= 3500 and quant_pessoas <= 8:
        resposta = f'A categoria de habilitação para o veículo de {quant_rodas} rodas e com o peso até 3500Kg é: B'
    elif 3500 <= peso_veiculo <= 6000 and quant_pessoas <=8:
        resposta = f'A categoria de habilitação para o veículo de {quant_rodas} rodas e com o peso de {peso_veiculo}Kg é: C'
    elif quant_pessoas > 8:
        resposta = f'A categoria de habilitação para o veículo que comportam mais de 8 pessoas é: D'
    else:
        resposta = f'A categoria de habilitação para o veículo com o peso maior que 6000Kg é: E'
else:
    resposta = 'Quantidade de rotas está incorreto. Tente novamente. '

print('-' * 80)
print(resposta)
print('-' * 80)