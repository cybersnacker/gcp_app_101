### Environment setup
Ensure that the packages/dependencies listed in requirements.txt are installed on the compute machine where the scripts below would be executed. 

### Setting up CloudSQL & App Engine
1. These steps are for first time creation. Create a CloudSQL database by in GCP by choosing the type (ex: PostgreSQL, MySQL, MSSQL), compute, region, memory
2. (Optional) Create a new user other than root.
3. We will use the public IP address of the instance. Allowlist IP addresses that will be accessing this database (ex: your computer's public IP address, GCP VM instance). Do this by going to Connections tab -> Add Network and type in your IP address in the Network box.
4. Verify that any app that is in the project that needs access to this instance has access to the CloudSQL instance
5. Verify that the project ID is correct by running `gcloud config list`. If project ID is empty, set it by running `gcloud config set project PROJECT__ID`
6. Create an App Engine with a configuration of your choice

### Setup the DATABASE and TABLES
1. These steps are for first time creation. Run setup_db.py to create database and tables with appropriate schema. setup_db.py requires an environment variable for configuration file that contains config information for the database in a format friendly to the config parser. 
2. setup_db.py needs to be run either from your local computer or a GCP VM/compute engine whose IP address has been placed in the allowlist of the database. 

### Define backend & app API endpoints
1. db.py creates the backend functionality associated with the API
2. main.py is the Flask app that creates API endpoints
3. An app.yaml file is necessary to deploy an app on GCP to set up the environment. An example file looks like this
```
runtime: python37

env_variables:
  cloud_sql_user: 'val1'
  cloud_sql_password: 'val2'
  cloud_sql_host: val3
  cloud_sql_conn_name: 'val4'
  cloud_sql_db: 'val5'

```
4. Type `gcloud app deploy` to deploy the app, GCP will automatically deploy the app and provide a URL to view the app. The app can also be accessed by typing `gcloud app browse`
