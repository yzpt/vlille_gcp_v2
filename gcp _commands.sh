# V'lille GCP Dash

# config
PROJECT_ID=vlille-gcp-dash-yzpt
SERVICE_ACCOUNT_NAME=SA-$PROJECT_ID
SERVICE_ACCOUNT=$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com
BILLING_ACCOUNT=$(cat key-billing-account.txt)
BUCKET_NAME=gs://$PROJECT_ID-function
REGION_FUNCTION=europe-west9
PUBSUB_TOPIC=cloud-function-trigger-vlille
DATASET_ID=vlille_dataset


# Creating a new gcloud project
gcloud projects create $PROJECT_ID

# Project activation
gcloud config set project $PROJECT_ID

# Creating a service account
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME --display-name "$PROJECT_ID service-account"

# Granting the least permissions (dataEditor) to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/bigquery.dataEditor"

# Granting the least permissions (storage.objectAdmin) to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/storage.objectAdmin"

# Creating a key for the service account
gcloud iam service-accounts keys create key-$PROJECT_ID.json --iam-account=$SERVICE_ACCOUNT

# Linking the billing account to the project
# retrieve billing account id:
gcloud billing accounts list
# set billing account
BILLING_ACCOUNT=$(cat key-billing-account.txt)
gcloud billing projects link $PROJECT_ID --billing-account=$BILLING_ACCOUNT


# Enabling APIs: Build, Run, Functions, Pub/Sub, Scheduler
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable pubsub.googleapis.com
gcloud services enable cloudscheduler.googleapis.com

# Creating a BigQuery dataset
bq mk $PROJECT_ID:$DATASET_ID
