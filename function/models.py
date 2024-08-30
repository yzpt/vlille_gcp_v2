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

@dataclass
class Station:
    id: int
    name: str
    adress: str
    city: str
    type: str
    latitude: float
    longitude: float
    