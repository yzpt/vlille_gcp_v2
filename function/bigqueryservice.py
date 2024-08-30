from google.cloud import bigquery
from typing import List
from models import Record

class BigQueryService:
    def __init__(self, project_name: str, dataset_id: str, table_id: str):
        self.client = bigquery.Client(project=project_name)
        self.dataset_id = dataset_id
        self.table_id = table_id

    def insert_data(self, data: dict, timestamp: str) -> None:
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        table = self.client.get_table(table_ref)
        
        records_to_insert: List[Record] = []
        for record in data['features']:
            new_record = Record(
                station_id         =record["properties"]["objectid"],
                state              =record["properties"]["etat"],
                available_bikes    =record["properties"]["nb_velos_dispo"],
                available_places   =record["properties"]["nb_places_dispo"],
                connexion_state    =record["properties"]["etat_connexion"],
                last_update        =record["properties"]["date_modification"],
                record_timestamp   =timestamp
            )
            records_to_insert.append(new_record)
        
        # Convert the dataclass instances to dictionaries before insertion
        data_to_insert = [record.__dict__ for record in records_to_insert]
        self.client.insert_rows(table, data_to_insert)
