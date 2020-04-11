# -*- coding: UTF-8 -*-

print('''
--------------------------------------------------------------------------------------------------------------------------------------------------

Para o uso desta ferramenta, alguns padrões devem ser obedecidos, por exemplo:

	- Em dia, deve ser inserido um número válido entre 0 e 31.
	- Em mês, deve ser inserido o número referente ao mês. Por exemplo: 1 para janeiro e 12 para dezembro.
	- Em ano, deve ser inserido o número referente ao ano. Por exemplo: 2017.

--------------------------------------------------------------------------------------------------------------------------------------------------
''')

dia = input('Inserir o dia: ')
mes = input('Inserir o mês: ')
ano = input('Inserir o ano: ')
cMes = 0
anoA = [31,29,31,30,31,30,31,31,30,31,30,31]
bissexto = ''
qtdeMes = 0
juliano = 0

if mes == 1:
        qtde = dia
else:
        while cMes < mes -1:
                qtdeMes = qtdeMes + anoA[cMes]
                cMes = cMes + 1
        qtde = qtdeMes + dia

if ano%4==0 and ano%100!=0 or ano%400==0:
        bissexto = 'Sim'
        juliano = qtde

elif mes >= 3:
        bissexto = 'Não'
        juliano = qtde - 1
else:
        bissexto = 'Não'
        juliano = qtde
	
print ("O dia juliano desta data (contagem de dias corridos) é " + str(juliano))
