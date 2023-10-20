from flask import Flask, request, jsonify, render_template
import mysql.connector
import config

class SubscribeUser:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DB
        )
    def is_admin(self, email,entered_password):
        cursor = self.connection.cursor(buffered=True)
        query = "SELECT password FROM USER WHERE email = %s"
        cursor.execute(query, (email,))
        stored_password = cursor.fetchone()
        if stored_password is None or entered_password is None:
            return False
        if entered_password!=stored_password[0]:
            return False
        query = "SELECT isAdmin FROM USER WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return False 
    def subscribe(self):
        if request.method == 'POST':
            data = request.form
            if (data['user_email']!=data['email'] and not self.is_admin(data['user_email'],data['password'])) :
                return jsonify({'message': 'User Does not have permission'}), 403
            cursor = self.connection.cursor(buffered=True)
            query = "Select * FROM Subscribers WHERE email= %s"
            cursor.execute(query, (data['email'],))
            result = cursor.fetchone()
            if result is not None and result[2]==0:
                query = """ UPDATE Subscribers
                        SET isActive = TRUE
                        WHERE email = %s
                    """
                cursor.execute(query, (data['email'],))
                self.connection.commit()
                return jsonify({'message': 'Email Subscribed Again'}), 201
            query = """INSERT INTO Subscribers (email, first_name)
                        VALUES (%s, %s)"""

            cursor.execute(query, (data['email'], data['first_name'],))
            self.connection.commit()
            return jsonify({'message': 'Email Subscribed'}), 201

        return render_template('subscribe.html')

