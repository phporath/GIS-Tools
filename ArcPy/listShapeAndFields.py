import arcpy
import csv

# operar script no diret�rio "C"
arcpy.env.workspace = input('Inserir endere�o onde est�o salvos os Shapefiles: ')

shapes = arcpy.ListFeatureClasses()

def toASCII(str):
    return str.encode('ascii', 'ignore').decode('ascii');

with open(input('Nome do arquivo csv: '), 'wb') as csvfile:
    streamWriter = csv.writer(csvfile, delimiter=',')
    streamWriter.writerow(['Nome arquivo', 'geometria', 'Coluna', 'Tipo', 'Extens�o'])
    for shape in shapes:
        desc = arcpy.Describe(shape)
        geometryType = desc.ShapeType
        print(geometryType)
        fields = arcpy.ListFields(shape)
        for field in fields:
            streamWriter.writerow([toASCII(shape), toASCII(geometryType), toASCII(field.name), field.type, field.length])
