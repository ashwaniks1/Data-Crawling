#importing packages

from bs4 import BeautifulSoup
import requests
import pymysql

#connection to database
conn = pymysql.connect(host='10.103.92.251', user='virusplay', password='virusplay', database='virusplay')
cur = conn.cursor()

#function to store data


def store(ranking, name, url):

    cur.execute("INSERT INTO appbrain_data (ranking,name,url) values (%s,%s,%s)", (ranking, name, url))
    cur.connection.commit()

#source page


webpage = requests.get('https://www.appbrain.com/stats/google-play-rankings').text
soup = BeautifulSoup(webpage, 'html.parser')

# code to extract required data from html tags

# nested for loop is used to extract the data from the nested tags of html page


for s in soup.find_all('div', class_='data-table-container topmargin-m'):
    for category in s.table.tbody.findAll('tr'):
        ranking = category.td.text
        for app in category.findAll('td', {'class': 'ranking-app-cell'}):
            name = app.a.text
            url = app.a.get('href')
            store(ranking, name, url)
            print(ranking, name, url)

#database closed

conn.close()
cur.close()
