from email import header
import requests
from bs4 import BeautifulSoup

mail = input("Enter the email address: ")


dta = {
    "email": mail
}
header = {
    "referer": "https://www.verifyemailaddress.org/"
}
r = requests.post('https://www.verifyemailaddress.org/email-validation-result',headers=header, data=dta)
htmlContent = r.content
# print(r)
soup = BeautifulSoup(htmlContent, 'html.parser')

resultSec = soup.find('section', id="result")

# print(soup.contents)
result_success = resultSec.find('li', class_="success valid")
result_failure = resultSec.find('li', class_="failure")

# print(result_success)
# print(result_failure)
if(result_success is not None):
    print(result_success.contents)
else:
    print(result_failure.contents)