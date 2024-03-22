from flask import Flask,render_template, request
import pyodbc
from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'your password'
# app.config['MYSQL_DB'] = 'EmpData'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=EmpData;UID=DESKTOP-OPD33C4\oorwin;PWD=password')

@app.route("/demo")
def demo():
  return render_template("demo.html")

# mysql = MySQL(app)

@app.route("/form")
def form():
  if request.method == "POST":
    userDetails = request.form
    name = userDetails['name'] 
    email = userDetails['email']
    password = userDetails['password']
    gender = userDetails['gender']
    languages = userDetails['languages']
    courses = userDetails['courses']
    comments = userDetails['comments']

    cursor = cnxn.cursor();

    sql = "INSERT INTO empDetails(name, email, password, gender, languages, courses, comments) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (name, email, password, gender, languages, courses, comments))

    # cur.execute("insert into empdetails(name,email,password,gender,languages,courses,comments) values(%s %s %s %s %s %s %s)",(name,email,password,gender,languages,courses,comments))

  return render_template("form.html")
  
@app.route("/")
def index():
  return 'Hello World!'

if __name__ == '__main__':
  app.run()