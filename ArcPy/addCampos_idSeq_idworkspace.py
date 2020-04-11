# -*- coding: utf-8 -*-
import arcpy
import csv

arcpy.env.workspace = input('Inserir endereço onde estão salvos os Shapefiles: ')  #colocar endereço onde estão as camadas

shapes = arcpy.ListFeatureClasses()

checker_fieldname = ''
nchecker_idseq = 0
nchecker_idw_kspace = 0

for shape in shapes:
        fields = arcpy.ListFields(shape)
        
        for field in fields:
                checker_fieldname = field.name

                if checker_fieldname == 'idseq':
                        nchecker_idseq += 1
                else:
                        nchecker_idseq = nchecker_idseq
                print(nchecker_idseq)

                if checker_fieldname == 'idw_kspace':
                        nchecker_idw_kspace += 1
                else:
                        nchecker_idw_kspace = nchecker_idw_kspace
                print(nchecker_idw_kspace) 

        if nchecker_idseq == 0:
                arcpy.AddField_management(shape, 'idseq', 'SHORT', 4, '', '', '', 'NULLABLE', 'REQUIRED')  #criar uma linha para cada campo novo a ser criado
                
        else:
                arcpy.DeleteField_management(shape, 'idseq')
                arcpy.AddField_management(shape, 'idseq', 'SHORT', 4, '', '', '', 'NULLABLE', 'REQUIRED')
                print(shape)
                nchecker_idseq = 0

        if nchecker_idw_kspace == 0:
                arcpy.AddField_management(shape, 'idw_kspace', 'SHORT', 4, '', '', '', 'NULLABLE', 'REQUIRED')  #criar uma linha para cada campo novo a ser criado
                
        else:
                arcpy.DeleteField_management(shape, 'idw_kspace')
                arcpy.AddField_management(shape, 'idw_kspace', 'SHORT', 4, '', '', '', 'NULLABLE', 'REQUIRED')
                print(shape)
                nchecker_idw_kspace = 0
                
        arcpy.CalculateField_management(shape, 'idseq', 0, "PYTHON_9.3")
        arcpy.CalculateField_management(shape, 'idw_kspace', 0, "PYTHON_9.3")
        
print('Fim do processo')
