# venv function
python3 -m venv venv_vlille_function
source venv_vlille_function/bin/activate

pip install requests google-cloud-bigquery google-cloud-storage pytz

# function deploy
gsutil ls
BUCKET_NAME=gs://vlille-gcp-etl-function
# zip function's folder
cd function && zip -r ../function.zip . && cd ..
# upload function
gsutil cp function.zip $BUCKET_NAME
# deploy function
gcloud functions deploy vlille_api_extraction_v2 --runtime python311 --region $REGION_FUNCTION --trigger-topic $PUBSUB_TOPIC --source $BUCKET_NAME/function.zip --entry-point vlille_pubsub --gen2





### dev venv
python3 -m venv venv_vlille_dev
source venv_vlille_dev/bin/activate
pip install requests google-cloud-bigquery google-cloud-storage pytz google-cloud-bigquery-storage
pip install ipykernel pandas db-dtypes




## Dash Leaflet
pip install dash dash-leaflet dash-extensions dash-bootstrap-components

# upgrade ip pandas
pip install --upgrade pandas

