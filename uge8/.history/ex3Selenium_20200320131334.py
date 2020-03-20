from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://www.gutenberg.org/ebooks/search/?query=sherlock+holmes+conan')
browser.implicitly_wait(3)

link_to_next = browser.find_elements_by_link_text('Next')
link_to_next[0].click()