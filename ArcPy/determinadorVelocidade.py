# Em parser selecionar Python
#Em "Pre-Logic Script Code" digite:
def Reclass(classificacao, jurisdicao):
	if (classificacao == 'Planejada'):
		return 3
	elif (classificacao == 'Travessia'):
		return 4
	elif (classificacao == 'Leito natural') or (classificacao == 'Implantada') or (classificacao == 'Em obra de implanta��o'):
		return 28
	elif (classificacao == 'Em obra de pavimenta��o') and (jurisdicao == 'Municipal'):
		return 37
	elif ((classificacao == 'Pavimentada') and (jurisdicao == 'Municipal') or (jurisdicao == 'Privada')) or ((classificacao == 'Em obra de pavimenta��o')and (jurisdicao != 'Municipal')):
		return 51
	elif ((classificacao == 'Pavimentada') and (jurisdicao != 'Municipal' or jurisdicao != 'Privada')) or (classificacao == 'Em obra de duplica��o'):
		return 66
	elif (classificacao == 'Duplicada'):
		return 83
	else:
		return 0

#No campo abaixo "Nome do campo=" digite apenas:
Reclass(!cla_icacao!,!jurisdicao!)
