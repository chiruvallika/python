from flask import Flask,render_template,request,redirect,url_for, jsonify, Response
import pyodbc 
import pandas as pd
import csv


app = Flask(__name__)

server = 'DESKTOP-OPD33C4\\SQLEXPRESS01'
database = 'employee_details'
username = 'sa'
password = 'Oorwin@123'
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+password+';Trusted_Connection=no')

# create_table_query = '''
# CREATE TABLE users (
#     id INT IDENTITY(1,1) PRIMARY KEY,
#     username VARCHAR(50) not null,
#     gender VARCHAR(50) not null,
#     contact VARCHAR(50) not null ,
# );
# '''

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        userDetails = request.form
        updateID = userDetails['update']
        username = userDetails['name'].capitalize()
        gender = userDetails['gender']
        contact = userDetails['contact']
        cursor = cnxn.cursor()
        # cursor.execute(create_table_query)
        # cursor.execute('''ALTER TABLE users ADD email varchar(50) ;''')
        # cursor.execute('''ALTER TABLE users ADD languages varchar(100);''')
        if updateID:
            cursor.execute("update users set username = ?,gender = ?, contact = ? where id = ?", (username,gender,contact,updateID))
        else:
            sql = "INSERT INTO users(username, gender, contact) VALUES (?, ?, ?)"
            cursor.execute(sql, (username, gender, contact))
        cnxn.commit()
        
        return redirect(url_for('viewTableData'))
    
def is_id_present(user_id):
    cursor = cnxn.cursor()
    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    if row:
        return True
    else:
        return False
    
@app.route('/viewTableData')
def viewTableData():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM users order by id desc")
    data = cursor.fetchall()
    return render_template('viewTableData.html', data=data)

@app.route('/addDetails')
def addDetails():
    return render_template('addDetails.html',data="")
    
@app.route('/addOtherDetails',methods=['POST'])
def addOtherDetails():
    if request.method=='POST':
        userDetails = request.form
        updateID = userDetails['update']
        username = userDetails['name']
        username = username.capitalize()
        gender = userDetails['gender']
        contact = userDetails['contact']
        email = userDetails['email']
        languages_str = userDetails.getlist('language')  
        languages = ",".join(languages_str)
        cursor = cnxn.cursor()
        # cursor.execute(create_table_query)
        # cursor.execute('''ALTER TABLE users ADD email varchar(50) ;''')
        # cursor.execute('''ALTER TABLE users ADD languages varchar(100);''')
        if updateID:
            cursor.execute("update users set username = ?,gender = ?, contact = ?, email = ?,languages = ? where id = ?", (username,gender,contact,email,languages,updateID))
            cnxn.commit()
        else:
            sql = "INSERT INTO users(username, gender, contact, email, languages) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql, (username, gender, contact, email, languages))
            cnxn.commit()
        
        return redirect(url_for('viewTableData'))
    
@app.route('/deleteData',methods=['POST'])
def deleteData():
    if request.method == 'POST':
        user_id = request.form['del_id']
        if user_id:
            cursor = cnxn.cursor()
            cursor.execute('''delete from users where id = ?''',user_id)
            cnxn.commit()
        else:
            return "unable to fetch user id"
    return redirect(url_for('viewTableData'))

@app.route('/editData', methods=['POST'])
def editData():
    user_id = request.form['edit_id']
    email_val = request.form['email_val']
    if email_val == 'None':
        email_val=""
    if email_val:
        if is_id_present(user_id):
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            data=cursor.fetchone()
            return render_template('addDetails.html',data=data)
    else:
        if user_id:
            if is_id_present(user_id):
                cursor = cnxn.cursor()
                cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
                data=cursor.fetchone()
                return render_template('empForm.html',data=data)
@app.route('/viewRowData',methods=['POST'])
def viewData():
    viewrow_id = request.form['viewrow_id']
    if viewrow_id:
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (viewrow_id,))
        rowData = cursor.fetchone()
        return render_template('viewRowData.html',rowData=rowData)

@app.route('/')
def empForm():
    return render_template('empForm.html',data="")

@app.route('/get_data',methods=['GET','POST'])
def get_data():
    page = request.form.get('page', 1, type=int)
    search = request.form.get('search')
    # print(search)
    # print(page)
    sortOrder = request.form.get('sortOrder')
    sortColumn = request.form.get('sortColumn')
    per_page = request.form.get('items_per_page',5,type=int)
    # print(per_page)
    offset = (page - 1) * per_page

    try:
        cursor = cnxn.cursor()
        if search:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username LIKE ? OR gender LIKE ? OR contact LIKE ? OR email LIKE ? OR languages LIKE ?", ('%' + search + '%', '%' + search + '%','%' + search + '%', '%' + search + '%', '%' + search + '%'))
        else:
            cursor.execute("SELECT COUNT(*) FROM users")
        total_rows = cursor.fetchone()[0]
        if search:
            print("in if blk")
            if sortOrder:
                cursor.execute("SELECT * FROM users WHERE username LIKE ? OR gender LIKE ? OR contact LIKE ? OR email LIKE ? OR languages LIKE ? ORDER BY {} {} OFFSET ? ROWS FETCH NEXT ? ROWS ONLY".format(sortColumn, sortOrder),
            ('%' + search + '%', '%' + search + '%','%' + search + '%', '%' + search + '%', '%' + search + '%', offset, per_page))
                print("sort search exec")
            else:
                print("in search else block")
            
                cursor.execute("SELECT * FROM users WHERE username LIKE ? OR gender LIKE ? OR contact LIKE ? OR email LIKE ? OR languages LIKE ? ORDER BY id DESC OFFSET ? ROWS FETCH NEXT ? ROWS ONLY",
                ('%' + search + '%', '%' + search + '%','%' + search + '%', '%' + search + '%', '%' + search + '%',  offset, per_page))
        elif sortOrder:
            print("in else-if blk")
            cursor.execute("SELECT * FROM users ORDER BY {} {} OFFSET ? ROWS FETCH NEXT ? ROWS ONLY".format(sortColumn, sortOrder),offset, per_page)

        else:
            print("in else blk")
            cursor.execute("SELECT * FROM users ORDER BY id desc OFFSET ? ROWS FETCH NEXT ? ROWS ONLY", offset, per_page)
        
        rows = cursor.fetchall()

        data = []
        for row in rows:
            row_dict = {
                'id': row.id,
                'username': row.username,
                'gender': row.gender,
                'contact': row.contact,
                'email': row.email,
                'languages': row.languages
            }
            data.append(row_dict)
        # cursor.execute('select count(*) from users')
        # count = cursor.fetchone()[0]
        # print(rows[0])
        cursor.close()
        return jsonify(data=data, total_rows=total_rows)
    except Exception as e:
        return jsonify({"error": str(e)})

    
import io

# @app.route('/download/report/csv')
# def download_report():
#     cursor = cnxn.cursor()
#     try:
#         cursor.execute("SELECT * FROM users")
#         result = cursor.fetchall()

#         output = io.StringIO()
#         writer = csv.writer(output)

#         line = ['Id', 'Username', 'Gender', 'Contact', 'Email', 'Languages']
#         writer.writerow(line)

#         for row in result:
#             writer.writerow(row)

#         output.seek(0)

#         return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=employee_report.csv"})
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()

@app.route('/download/csv/<int:currPage>/<int:items_per_page>')
def downloadCsv(currPage,items_per_page):
    cursor = cnxn.cursor()
    try:
        cursor.execute('select * from users order by id desc offset ? rows fetch next ? rows only',(currPage,items_per_page))
        rows = cursor.fetchall()
        result = io.StringIO
        writer = csv.writer(result)
        line = ['Id','Username','Gender','Contact','Email','Languages']
        writer.writerow(line)
        for row in rows:
            writer.writerow(row)
        result.seek(0)
        return Response(result, mimetype="text/csv", headers={"Content-Description":"attachment;filename=employee_data.csv"})
    except Exception as e:
        print(e)
    finally:
        cursor.close()



if __name__ == '__main__':
  app.run(debug=True, host = '127.0.0.1',port=5000)
