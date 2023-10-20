from flask import Flask, request, jsonify
import mysql.connector
import config

class getEmails:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DB
        ) 
    def getAllEmails(self):
        cursor = self.connection.cursor(buffered=True)
        cursor.execute('SELECT email FROM Subscribers where isActive=True')

        data = cursor.fetchall()
        cursor.close()
        return data
