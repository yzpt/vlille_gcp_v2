from datetime import datetime
import requests
import pytz
import os

from config import Config
from bigqueryservice import BigQueryService

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Config.GOOGLE_CREDENTIALS

class TimeService:
    @staticmethod
    def get_current_time_in_timezone(timezone: str) -> datetime:
        tz = pytz.timezone(timezone)
        return datetime.now(tz)

class APIService:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self) -> dict:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()

class VLilleETL:
    def __init__(self, config: Config):
        self.api_service        = APIService(config.API_URL)
        self.bigquery_service   = BigQueryService(config.PROJECT_NAME, config.DATASET_ID, config.TABLE_ID)
        self.timezone           = config.TIMEZONE

    def execute(self) -> None:
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

def vlille_pubsub(event, context) -> None:
    etl = VLilleETL(Config)
    etl.execute()

if __name__ == "__main__":
    vlille_pubsub('data', 'context')
