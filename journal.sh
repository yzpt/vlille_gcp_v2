# venv function
python3 -m venv venv_vlille_function
source venv_vlille_function/bin/activate

pip install requests google-cloud-bigquery google-cloud-storage pytz


### dev venv
python3 -m venv venv_vlille_dev
source venv_vlille_dev/bin/activate
pip install requests google-cloud-bigquery google-cloud-storage pytz google-cloud-bigquery-storage
pip install ipykernel pandas db-dtypes




## Dash Leaflet
pip install dash dash-leaflet dash-extensions dash-bootstrap-components

# upgrade pip pandas
pip install --upgrade pandas

