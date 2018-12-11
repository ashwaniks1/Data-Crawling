# ---- In this part, we extract the name and ranking of the apps, its developer name, category, ratings, and number of downloads available on www.appbrain.com.


from bs4 import BeautifulSoup
import requests
import pymysql


conn = pymysql.connect(host='10.103.92.251', user='virusplay', password='virusplay', database='virusplay')
cur = conn.cursor()


def store(content):

    cur.execute("INSERT INTO app_data (content) values (%s)", content)
    cur.connection.commit()


webpage = requests.get('https://www.appbrain.com/stats/google-play-rankings').text
soup = BeautifulSoup(webpage, 'html.parser')

# nested for loop is used to extract the data from the nested tags of html page

for s in soup.find_all('div', class_='data-table-container topmargin-m'):
    for c in s.table.tbody.findAll('tr'):
        content = c.text
        store(content)
        print(content)
        #for app in category.findAll('td', {'class': 'ranking-app-cell'}):
            #name = app.a.text
            #url = app.a.get('href')
            #store(ranking, name, url)
            #print(ranking, name, url)


conn.close()
cur.close()