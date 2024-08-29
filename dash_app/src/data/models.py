from dataclasses import dataclass

@dataclass
class Record:
    station_id: int
    state: str
    available_bikes: int
    available_places: int
    connexion_state: str
    last_update: str
    record_timestamp: str
    
    # @classmethod
    # def from_dict(cls, record: dict, timestamp: str) -> 'Record':
    #     return cls(
    #         station_id          =record["properties"]["objectid"],
    #         state               =record["properties"]["etat"],
    #         available_bikes     =record["properties"]["nb_velos_dispo"],
    #         available_places    =record["properties"]["nb_places_dispo"],
    #         connexion_state     =record["properties"]["etat_connexion"],
    #         last_update         =record["properties"]["date_modification"],
    #         record_timestamp    =timestamp
    #     )


@dataclass
class Station:
    id: int
    name: str
    adress: str
    city: str
    type: str
    latitude: float
    longitude: float
    