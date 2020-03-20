import bs4
import requests


r = requests.get('http://www.gutenberg.org/ebooks/search/?query=sherlock+holmes+conan')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

print(soup.prettify()[:1500])