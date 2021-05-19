# make sure to add geckodriver and chromedriver to PATH.

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.espn.com/nba/scoreboard/_/date/20210516")

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

for tag in soup.find_all("td", {"class":"total"}):
    print (tag.text)

for tag in soup.find_all("td", {"class":"home"}):
    print (tag.text)

for tag in soup.find_all("td", {"class":"away"}):
    print (tag.text)

# Find how to index home and away with scores.