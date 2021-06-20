import mysql.connector
import configparser
import os

c = configparser.ConfigParser()
c.read(os.getenv('CONFIG_FILE'))

'''
This script programmatically connects to GCP CloudSQL instance
Creates a database and table
'''

config = {
    'user': c['CLOUDSQL']['cloud_sql_user'],
    'password': c['CLOUDSQL']['cloud_sql_password'],
    'host': c['CLOUDSQL']['cloud_sql_host']
}

''' Establish connection  '''
conn = mysql.connector.connect(**config)
cursor = conn.cursor()  # initialize connection cursor

''' Create a new databse '''
cursor.execute('CREATE DATABASE demo_db')  # create a new database

''' Verify database creation '''
cursor.execute('SHOW DATABASES;')
result = cursor.fetchall()
print(result)

''' Use database '''
cursor.execute('USE demo_db;')

''' Create a new table '''
cursor.execute("CREATE TABLE songs ("
               "song_id INT NOT NULL AUTO_INCREMENT,"
               "title VARCHAR(255),"
               "artist VARCHAR(255),"
               "genre VARCHAR(255),"
               "PRIMARY KEY(song_id) );")

# conn.commit()

''' Verify new table creation '''
cursor.execute('SHOW tables;')
result = cursor.fetchall()
print(result)

conn.close()