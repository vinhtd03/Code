import requests
from bs4 import BeautifulSoup as bs
from getpass import getpass

#user=input("Enter your username: ")
url='https://github.com/session'

s = requests.Session()
req =s.get(url).text

html = bs(req,"html.parser")
token = html.find("input", {"name":"authenticity_token"})['value']
com_val =html.find("input",{"name":"commit"})['value']

data = {
    'login_field':'v1nc3nt-03',
    'password':'v1nc3nt.vtd',
    'authenticity_token':token,
    'commit': com_val}
r1=s.post(url,data=data)

ans=bs(r1.content,"html.parser")


print(ans)

