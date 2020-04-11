#Em "Pre-Logic Script Code" digite:

def TextValue(nomeVariavel):
    if nomeVariavel == 'P':
        return "Ponte"
    elif nomeVariavel == 'PE':
        return "Ponte estreita"
    elif nomeVariavel == 'V':
        return "Viaduto"
    elif nomeVariavel == 'VE':
        return "Viaduto estreito"
    elif nomeVariavel == 'T':
        return "Túnel"
    else:
        return "Teste"

#No campo abaixo "Nome do campo=" digite apenas:

TextValue( !Campo! )