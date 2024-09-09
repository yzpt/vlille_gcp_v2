from google.cloud import bigquery

class BigQueryService:
    def __init__(self, project_name: str, dataset_id: str, table_id: str):
        self.client = bigquery.Client(project=project_name)
        self.dataset_id = dataset_id
        self.table_id = table_id

    def insert_data(self, data: dict, timestamp: str) -> None:
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        table = self.client.get_table(table_ref)
        
        data_to_insert = []
        for record in data['features']:
            row = {
                "station_id":       record["properties"]["objectid"],
                "etat":             record["properties"]["etat"],
                "nb_velos_dispo":   record["properties"]["nb_velos_dispo"],
                "nb_places_dispo":  record["properties"]["nb_places_dispo"],
                "etat_connexion":   record["properties"]["etat_connexion"],
                "derniere_maj":     record["properties"]["date_modification"],
                "record_timestamp": timestamp
            }
            data_to_insert.append(row)
        self.client.insert_rows(table, data_to_insert)
        
    def query_data(self, query: str) -> list:
        query_job = self.client.query(query)
        return query_job.result()
    