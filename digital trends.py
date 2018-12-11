# on this webpage only the name of the top free android apps (Dec 2018) with ranking is extracted which is available on www.digitaltrends.com for apps.

from bs4 import BeautifulSoup
import requests
import pymysql

conn = pymysql.connect(host='10.103.92.251', user='virusplay', password='virusplay', database='virusplay')
cur = conn.cursor()


def store(name):

    cur.execute("INSERT INTO digitaltrends_data (name) values (%s)", name)

    cur.connection.commit()


webpage = requests.get('https://www.digitaltrends.com/mobile/best-android-apps/2/').text
soup = BeautifulSoup(webpage, 'html.parser')


for s in soup.find_all('div', {'class': 'h-multistitch-content-wrap'}):
    for t in s.find_all('h2'):
        name = t.text
        store(name)
        print(name)

    # no docid and url available on this webpage.

conn.close()
cur.close()