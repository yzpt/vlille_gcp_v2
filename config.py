class Config:
    PROJECT_ID = 'vlille-gcp-etl'
    DATASET_ID = 'vlille_dataset_v2'
    RECORDS_TABLE_ID = 'records'
    STATIONS_TABLE_ID = 'stations'
    GOOGLE_CREDENTIALS = "key-" + PROJECT_ID + ".json"
    API_URL = 'https://data.lillemetropole.fr/geoserver/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=dsp_ilevia%3Avlille_temps_reel&OUTPUTFORMAT=application%2Fjson'
    TIMEZONE = 'Europe/Paris'