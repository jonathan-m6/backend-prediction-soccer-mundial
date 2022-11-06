
def get_contract(item):
    contract=dict()
    contract['idEvent']=item['idEvent']
    contract['strEvent']=item['strEvent']
    contract['strHomeTeam']=item['strHomeTeam']
    contract['strAwayTeam']=item['strAwayTeam']
    contract['intRound']=item['intRound']
    contract['strTimestamp']=item['strTimestamp']
    contract['strBanner']=item['strBanner']
    contract['strLeague']=item['strLeague']
    contract['strFilename']=item['strFilename']
    contract['intHomeScore']=item['intHomeScore']
    contract['intAwayScore']=item['intAwayScore']
    return contract