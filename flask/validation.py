from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def userForm():
    return render_template('userForm.html')


user_data = {}
idx = 0


@app.route("/submit", methods=['POST', 'GET'])
def userDetails():
    if request.method == "POST":
        name = request.form['name']
        employeeID = request.form['employeeID']
        position = request.form['position']
        department = request.form['department']
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']
        address = request.form['address']
        global idx
        idx += 1
        data = {
            'index': idx,
            'name': name,
            'employeeID': employeeID,
            'position': position,
            'department': department,
            'email': email,
            'phoneNumber': phoneNumber,
            'address': address
        }
        user_data[idx] = data
        return render_template('userDetails.html', user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True)
