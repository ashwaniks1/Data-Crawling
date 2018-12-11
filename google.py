#importing packages

from bs4 import BeautifulSoup
import requests
import pymysql

#connection to database
conn = pymysql.connect(host='10.103.92.251', user='virusplay',password='virusplay',database='virusplay')
cur = conn.cursor()

#fuction to store data


def store(name, docid, url):

    cur.execute("INSERT INTO google_data (name,docid,url) values (%s,%s,%s)", (name, docid, url))

    cur.connection.commit()

#source page


webpage = requests.get('https://play.google.com/store/apps/collection/topselling_free').text
soup = BeautifulSoup(webpage, 'html.parser')

# code to extract required data from html tags
for s in soup.findAll('div', {'class': 'card no-rationale square-cover apps small'}):
    name = s.div.div.a.get('aria-label')
    docid = s.get('data-docid')
    url = s.a.get('href')
    store(name, docid, url)
    print(name, 'docid:',  docid, 'URL:', url)

#database closed
conn.close()
cur.close()