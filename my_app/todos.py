import requests
from bs4 import BeautifulSoup


url = 'https://jsonplaceholder.typicode.com/todos'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}
response = requests.get(url=url, headers=headers)




# from bs4 import BeautifulSoup
# import requests

# rs = requests.get('https://jsonplaceholder.typicode.com/todos')
# root = BeautifulSoup(rs.content, 'html.parser')

# for todo in root.select('#page-content p'):
#     print(p.get_text(strip=True))