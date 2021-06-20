import os
import mysql.connector
from flask import jsonify

''' This is the backend API functionality for the app '''

config = {
    'user': os.getenv('cloud_sql_user'),
    'password': os.getenv('cloud_sql_password'),
    'database': os.getenv('cloud_sql_db'),
    'unix_socket': os.getenv('cloud_sql_conn_name')
}

''' Insert data into db '''
def add_data(json_obj):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = ('INSERT INTO songs (title, artist, genre) VALUES(%s, %s, %s);')
    data = (json_obj['title'], json_obj['artist'], json_obj['genre'])
    cursor.execute(query, data)
    conn.commit()
    conn.close()

''' Get data from db '''
def get_data():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT * from songs;')
    result = cursor.fetchall()
    if len(result) > 0:
        got_data = jsonify(result)
    else:
        got_data = "No records in db"
    conn.close()
    return got_data
