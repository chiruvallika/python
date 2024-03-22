from flask import Flask , request,render_template
from flask_mysqldb import MySQL

app=Flask(__name__) 


app.config['MYSQL_DATABASE_USER'] ="sa" 
app.config['MYSQL_DATABASE_PASSWORD'] = "Oorwin@123" 
app.config['MYSQL_DATABASE_DB'] ="employee_details" 
app.config['MYSQL_DATABASE_HOST'] = "localhost" 
mysql = MySQL(app) 



@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        userDetails = request.form
        name = userDetails['name']
        gender = userDetails['gender']
        contact = userDetails['contact']
        cursor = mysql.connection.cursor()
        # sql = "INSERT INTO empDetails(name, gender, contact) VALUES (?, ?, ?)"
        # cursor.execute(sql, (name, gender, contact))
        cursor.execute(''' INSERT INTO employees VALUES(%s,%s,%s)''',(name,gender,contact))
        mysql.connection.commit()
    return "Data inserted succesfully"

@app.route('/')
def empForm():
    return render_template('empForm.html')



if __name__ == '__main__':
  app.run(host='localhost',debug=True)