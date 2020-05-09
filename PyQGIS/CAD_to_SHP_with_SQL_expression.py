# coding=utf-8
import os
import glob
# from osgeo import ogr

# colocar o endereço onde estão os arquivos CAD
folderCAD = 'C:/Users/phpor/Documents/SPU/Projeto - LTM LPM/1088/DadosOriginais/DGN_LPM_11_09_2019_Processo_1088/Folhas_SaíGuaçú_Penha CD45'
extension = '*.dgn'

# folder path of Result shapefile
path_res = os.path.dirname(folderCAD) # não precisa usar
# go to Select_folder
os.chdir(folderCAD)
# copy the shapefiles (you don't need to load the shapefiles, so use runalg)
for nameCAD in glob.glob(extension):
    print (nameCAD) # just for test the argumment
    # I need convert nameCAD to nameSHP
