import requests
from bs4 import BeautifulSoup


num = input('Enter mobile number --> ')
r = requests.get('https://bmobile.in/' + num)
htmlContent = r.content

# print(htmlContent)

# parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# print(list(soup.children))

# print(soup.find('table'))

x = soup.find('table', class_='table table-hover table-condensed') # table displayed when no. is present
y = soup.find('div', class_='alerttext')

if x is None:  
    if "not found" in y.string:
        print("No. not found")
else:
    print("Number Valid")
    # print(x.find_all('td', class_='dtls'))
    # th = x.find('td', class_='dtls', string=" " + num)

    th = x.find('a', href=True)
    print("The Operator for this number is:", th.string)

    # for location
    i = 1
    for thloc in x.find_all('tr'):
        if i==3:
            # if 'Active' in thloc.contents[1].string:
            #     print(th.contents[1].string)
            print("The Location of this number is:",thloc.contents[1].string)
        i = i + 1

# print(soup.find_all("title"))
# print(soup.find('div', class_='alerttext').string)