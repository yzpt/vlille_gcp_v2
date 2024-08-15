# V'lille GCP v2

# Config 
PROJECT_ID=vlille-gcp-v2

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
SERVICE_ACCOUNT=admin-vlille-gcp-v2@vlille-gcp-v2.iam.gserviceaccount.com

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

