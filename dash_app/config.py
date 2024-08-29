class Config:
    PROJECT = 'vlille-gcp-etl'
    DATASET = 'vlille_dataset'
    TABLE_RECORDS = 'records'
    TABLE_STATIONS = 'stations'
    GOOGLE_CREDENTIALS = "key-" + PROJECT + ".json"
    API_URL = 'https://data.lillemetropole.fr/geoserver/wfs?SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=dsp_ilevia%3Avlille_temps_reel&OUTPUTFORMAT=application%2Fjson'
    TIMEZONE = 'Europe/Paris'