from flask import Flask, render_template, session, url_for
from flask import jsonify, request
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
from werkzeug.utils import redirect
import mysql.connector
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="user",
    passwd="Kesha123@ms",
    database="parkway"
    )
#mycursor = mydb.cursor()
mycursor = mydb.cursor(buffered=True)


@app.route('/', methods=['GET', 'POST'])
def test():
    return "render_template('/login.html')"




@app.route('/success/<name>')
def success(name):
   if name == 'wrong':
       return 'Invalid Username password'
   return "success"


@app.route('/login', methods=['POST'])
def login():
   data = request.json
   user = data['username']
   password = data['password']
   #cur = mysql.connection.cursor()
   mycursor.execute("Select username,password from user where username = %s and password=%s", (user, password))
   mydb.commit()
   tabledata = mycursor.fetchone()
   if tabledata:
       return redirect(url_for('success', name=tabledata))
   else:
       return redirect(url_for('success', name="wrong"))


if __name__ == '__main__':
    app.run(debug=True)