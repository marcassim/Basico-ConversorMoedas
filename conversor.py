from unittest import result
from forex_python.converter import CurrencyCodes, CurrencyRates

cr = CurrencyRates()
cc = CurrencyCodes()

def titulo(txt):
    print('-'*len(txt))
    print('\033[34m'+txt+'\033[0;0m')
    print('-'*len(txt))

def moeda():
    print('\033[35m\n1 - BRL\n2 - USD\n3 - OUTRO:\n4 - SAIR\33[0;0m')

while True:
    titulo('Conversor de Moedas')
    # titulo(' - Insira o valor para conversão\n - Insira a moeda inicial\n - Insira a moeda de CAMBIO')
    titulo('Valor Inicial')

    while True:
        try:
            valor_inicial = float(input('Insira o valor desejado para a operação:  \n'))
            break
        except ValueError:
            print('\033[31m Entrada inválida. Insira um valor válido! \33[0;0m')

    titulo('Selecione a moeda inicial')
    cod_moeda_inicial = None
    while cod_moeda_inicial not in (1,2,3,4):
        moeda()
        try:
            cod_moeda_inicial = int(input('Selecione uma das 4 opções: '))
            if cod_moeda_inicial == 1:
                cod_moeda_inicial = 'BRL'
                print('Código escolhido: = ', cod_moeda_inicial)
                break
            elif cod_moeda_inicial ==2:
                cod_moeda_inicial = 'USD'
                print('Código escolhido: = ', cod_moeda_inicial)
                break
            elif cod_moeda_inicial ==3:
                cod_moeda_inicial= input('\nOUTRO, código da moeda escolhida (três digitos):').upper()
                print('Código de escolha do país de operação: ', cod_moeda_inicial)
                break
            elif cod_moeda_inicial ==4:
                break
            else: 
                print('Digite apenas 1 a 3')
        except:
            print('Opção inválida! Digite uma opção existente')

    titulo ('Selecione a moeda para câmbio')
    cod_moeda_cambio = None
    while cod_moeda_cambio not in (1,2,3,4):
        moeda()
        try:
            cod_moeda_cambio=int(input('Selecione uma ds 4 opções:  '))
            if cod_moeda_cambio ==1:
                cod_moeda_cambio='BRL'
                print('código escolhido:', cod_moeda_cambio)
                break
            elif cod_moeda_cambio ==2:
                cod_moeda_cambio = 'USD'
                print('código escolhido:', cod_moeda_cambio)
                break
            elif cod_moeda_cambio ==3:
                cod_moeda_cambio= input('\nOUTRO, código da moeda escolhida (três digitos):').upper()
                print('Código de escolha do país de operação: ', cod_moeda_cambio)
                break
            elif cod_moeda_inicial ==4:
                break
            else: 
                print('Digite apenas 1 / 2 / 3 / 4')
        except:
            print('Opção inválida! Digite uma opção existente')


    
    titulo('Convertendo...')
    result = cr.convert(cod_moeda_inicial, cod_moeda_cambio, valor_inicial)
    simbolo_moeda = cc.get_symbol(cod_moeda_inicial)
    simbolo_moeda_cambio = cc.get_symbol(cod_moeda_cambio)
    result = round(result,3)

    print(f'{cod_moeda_inicial} - {simbolo_moeda}{valor_inicial} = {cod_moeda_cambio} - {simbolo_moeda_cambio} {result}')
