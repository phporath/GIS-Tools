# -*- coding: UTF-8 -*-

Chaves = ["Levantar", "Analisar", "Povoar", "Documentar", "Homologar"]
Temas = ["Tema 1", "Tema 2", "Tema 3", "Tema x"]

cTemas = 0
cChaves = 0

while cTemas < len(Temas):
    while cChaves < len(Chaves):
        print(Chaves[cChaves]+"|"+Temas[cTemas])
        cChaves = cChaves + 1
    cChaves = 0
    cTemas = cTemas + 1