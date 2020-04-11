# -*- coding: cp1252 -*-

import arcpy
import csv

# operar script no diret�rio "C"

print('''
--------------------------------------------------------------------------------------------------------------------------------------------------

Para o uso desta ferramenta, alguns padr�es devem ser obedecidos, por exemplo:

	- As listas devem possuir aspas sob cada campo e serem separadas por v�ruglas, por exemplo: 'S�o Paulo', 'Campinas'.
	- O mesmo padr�o serve para os n�meros, por exemplo: '43454', '8897879'.
	- O output desra ferramenta � uma planilha CSV. Dessa forma, espera-se o nome do arquivo no seguinte padr�o: 'matrizOD.csv'

--------------------------------------------------------------------------------------------------------------------------------------------------
''')

idOrigem = input('Inserir lista de ID origens: ')
origem = input('Inserir lista de origens: ')
idDestino = input('Inserir lista de ID destinos: ')
destino = input('Inserir lista de destinos: ')

print ('''
--------------------------------------------------------------------------------------------------------------------------------------------------

Guia para inser��o do tipo de Origem e Destino:
1 - Cidades
2 - Instala��es Portu�rias
3 - Terminais Ferrovi�rios de Carga

--------------------------------------------------------------------------------------------------------------------------------------------------
''')

tpOrigem = input('Inserir o n�mero referente ao tipo de origem: ')
if tpOrigem == 1:
    tipoOrigem = ["Cidades"]
elif tpOrigem == 2:
    tipoOrigem = ["Instala��es Portu�rias"]
elif tpOrigem == 3:
    tipoOrigem = ["Terminais Ferrovi�rios de Carga"]
else:
    print("Valor n�o encontrado, digite outro valor!")
    
tpDestino = input('Inserir o n�mero referente ao tipo de destino: ')
if tpDestino == 1:
    tipoDestino = ["Cidades"]
elif tpDestino == 2:
    tipoDestino = ["Instala��es Portu�rias"]
elif tpDestino == 3:
    tipoDestino = ["Terminais Ferrovi�rios de Carga"]
else:
    print("Valor n�o encontrado, digite outro valor!")

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


