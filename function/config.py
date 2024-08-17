class Config:
    PROJECT_NAME = 'vlille-gcp-etl'
    DATASET_ID = 'vlille_dataset'
    TABLE_ID = 'records'
    GOOGLE_CREDENTIALS = "key-" + PROJECT_NAME + ".json"
    API_URL = ('https://data.lillemetropole.fr/geoserver/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=dsp_ilevia%3Avlille_temps_reel&OUTPUTFORMAT=application%2Fjson')
    TIMEZONE = 'Europe/Paris'