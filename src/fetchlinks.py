#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import logging
import os
import traceback
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

os.environ['WEBPAGE_LINKCLASS_CONFIG'] = 'chapternav-link'
WEBPAGE_LINKCLASS = os.environ['WEBPAGE_LINKCLASS_CONFIG']

def extractLinks(url: str, linkclass: str):
    """This method will scrawl over and extracts the url links present in the given web page
    :return: list of url links associated to the given class
    """
    links = []
    try:
        # Set headers to spoof as a standard mozilla useragent
        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        logger.debug(f'\nContent from the given web page::::::::\n{soup.prettify()}')

        for link in soup.find_all("a", class_=linkclass):
            links.append(link.get('href'))
        if len(links) == 0:
            for link in soup.find_all("a"):
                links.append(link.get('href'))
    except RuntimeError:
        logger.info(f'\nUnexpected runtime error occured while fetching the data from the given web page: \n{traceback.format_exc()}')
        
    return links

def getWebpageLinks():
    """
        logs all the url links extracted from the given web page    
    """
    links = []
    try:
        links = extractLinks(sys.argv[1], WEBPAGE_LINKCLASS)
        if len(links) > 0: 
            for link in links:
                logger.info(f"\nlink:{link}")
        else:
            logger.info(f"\nthere are no links found in the given website")
    except RuntimeError:
        logger.info(f'\nUnexpected runtime error occured while retrieving the required link references from the given webpage: \n{traceback.format_exc()}')


if __name__ == "__main__":
    getWebpageLinks()


