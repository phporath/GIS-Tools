# -*- coding: cp1252 -*-

import arcpy
import csv

# operar script no diretório "C"

print('''
--------------------------------------------------------------------------------------------------------------------------------------------------

Para o uso desta ferramenta, alguns padrões devem ser obedecidos, por exemplo:

	- As listas devem possuir aspas sob cada campo e serem separadas por víruglas, por exemplo: 'São Paulo', 'Campinas'.
	- O mesmo padrão serve para os números, por exemplo: '43454', '8897879'.
	- O output desra ferramenta é uma planilha CSV. Dessa forma, espera-se o nome do arquivo no seguinte padrão: 'matrizOD.csv'

--------------------------------------------------------------------------------------------------------------------------------------------------
''')

idOrigem = input('Inserir lista de ID origens: ')
origem = input('Inserir lista de origens: ')
idDestino = input('Inserir lista de ID destinos: ')
destino = input('Inserir lista de destinos: ')

print ('''
--------------------------------------------------------------------------------------------------------------------------------------------------

Guia para inserção do tipo de Origem e Destino:
1 - Cidades
2 - Instalações Portuárias
3 - Terminais Ferroviários de Carga

--------------------------------------------------------------------------------------------------------------------------------------------------
''')

tpOrigem = input('Inserir o número referente ao tipo de origem: ')
if tpOrigem == 1:
    tipoOrigem = ["Cidades"]
elif tpOrigem == 2:
    tipoOrigem = ["Instalações Portuárias"]
elif tpOrigem == 3:
    tipoOrigem = ["Terminais Ferroviários de Carga"]
else:
    print("Valor não encontrado, digite outro valor!")
    
tpDestino = input('Inserir o número referente ao tipo de destino: ')
if tpDestino == 1:
    tipoDestino = ["Cidades"]
elif tpDestino == 2:
    tipoDestino = ["Instalações Portuárias"]
elif tpDestino == 3:
    tipoDestino = ["Terminais Ferroviários de Carga"]
else:
    print("Valor não encontrado, digite outro valor!")

cDestino = 0
cOrigem = 0

def toASCII(str):
    return str.encode('ascii', 'ignore').decode('ascii');

with open(input('Nome do arquivo csv: '), 'wb') as csvfile:
    streamWriter = csv.writer(csvfile, delimiter=',')
    streamWriter.writerow(['IdORIGEM', 'ORIGEM', 'TIPOORIGEM', 'IDDESTINO', 'DESTINO', 'TIPODESTINO', 'NOMECAMADA', 'FLUXO'])
    while cDestino < len(destino):
        while cOrigem < len(origem):
            nomeCamada = origem[cOrigem]+destino[cDestino]
            streamWriter.writerow([idOrigem[cOrigem],origem[cOrigem],tipoOrigem[0],idDestino[cDestino],destino[cDestino],tipoDestino[0],nomeCamada,1])
            cOrigem = cOrigem + 1
        cOrigem = 0
        cDestino = cDestino + 1


