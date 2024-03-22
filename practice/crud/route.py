from flask import Flask,render_template, request,redirect,url_for,jsonify, Response
import pyodbc
import csv,io

app = Flask(__name__)

server = 'DESKTOP-OPD33C4\\SQLEXPRESS01'
database = 'employee_details'
username = 'sa'
password = 'Oorwin@123'
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+password+';Trusted_connection=no')

# create_table_query  = '''
#     create table users();
# '''

@app.route('/')
def userDetails():
    return render_template('userDetails.html',data="")

@app.route('/get_database_data',methods=['POST','GET'])
def get_databse_data():
    sort_column = request.form.get('sort')
    sort_order = request.form.get('order')
    search_val = request.form.get('search')
    page = request.form.get('pageInfo',1,type=int)
    itemsPerPage = request.form.get('itemsPerPage',5,type=int)
    offset = (page - 1)*itemsPerPage
    cursor = cnxn.cursor()
    if sort_order:
        if search_val:
            cursor.execute('select * from users_data where username like ? or gender like ? or contact like ? or email like ? or languages like ? order by {} {} offset ? rows fetch next ? rows only'.format(sort_column,sort_order),('%' + search_val + '%', '%' + search_val + '%','%' + search_val + '%', '%' + search_val + '%', '%' + search_val + '%', offset, itemsPerPage))
        else:
            cursor.execute('select * from users_data order by {} {} offset ? rows fetch next ? rows only'.format(sort_column,sort_order),offset,itemsPerPage)
    elif search_val:
        cursor.execute('select * from users_data where username like ? or gender like ? or contact like ? or email like ? or languages like ? order by id desc offset ? rows fetch next ? rows only', ('%' + search_val + '%', '%' + search_val + '%', '%' + search_val + '%', '%' + search_val + '%', '%' + search_val + '%',offset,itemsPerPage))
    else:
        cursor.execute('select * from users_data order by id desc offset ? rows fetch next ? rows only',(offset,itemsPerPage))
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
    if search_val:
        cursor.execute('select count(*) from users_data where username like ? or gender like ? or contact like ? or email like ? or languages like ?',('%' + search_val + '%', '%' + search_val + '%','%' + search_val + '%', '%' + search_val + '%', '%' + search_val + '%'))
    else:
        cursor.execute('select count(*) from users_data')
    count = cursor.fetchone()[0]
    return jsonify(data=data,total_rows=count)

@app.route('/submit',methods=['POST'])
def submit():
    formData = request.form
    username = formData['name'].capitalize()
    gender = formData['gender']
    contact = formData['contact']
    email = formData['email']
    languages_data = formData.getlist('language')
    languages = ",".join(languages_data)
    editID = formData.get('edit_id')
    print("submit form edit id")
    print(editID)
    cursor = cnxn.cursor()
    if editID:
        cursor.execute("update users_data set username = ?,gender = ?, contact = ?, email = ?,languages = ? where id = ?", (username,gender,contact,email,languages,editID))
    else:
        cursor.execute('insert into users_data(username,gender,contact,email,languages) values(?,?,?,?,?)',(username,gender,contact,email,languages))
    cnxn.commit()

    return render_template('viewFormData.html')

@app.route('/deleteData',methods=['POST'])
def deleteData():
    if request.method == 'POST':
        delete_id = request.form['del_id']
        cursor = cnxn.cursor()
        cursor.execute("delete from users_data where id=?",delete_id)
        cnxn.commit()
    else:
        return "Delete id not feteched."
    return redirect(url_for('get_databse_data'))


@app.route('/edit/<int:edit_id>',methods=['GET'])
def editData(edit_id):
    if request.method == 'GET':
        print(edit_id)
        cursor = cnxn.cursor()
        cursor.execute('select * from users_data where id = ?',edit_id)
        data = cursor.fetchone()
        print(data)
        return render_template('userDetails.html',data=data)

@app.route('/download/csv/<int:currPage>/<int:itemsPerPage>',methods=['GET'])
def download_report(currPage,itemsPerPage):
    cursor = cnxn.cursor()
    print("iin download")
    try:
        offset = (currPage - 1)*itemsPerPage
        cursor.execute('select * from users_data order by id desc offset ? rows fetch next ? rows only',(offset,itemsPerPage))
        result = cursor.fetchall()
        output = io.StringIO()
        writer = csv.writer(output)
        print(writer)
        heading = ['Id','Username','Gender','Contact','Email','Languages']
        writer.writerow(heading)
        for row in result:
            writer.writerow(row)
        output.seek(0)

        return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=emp_data.csv"})
    except Exception as e:
        print(e)
    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port=5001)