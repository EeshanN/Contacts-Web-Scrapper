import requests
from bs4 import BeautifulSoup

num = input('Enter mobile number --> ')

dta = {
    "submit": "true",
    "search" : str(num),
    "submit" : "Trace"
}
r = requests.post('https://www.findandtrace.com/trace-std-landline-number', data=dta)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')


x = soup.find('table', class_='shop_table')
y = soup.find('div', class_='col-md-4')
# print(y.contents[3].string)

if x is None:
    if '404' in y.contents[3].string:
        print('Not found')
else:
    i = 1
    for th in x.find_all('tr'):
        if i==6:
            if 'Live' in th.contents[1].string:
                print(th.contents[1].string)
        i = i + 1




