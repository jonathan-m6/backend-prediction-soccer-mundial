
def get_contract(item):
    contract=dict()
    contract['_id']=item['idEvent']
    contract['nombre']=item['strEvent']
    contract['equipoLocal']=item['strHomeTeam']
    contract['equipoVisita']=item['strAwayTeam']
    contract['ronda']=item['intRound']
    contract['fecha']=item['strTimestamp']
    contract['liga']=item['strLeague']
    contract['golesLocal']=item['intHomeScore']
    contract['golesVisita']=item['intAwayScore']
    contract['estadio'] = item['strVenue']
    contract['esatdo'] = item['strStatus']
    return contract