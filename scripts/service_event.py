
def get_contract(item):
    contract=dict()
    contract['_id']=item['idEvent']
    contract['nombre']=item['strEvent']
    contract['equipoLocal']=item['strHomeTeam']
    contract['equipoVisita']=item['strAwayTeam']
    contract['ronda']=int(item['intRound'])
    contract['fecha']=item['strTimestamp']
    contract['liga']=item['strLeague']
    contract['golesLocal']=item['intHomeScore'] if not item['intHomeScore'] else int(item['intHomeScore'])
    contract['golesVisita']=item['intAwayScore'] if not item['intAwayScore'] else int(item['intAwayScore'])
    contract['estadio'] = item['strVenue']
    contract['estado'] = item['strStatus']
    return contract

def find_countries(local, visitante):
	localObj = _find_country(local)
	visitanteObj = _find_country(visitante)
	return localObj['nombre'], visitanteObj['nombre'], localObj['iso'], visitanteObj['iso'], localObj['nombre'] + ' vs ' + visitanteObj['nombre'] 
	

def _find_country(pais):
	for country in _countries():
		if country['name'] == pais:
			return country
	return ''

def _countries():
  return [
		{"iso":"QA", "nombre": "Qatar", "name":"Qatar"},
		{"iso":"EC", "nombre": "Ecuador", "name":"Ecuador"},
		{"iso":"SN", "nombre": "Senegal", "name":"Senegal"},
		{"iso":"NL", "nombre": "Holanda", "name":"Netherlands"},
		{"iso":"XX", "nombre": "Inglaterra", "name":"England"},
		{"iso":"IR", "nombre": "Iran", "name":"Iran"},
		{"iso":"US", "nombre": "Estados Unidos", "name":"USA"},
		{"iso":"XX", "nombre": "Gales", "name":"Wales"},
		{"iso":"AR", "nombre": "Argentina", "name":"Argentina"},
		{"iso":"SA", "nombre": "Arabia Saudita", "name":"Saudi Arabia"},
		{"iso":"MX", "nombre": "Mexico", "name":"Mexico"},
		{"iso":"PL", "nombre": "Polonia", "name":"Poland"},
		{"iso":"FR", "nombre": "Francia", "name":"France"},
		{"iso":"AU", "nombre": "Australia", "name":"Australia"},
		{"iso":"DK", "nombre": "Dinamarca", "name":"Denmark"},
		{"iso":"TN", "nombre": "Túnez", "name":"Tunisia"},
		{"iso":"ES", "nombre": "España", "name":"Spain"},
		{"iso":"CR", "nombre": "Costa Rica", "name":"Costa Rica"},
		{"iso":"DE", "nombre": "Alemania", "name":"Germany"},
		{"iso":"JP", "nombre": "Japón", "name":"Japan"},
		{"iso":"BE", "nombre": "Bélgica", "name":"Belgium"},
		{"iso":"CA", "nombre": "Canada", "name":"Canada"},
		{"iso":"MA", "nombre": "Marruecos", "name":"Morocco"},
		{"iso":"HR", "nombre": "Croacia", "name":"Croatia"},
		{"iso":"BR", "nombre": "Brasil", "name":"Brazil"},
		{"iso":"RS", "nombre": "Serbia", "name":"Serbia"},
		{"iso":"CH", "nombre": "Suiza", "name":"Switzerland"},
		{"iso":"CM", "nombre": "Camerún", "name":"Cameroon"},
		{"iso":"PT", "nombre": "Portugal", "name":"Portugal"},
		{"iso":"GH", "nombre": "Ghana", "name":"Ghana"},
		{"iso":"UY", "nombre": "Uruguay", "name":"Uruguay"},
		{"iso":"KR", "nombre": "Corea del Sur", "name":"South Korea"},
	]