#This file is helps to create database and Tables 

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, List, Dict, Any


# mysql_connection = mysql.connector.connect(
#                 host="DESKTOP-T5HOJK9",
#                 user="root@localhost",
#             password="Developer@22"
#             )



import mysql.connector

# Replace with your database and table names
database_name = "Appointment"
table_name = "appointments"

# MySQL server connection configuration
config = {
    "host": "localhost",
    "user": "root",
    "password": "Developer@22"
}

# Create a connection to the MySQL server
connection = mysql.connector.connect(**config)

# Create a cursor to execute SQL commands
cursor = connection.cursor()

try:
    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    # Use the database
    cursor.execute(f"USE {database_name}")

    # Create the table if it doesn't exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        number VARCHAR(20),
        doctor VARCHAR(255),
        time DATETIME,
        category VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()
    print(f"Database '{database_name}' and table '{table_name}' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    connection.close()
