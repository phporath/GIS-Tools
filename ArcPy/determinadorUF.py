# Em parser selecionar Python
#Em "Pre-Logic Script Code" digite:
def Reclass(codMun):
	if (codMun == '11'):
		return 'RO'
	elif (codMun == '12'):
		return 'AC'
	elif (codMun == '13'):
		return 'AM'
	elif (codMun == '14'):
		return 'RR'
	elif (codMun == '15'):
		return 'PA'
	elif (codMun == '16'):
		return 'AP'
	elif (codMun == '17'):
		return 'TO'
	elif (codMun == '21'):
		return 'MA'
	elif (codMun == '22'):
		return 'PI'
	elif (codMun == '23'):
		return 'CE'
	elif (codMun == '24'):
		return 'RN'
	elif (codMun == '25'):
		return 'PB'
	elif (codMun == '26'):
		return 'PE'
	elif (codMun == '27'):
		return 'AL'
	elif (codMun == '28'):
		return 'SE'
	elif (codMun == '29'):
		return 'BA'
	elif (codMun == '31'):
		return 'MG'
	elif (codMun == '32'):
		return 'ES'
	elif (codMun == '33'):
		return 'RJ'
	elif (codMun == '35'):
		return 'SP'
	elif (codMun == '41'):
		return 'PR'
	elif (codMun == '42'):
		return 'SC'
	elif (codMun == '43'):
		return 'RS'
	elif (codMun == '50'):
		return 'MS'
	elif (codMun == '51'):
		return 'MT'
	elif (codMun == '52'):
		return 'GO'
	elif (codMun == '53'):
		return 'DF'
	else:
		return 0
#No campo abaixo "Nome do campo=" digite apenas:
Reclass(!CD_GEOCMU![0:2])
