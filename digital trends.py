# on this webpage only the name of the app with ranking is extracted. There is no docid or url available on www.digitaltrends.com for apps.

from bs4 import BeautifulSoup
import requests
import pymysql

conn = pymysql.connect(host='10.103.92.251', user='virusplay', password='virusplay', database='virusplay')
cur = conn.cursor()


def store(name, docid, url):

    cur.execute("INSERT INTO digitaltrends_data (name,docid,url) values (%s,%s,%s)", (name, docid, url))

    cur.connection.commit()

webpage = requests.get('https://www.digitaltrends.com/mobile/best-android-apps/2/').text
soup = BeautifulSoup(webpage, 'html.parser')


for s in soup.find_all('h2'):
    name = s.text
    docid = s.get('docid')
    url = s.get('href')
    store(name, docid, url)
    print(name, 'docid:',  docid, 'URL:', url)

    # docid and url will show none as they are not available on this webpage.

conn.close()
cur.close()