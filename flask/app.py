from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("form.html")


@app.route("/user")
def greet():
    return "hello"


@app.route("/passed/<int:score>")
def passed(score):
    return "You have passed with a score: "+str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "You have failed with a score: "+str(score)


@app.route("/result/<int:marks>")
def result(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "passed"
    # return redirect(url_for(result, score=marks))
    return render_template("result.html", result=result)


@ app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        english = float(request.form['english'])
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        total_score = (english+maths+science)/3
    return redirect(url_for("result", marks=total_score))


if __name__ == '__main__':
    app.run(debug=True)
