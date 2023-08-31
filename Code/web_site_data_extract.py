import requests
from bs4 import BeautifulSoup

def scrape_website(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  return soup

def extract_data(soup):
  data = []
  for article in soup.find_all('article'):
    title = article.find('h2').text
    url = article.find('a')['href']
    data.append({'title': title, 'url': url})
  return data

if __name__ == '__main__':
  url = 'https://www.example.com/'
  soup = scrape_website(url)
  data = extract_data(soup)
  print(data)