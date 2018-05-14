#import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

targetURL = "https://www.reddit.com/"
#read interprets binary into human language
soup = bs(uReq(targetURL).read())
print(soup.prettify()) #prettify makes page pretty

for links in soup.findAll('a', attrs = {'data-event-action' : 'title'}): #prints only a tags - links one
    print(links.text)

