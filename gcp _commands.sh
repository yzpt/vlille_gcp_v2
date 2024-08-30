# V'lille GCP Dash

# config
PROJECT_ID=vlille-gcp-dash-yzpt
SERVICE_ACCOUNT_NAME=SA-$PROJECT_ID
SERVICE_ACCOUNT=$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com
BILLING_ACCOUNT=$(cat key-billing-account.txt)
BUCKET_NAME=gs://$PROJECT_ID-function
REGION_FUNCTION=europe-west9
DATASET_ID=vlille_dataset
PUBSUB_TOPIC=cloud-function-trigger-vlille
SCHEDULER_NAME=vlille-minute
SCHEDULER_LOCATION=europe-west1
TIMEZONE=Europe/Paris


# Creating a new gcloud project
gcloud projects create $PROJECT_ID

# Project activation
gcloud config set project $PROJECT_ID

# Creating a service account
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME --display-name "$PROJECT_ID service-account"

# Granting the least permissions (dataEditor) to the service account
# gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/bigquery.dataEditor"
# need the 'user' role to create jobs from bigquery client:
gcloud projects add-iam-policy-binding $PROJECT_ID --member="serviceAccount:$SERVICE_ACCOUNT" --role="roles/bigquery.user"

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
gcloud services enable eventarc.googleapis.com


# Creating a Pub/Sub topic: cloud-function-trigger-vlille
gcloud pubsub topics create $PUBSUB_TOPIC

# Creating a job scheduler that sends a message to the Pub/Sub topic every minute
gcloud scheduler jobs create pubsub $SCHEDULER_NAME --schedule="* * * * *" --topic=$PUBSUB_TOPIC --message-body="{Message from the $SCHEDULER_NAME Pub/Sub scheduler}" --time-zone=$TIMEZONE --location=$SCHEDULER_LOCATION --description="Scheduler every minute"

# function deploy
gsutil ls
# zip function's folder
cd function && zip -r ../function.zip . && cd ..
# upload function
gsutil cp function.zip $BUCKET_NAME
# deploy function
gcloud functions deploy vlille_api_extraction_v2 --runtime python310 --region $REGION_FUNCTION --trigger-topic $PUBSUB_TOPIC --source $BUCKET_NAME/function.zip --entry-point vlille_pubsub --gen2

