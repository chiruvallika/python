from flask import Flask,render_template,request,url_for,redirect, jsonify
import pyodbc

app  = Flask(__name__)


server = 'DESKTOP-OPD33C4\\SQLEXPRESS01'
database = 'companies_data'
username = 'sa'
password = 'Oorwin@123'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

@app.route('/')
def form():
    print("main route")
    cursor = cnxn.cursor()
    cursor.execute('select acc_id,acc_name from accounts')
    accounts = cursor.fetchall()
    cursor.close()
    return render_template('form.html',accounts = accounts)

@app.route('/add_account',methods=['POST'])
def add_account():
    acc_name = request.form['acc_name']
    cursor = cnxn.cursor()
    cursor.execute('select count(*) from accounts where acc_name = ?',acc_name)
    count = cursor.fetchone()[0]
    if count>0:
        print("account already exist")
    if acc_name and count==0:
        cursor = cnxn.cursor()
        cursor.execute('insert into accounts(acc_name) values(?)',acc_name)
        cnxn.commit()
        cursor.close()
    return  redirect(url_for('form'))

@app.route('/add_employee', methods=['POST'])
def add_employee():
    print("inside add employee")
    acc_id = request.form['accountID']
    print(acc_id)
    des_id = request.form['designation_id']
    emp_name = request.form['name'].capitalize()
    mobile_number = request.form['phone_number']
    try:
        if des_id and emp_name and mobile_number:
            cursor = cnxn.cursor()
            cursor.execute('INSERT INTO account_employee_details (acc_id, des_id, emp_name, mobile_number) VALUES (?, ?, ?, ?)', (acc_id, des_id, emp_name, mobile_number))
            cnxn.commit()
    except pyodbc.Error as e:
        print('Error:', e)
    finally:
        if 'cursor' in locals():
            cursor.close()

    return redirect(url_for('render_data_page'))


# @app.route('/add_employee', methods=['POST'])
# def add_employee():
#     print("inside add employee")
#     acc_id = request.form['accountID']
#     print(acc_id)
#     emp_name = request.form['name']
#     mobile_number = request.form['phone_number']
#     des_name = request.form['designation']  

#     des_id = None

#     try:
#         cursor = cnxn.cursor()

#         cursor.execute('SELECT des_id FROM designations WHERE designation = ?', (des_name,))
#         existing_des = cursor.fetchone()
        
#         if existing_des:
#             des_id = existing_des[0]
#         else:
            
#             cursor.execute('INSERT INTO designations (designation) VALUES (?)', (des_name,))
#             cnxn.commit()
#             des_id = cursor.lastrowid

#         if acc_id and des_id and emp_name and mobile_number:
#             cursor.execute('INSERT INTO account_employee_details (acc_id, des_id, emp_name, mobile_number) VALUES (?, ?, ?, ?)', (acc_id, des_id, emp_name, mobile_number))
#             cnxn.commit()
#             return redirect(url_for('render_data_page'))
#         else:
#             return jsonify({'error': 'Incomplete data provided'}), 400

#     except pyodbc.Error as e:
#         print('Error:', e)
#         return jsonify({'error': 'Internal server error'}), 500

#     finally:
#         if 'cursor' in locals():
#             cursor.close()


@app.route('/get_database_data')
def get_database_data():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 5, type=int)
    offset = (page - 1) * page_size
    cursor = cnxn.cursor()
    sql_query = f'''
    SELECT emp.emp_id, emp.acc_id, acc.acc_name, emp.emp_name, emp.mobile_number, emp.des_id, des.designation
    FROM account_employee_details emp
    JOIN accounts acc ON acc.acc_id = emp.acc_id
    JOIN designations des ON des.des_id = emp.des_id
    ORDER BY emp.emp_id desc
    OFFSET {offset} ROWS FETCH NEXT {page_size} ROWS ONLY
    '''
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    print(rows)
    data = []
    for row in rows:
        row_dict = {
            'emp_id': row[0],
            'acc_id': row[1],
            'acc_name': row[2],
            'emp_name': row[3],
            'mobile_number': row[4],
            'des_id': row[5],
            'designation': row[6]
        }
        data.append(row_dict)
    print(data)
    # Convert each Row object to a dictionary
    # data = [dict(zip(row.keys(), row)) for row in rows]
    cursor.execute('SELECT COUNT(*) FROM account_employee_details')
    total_records = cursor.fetchone()[0]
    total_pages = (total_records + page_size - 1) // page_size
    cursor.close()
    return jsonify(data=data, total_records=total_records, total_pages=total_pages)

@app.route('/delete_data',methods=['POST'])
def delete_data():
    del_id = request.form['del_id']
    print("del id ")
    print(del_id)
    cursor = cnxn.cursor()
    cursor.execute('delete from account_employee_details where emp_id = ?',(del_id))
    cursor.close()
    return redirect(url_for('get_database_data'))

# @app.route('/edit_data',methods=['post'])
# def edit_data():
#     emp_id = request.form.get('emp_id')
#     acc_id = request.form.get('acc_id')
#     des_id = request.form.get('des_id')
#     cursor = cnxn.cursor()
#     cursor.execute('select * from accounts where acc_id = ?',acc_id)
#     acc_data = cursor.fetchone()
#     print(acc_data)
#     cursor.execute('select * from designations where des_id = ?',des_id)
#     des_data = cursor.fetchone()
#     print(des_data)
#     cursor.execute('select * from account_employee_details where emp_id = ?',emp_id)
#     emp_data = cursor.fetchone()
#     print(emp_data)
#     cursor.close()

#     return render_template('form.html',acc_data=acc_data,des_data=des_data,emp_data=emp_data)

@app.route('/empId/<int:empId>/accId/<int:accId>/desId/<int:desId>',methods=['GET'])
def edit(empId,accId,desId):
    cursor = cnxn.cursor()
    cursor.execute('select * from accounts where acc_id = ?',accId)
    acc_data = cursor.fetchone()
    print(acc_data)
    cursor.execute('select * from designations where des_id = ?',desId)
    des_data = cursor.fetchone()
    print(des_data)
    cursor.execute('select * from account_employee_details where emp_id = ?',empId)
    emp_data = cursor.fetchone()
    print(emp_data)
    cursor.close()

    return render_template('form.html',acc_data=acc_data,des_data=des_data,emp_data=emp_data)
    

@app.route('/render_data', methods=['GET'])
def render_data_page():
    return render_template('showData.html')



# @app.route('/render_data',methods=['GET','POST'])
# def render_data():
#     page = request.args.get('page', 1, type=int)
#     page_size = request.args.get('page_size', 5, type=int)  
#     print(page_size)
#     offset = (page - 1) * page_size
#     cursor = cnxn.cursor()
#     sql_query = f'''
#     SELECT emp.emp_id,acc.acc_name, emp.emp_name, emp.mobile_number, des.designation
#     FROM account_employee_details emp
#     JOIN accounts acc ON acc.acc_id = emp.acc_id
#     JOIN designations des ON des.des_id = emp.des_id
#     ORDER BY emp.emp_id desc   
#     OFFSET {offset} ROWS FETCH NEXT {page_size} ROWS ONLY
#     '''
#     cursor.execute(sql_query)
#     data = cursor.fetchall()
#     print(data)
#     cursor.execute('SELECT COUNT(*) FROM account_employee_details')
#     total_records = cursor.fetchone()[0]
#     total_pages = (total_records + page_size - 1) // page_size
#     cursor.close()
#     return render_template('viewData.html',data=data,page=page, total_pages=total_pages,total_records=total_records)

@app.route('/employeeForm',methods=['post','get'])
def employeeForm():
    # acc_id = request.form.get('account_id')
    acc_id = request.form['account_id']
    print("account idd is")
    print(acc_id)
    cursor = cnxn.cursor()
    cursor.execute('select des_id,designation from designations')
    designations = cursor.fetchall()
    # print(designations)
    cursor.close()
    designations_list = [{'des_id': row[0], 'designation': row[1]} for row in designations]
    return jsonify(designations=designations_list,acc_id=acc_id)

@app.route('/add_designation',methods=['post'])
def add_designation():
    if request.method == 'POST':
        print("in add des")
        designation = request.form['designation']
        print(designation)
        acc_id = request.form['accountID']
        print("account id in des")
        print(acc_id)
        # emp_name = request.form['emp_name'] 
        # emp_phone = request.form['emp_phone']
        cursor = cnxn.cursor()
        cursor.execute('SELECT COUNT(*) FROM designations WHERE designation = ?', (designation,))
        count = cursor.fetchone()[0]

        if count>0:
            print('Designation already exists!', 'error')
            
        if designation and count==0:
            print("in designation insertion")
            cursor = cnxn.cursor()
            cursor.execute('insert into designations(designation) values(?)',designation)
            cnxn.commit()
            cursor.close()
            
        cursor = cnxn.cursor()
        cursor.execute('select des_id,designation from designations')
        designations = cursor.fetchall()
        cursor.close()
        designations_list = [{'des_id': row[0], 'designation': row[1]} for row in designations]
        print(designations_list)
        return jsonify(designations=designations_list,account_id=acc_id)
        return redirect(url_for('employeeForm'))
    
# @app.route('/insert_data',methods=[])
# def insert_data():

    
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)

