#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import arcpy

args = sys.argv[1:]

# Functions definitions
def getPath(args):
    return args[0];

def getFileName(args):
    return '{0}.csv'.format(args[1]);

def goTo(path):
    os.chdir(path)
    return;

def toASCII(str):
    return str.encode('ascii', 'ignore').decode('ascii');

def writeCSV(arcpy, fileName):
    with open(fileName, 'wb') as csvfile:
        streamWriter = csv.writer(csvfile, delimiter=',')
        streamWriter.writerow(['Nome arquivo', 'Coluna', 'Tipo', 'Extensão'])
        shapes = arcpy.ListFeatureClasses()
        for shape in shapes:
            fields = arcpy.ListFields(shape)
            for field in fields:
                streamWriter.writerow([toASCII(shape), toASCII(field.name), field.type, field.length])
    return;

# Main
arcpy.env.workspace = getPath(args)
goTo(getPath(args))
writeCSV(arcpy, getFileName(args))