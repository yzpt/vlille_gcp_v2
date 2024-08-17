# config
PROJECT_ID=vlille-gcp-etl
SERVICE_ACCOUNT=admin-vlille-gcp-etl@vlille-gcp-etl.iam.gserviceaccount.com
BILLING_ACCOUNT=$(cat key-billing-account.txt)
BUCKET_NAME=gs://vlille-gcp-etl-function
REGION_FUNCTION=europe-west9
PUBSUB_TOPIC=cloud-function-trigger-vlille



# V'lille GCP v2

# Config 
PROJECT_ID=vlille-gcp-etl

# Creating a new gcloud project
gcloud projects create $PROJECT_ID

# List projects
gcloud projects list

# Project activation
gcloud config set project $PROJECT_ID

# Creating a service account
gcloud iam service-accounts create admin-$PROJECT_ID --display-name "Admin $PROJECT_ID"

# List service accounts
gcloud iam service-accounts list
# admin-vlille-gcp-v2@vlille-gcp-v2.iam.gserviceaccount.com
SERVICE_ACCOUNT=admin-vlille-gcp-etl@vlille-gcp-etl.iam.gserviceaccount.com

# Granting permissions (bigquery admin) to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/bigquery.admin"

# Granting permissions (storage admin) to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/storage.admin"

# Creating a key for the service account
gcloud iam service-accounts keys create key-$PROJECT_ID.json --iam-account=$SERVICE_ACCOUNT

# Linking the billing account to the project
gcloud billing accounts list
BILLING_ACCOUNT=$(cat key-billing-account.txt)
gcloud billing projects link $PROJECT_ID --billing-account=$BILLING_ACCOUNT



# Enabling APIs: Build, Functions, Pub/Sub, Scheduler
gcloud services enable cloudbuild.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable pubsub.googleapis.com
gcloud services enable cloudscheduler.googleapis.com

# Creating a BigQuery dataset
bq mk $PROJECT_ID:dataset

bq ls vlille_dataset


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


