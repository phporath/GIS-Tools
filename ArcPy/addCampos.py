# -*- coding: utf-8 -*-
import arcpy
arcpy.env.workspace = "C:\Users\pedro.henrique\Documents\LabTrans\SEPIII\TUP\Bloco III\TUP_Braskarne\SHP"  #colocar endereço onde estão as camadas

lista = ['camada1','camada2'] #colocar nomes exatos das camadas em questão
nrLista = 0

while nrLista < len(lista):
	nome = lista[nrLista]
	arcpy.AddField_management(nome, 'coluna1', 'LONG', 9, '', '', '', 'NULLABLE', 'REQUIRED')  #criar uma linha para cada campo novo a ser criado
	arcpy.AddField_management(nome, 'coluna2', 'TEXT', 20, '', '', '', 'NULLABLE', 'REQUIRED')
	nrLista = nrLista + 1

# referencia para criação de campos "http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm"