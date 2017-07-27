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
page = requests.get('https://fas.calendar.utoronto.ca/print/search-courses-print?')
tree = html.fromstring(page.content)

# Create a list of course names
course_titles = tree.xpath('//h3/text()')
course_hours = tree.xpath('//span[@class="views-field views-field-field-hours"]/span[@class="field-content"]/text()')

### Print a list of the data
print('Course Names: ', course_titles)
print('Hours: ', course_hours)

# TODO: generate flowchart using pygraphviz