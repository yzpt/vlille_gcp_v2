import base64
from datetime import datetime
from google.cloud import bigquery
import requests
import pytz
import os

class Config:
    PROJECT_NAME = 'vlille-gcp-etl'
    DATASET_ID = 'vlille_dataset'
    TABLE_ID = 'records'
    GOOGLE_CREDENTIALS = "key-" + PROJECT_NAME + ".json"
    API_URL = ('https://data.lillemetropole.fr/geoserver/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0'
               '&TYPENAMES=dsp_ilevia%3Avlille_temps_reel&OUTPUTFORMAT=application%2Fjson')
    TIMEZONE = 'Europe/Paris'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Config.GOOGLE_CREDENTIALS

class TimeService:
    @staticmethod
    def get_current_time_in_timezone(timezone: str):
        tz = pytz.timezone(timezone)
        return datetime.now(tz)

class APIService:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()

class BigQueryService:
    def __init__(self, project_name: str, dataset_id: str, table_id: str):
        self.client = bigquery.Client(project=project_name)
        self.dataset_id = dataset_id
        self.table_id = table_id

    def insert_data(self, data: dict, timestamp: str):
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

class VLilleETL:
    def __init__(self, config: Config):
        self.api_service        = APIService(config.API_URL)
        self.bigquery_service   = BigQueryService(config.PROJECT_NAME, config.DATASET_ID, config.TABLE_ID)
        self.timezone           = config.TIMEZONE

    def execute(self):
        current_time            = TimeService.get_current_time_in_timezone(self.timezone)
        timestamp               = current_time.strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            json_data = self.api_service.fetch_data()
            print("Data extracted from API")
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        try:
            self.bigquery_service.insert_data(json_data, timestamp)
            print("Data inserted into BigQuery")
        except Exception as e:
            print(f"Error inserting data into BigQuery: {e}")
            return

def vlille_pubsub(event, context):
    etl = VLilleETL(Config)
    etl.execute()

if __name__ == "__main__":
    vlille_pubsub('data', 'context')
