from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
  return 'Hello World!'

@app.route("/demo")
def demo():
  return render_template("demo.html")

if __name__ == '__main__':
  app.run()