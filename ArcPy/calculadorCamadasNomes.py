# -*- coding: UTF-8 -*-

campos = ['Cod_TUP', 'TUP', 'Tipo_Polig', 'Poligonal', 'Bloco', 'UF'] 
nmParcial = ''
nmCompleto = ''
cCampos = 0


while cCampos < len(campos)-1:
        nmParcial = "'"+campos[cCampos]+": '+str(!"+campos[cCampos]+"!)+'/ '+"
        nmCompleto = nmCompleto + nmParcial
        cCampos = cCampos + 1
        while cCampos == len(campos)-1:
                nmParcial = "'"+campos[cCampos]+": '+str(!"+campos[cCampos]+"!)"
                nmCompleto = nmCompleto + nmParcial
                cCampos = cCampos + 1
print (nmCompleto)

