from flask import Flask, request, render_template, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # data = request.json
    # website_url = data['web_url']
    website_url='https://www.onetonline.org/find/industry?i=23'
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        print(rows)
    # print(table)

    print(website_url)

    return "done"
    

@app.route('/')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
