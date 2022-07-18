from pydoc import describe
import requests
from bs4 import BeautifulSoup


num = input('Enter the number: ')

if len(num)!=10:
    print('invalid input')
    exit()

dta = {
    "mobilenumber" : str(num),
    "submit" : "Trace"
}


r = requests.post('https://www.findandtrace.com/trace-mobile-number-location', data=dta)
# print(r, type(r), r.content)
htmlContent = r.content


# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)

# print(list(soup.children))

# print(soup.find('table'))

ttl = soup.find('title')
# if soup.find('title', contents='404 NOT FOUND'):
#     print("exiting")
#     exit()

print(ttl.contents[0].string)

if '404' in ttl.contents[0].string:
    print('Not found')

x = soup.find('table', class_='shop_table')

# x = soup.find('div', class_='col-md-4')
# print(x)

# print(x.find('tr', contents=' LIVE - Active '))
i = 1
for th in x.find_all('tr'):
    if i==6:
        if 'Active' in th.contents[1].string:
            print(th.contents[1].string)
    i = i + 1
# print(soup.find("meta", content="404 NOT FOUND"))


# print(soup.find('table', class_='table table-hover table-condensed'))