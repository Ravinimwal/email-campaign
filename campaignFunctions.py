from flask import Flask, request, jsonify
import mysql.connector
import config
from unsubscribe import UnsubscribeUser
from getemails import getEmails
from addSubscribers import SubscribeUser
UnsubscribeUser= UnsubscribeUser()
SubscribeUser= SubscribeUser()
getEmails=getEmails()
app = Flask(__name__)
app.config.from_object(config)

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)


@app.route('/subscribe', methods=['GET','POST'])
def addUser():
    return SubscribeUser.subscribe()

@app.route('/unsubscribe', methods=['GET','POST'])
def removeUser():
    return UnsubscribeUser.unsubscribe()




if __name__=='__main__':
    app.run()