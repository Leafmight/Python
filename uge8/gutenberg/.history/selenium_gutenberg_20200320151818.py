import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_info(name):
    base_url = 'http://www.gutenberg.org/'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    # search_field = browser.find_element_by_tag_name('input')
    search_field = browser.find_element_by_name('query')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)
    # browser.implicitly_wait(3)

    page_source = browser.page_source

    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('li', {'class': 'booklink'})
    
    entries_str = []
    for e in event_cells:
        print('cell: ',e)
        title = e.select('a>span>span')[0].text
        author = e.select('a>span>span')[1].text
        downloads = e.select('a>span>span')[2].text
       
        samlet = '{}\n{}\n{}\n'.format(title,author,downloads)
        #print(samlet)
        # print(element.text)
        entries_str.append(samlet)
    return entries_str

def save_to_file(content, out_path='./test.txt'):
    with open(out_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    entries = get_info('Møller')
    save_to_file('\n\n'.join(entries))