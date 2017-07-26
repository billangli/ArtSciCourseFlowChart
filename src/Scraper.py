"""
Scraper.py
Finds available courses from the UofT ArtSci calendar 
Bill Li
Jul. 25th, 2017
"""

### Importing the required libraries
from lxml import html
import requests

### Getting data from the URL
"""tree will contain the entire HMTL file in a tree format"""
page = requests.get('http://calendar.artsci.utoronto.ca/crs_mat.htm')
tree = html.fromstring(page.content)

# Create a list of course names
course_names = tree.xpath('//span[@class="strong"]/text()')

### Print a list of the data
print('Course Names: ', course_names)

# TODO: generate flowchart using pygraphviz