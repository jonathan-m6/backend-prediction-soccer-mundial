def eventEntity(event) -> dict:
    return {
        "id": event["_id"],
        "idEvent": event["idEvent"],
        "strEvent": event["strEvent"],
        "strHomeTeam": event["strHomeTeam"],
        "strAwayTeam": event["strAwayTeam"],
        "intRound": event["intRound"],
        "strTimestamp": event["strTimestamp"],
        "strBanner": event["strBanner"],
        "strLeague": event["strLeague"],
        "strFilename": event["strFilename"],
        "intHomeScore": event["intHomeScore"],
        "intAwayScore": event["intAwayScore"]
    }


def eventListEntity(events) -> list:
    return [eventEntity(event) for event in events]

