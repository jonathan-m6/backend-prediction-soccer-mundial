
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