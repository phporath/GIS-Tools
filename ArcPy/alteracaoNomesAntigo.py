# -*- coding: utf-8 -*-
import arcpy

shp = "C:\Users\pedro.henrique\Documents\LabTrans\SEPIII\TUP\PoligonaisTUPsVersao10-11-2015\Bloco IV\PoligonalBlocoIV.shp"  #endereço da camada

nome = 'teste' #nome do campo a ser copiado

expressao = 'Campo(!TUP!)'  #alterar o nome do campo de referência

codeblock = """

def Campo (nome):
	nmCompleto = ''
	nrLista = 0
	texto = ''
	lista = nome.split(' ')

	while nrLista < len(lista):
		texto = lista[nrLista]
		nmParcial = texto[0].upper() + texto[1:len(texto)].lower()
		nmCompleto = nmCompleto + nmParcial + ' '
		nrLista = nrLista + 1
	def Campo (nome):
	nome = nome.title()
	nome = nome.replace(' Da ',' da ')
	nome = nome.replace(' Das ',' das ')
	nome = nome.replace(' De ',' de ')
	nome = nome.replace(' Do ',' do ')
	nome = nome.replace(' Dos ',' dos ')
	nome = nome.replace(' E ',' e ')
	nome = nome.replace(" D'a"," d'A")
	nome = nome.replace("-D'Á"," d'Á")
	nome = nome.replace(" D'o "," D'O ")
	#números romanos
	nome = nome.replace(' Iiv',' IIV')
	nome = nome.replace(' Iii',' III')
	nome = nome.replace(' Ii',' II')
	nome = nome.replace(' Viii',' VIII')
	nome = nome.replace(' Vii',' VII')
	nome = nome.replace(' Vi',' VI')
	nome = nome.replace(' Xiv',' XIV')
	nome = nome.replace(' Xix',' XIX')
	nome = nome.replace(' Xv',' XV')
	nome = nome.replace(' Xviii',' XVIII')
	nome = nome.replace(' Xvii',' XVII')
	nome = nome.replace(' Xvi',' XVI')
	nome = nome.replace(' Xx',' XX')
	#siglas
	nome = nome.replace('Apa ','APA ')
	nome = nome.replace('Cr ','CR ')
	nome = nome.replace('Floe ','FLOE ')
	nome = nome.replace('Floe ','FLOE ')
	nome = nome.replace('Flona ','FLONA ')
	nome = nome.replace('Pa ','PA ')
	nome = nome.replace('Pad ','PAD ')
	nome = nome.replace('Pad ','PA ')
	nome = nome.replace('Pae ','PAE ')
	nome = nome.replace('Par ','PAR ')
	nome = nome.replace('Pc ','PC ')
	nome = nome.replace('Pca ','PCA ')
	nome = nome.replace('Pct ','PCT ')
	nome = nome.replace('Pds ','PDS ')
	nome = nome.replace('Pe ','PE ')
	nome = nome.replace('Pic ','PIC ')
	nome = nome.replace('Prb ','PRB ')
	nome = nome.replace('Rds ','RDS ')
	nome = nome.replace('Resex ','RESEX ')
	nome = nome.replace('Rppn ','RPPN ')
	
	return nome
	
	return nome"""

arcpy.CalculateField_management(shp, nome, expressao, 'PYTHON_9.3', codeblock)