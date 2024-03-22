
import requests
from bs4 import BeautifulSoup

url = 'https://h1bgrader.com/job-titles/software/lca/2024'


response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # table = soup.find('table')

    # table_data = []
    # for row in table.find_all('tr')[1:]: 
    #     columns = row.find_all('td')
    #     row_data = {
    #         'Comapny': columns[0].text,
    #         'Contact': columns[1].text,
    #         'Country': columns[2].text,
    #     }
    #     table_data.append(row_data)
    # print(table_data)
else:
    print("error")


