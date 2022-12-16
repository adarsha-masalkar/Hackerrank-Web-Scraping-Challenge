from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/'

movies_list = []

next_url = ['search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc']


def page(c):
    curr_url = url + c
    response = requests.get(curr_url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('h3.lister-item-header a')
    runtime = soup.select('span.runtime')
    id1 = soup.select('span.lister-item-index')

    for a, b, c in zip(movies, runtime, id1):
        movies_list.append((c.get_text()[:-1], a.get_text(), b.get_text()))

    next1 = soup.select('a.lister-page-next')[0]
    next_url.append(next1.get('href'))


cur = 0
for i in next_url:
    if cur <= 170:
        page(i)
        print('Scraped page no. ', cur)
        cur += 1
    else:
        movies_list.sort(key=lambda x: float(x[2][:-4]), reverse=True)
        for i in movies_list:
            if 1000 <= int(i[0].replace(',', '')) <= 8000:
                print(i)
                exit()
