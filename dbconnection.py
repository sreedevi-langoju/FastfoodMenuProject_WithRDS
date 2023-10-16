import boto3
import mysql.connector

def connect_database():
    try:
        # Initialize a Boto3 client for SSM
        ssm_client = boto3.client('ssm')

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
