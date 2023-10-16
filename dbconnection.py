import os
import boto3
import mysql.connector

# Set the AWS region via an environment variable
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

def connect_database():
    try:
        # Retrieve the AWS region from the environment variable
        aws_region = os.environ.get('AWS_DEFAULT_REGION')

        # Initialize a Boto3 client for SSM with the specified region
        ssm_client = boto3.client('ssm', region_name=aws_region)

        # Fetch parameter values from Parameter Store
        db_host = ssm_client.get_parameter(Name='/fastfood/dbconfig/db_host', WithDecryption=True)['Parameter']['Value']
        db_user = ssm_client.get_parameter(Name='/fastfood/dbconfig/db_user', WithDecryption=True)['Parameter']['Value']
        db_password = ssm_client.get_parameter(Name='/fastfood/dbconfig/db_password', WithDecryption=True)['Parameter']['Value']
        db_database = ssm_client.get_parameter(Name='/fastfood/dbconfig/db_database', WithDecryption=True)['Parameter']['Value']

        # Database configuration
        db_config = {
            'host': db_host,
            'user': db_user,
            'password': db_password,
            'database': db_database
        }

        # Connect to the MariaDB server
        connection = mysql.connector.connect(**db_config)

        return connection
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None
