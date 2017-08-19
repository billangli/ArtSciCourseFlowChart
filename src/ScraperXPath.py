"""
Scraper.py
Finds available courses from the UofT ArtSci calendar using XPath
I am confused so I will be using BeautifulSoup
Bill Li
Jul. 25th, 2017
"""

import requests
### Importing the required libraries
from lxml import html

### Getting data from the URL
"""tree will contain the entire HMTL file in a tree format"""
page = requests.get('https://fas.calendar.utoronto.ca/print/search-courses-print?')
tree = html.fromstring(page.content)


### Creating a Course class
class Course:
    'Contains info related to the course'

    def __init__(self, title, hours, description, prerequisite, corequisite, exclusion, distribution, breadth):
        self.title = self
        self.hours = hours
        self.description = description
        self.prerequisite = prerequisite
        self.corequisite = corequisite
        self.exclusion = exclusion
        self.distribution = distribution
        self.breadth = breadth

# Create a list of course names
course_titles = tree.xpath('//h3/text()')
course_hours = tree.xpath('//span[@class="views-field views-field-field-hours"]/span[@class="field-content"]/text()')
course_description = tree.xpath('//div[@class="views-field views-field-body"]/div[@class="field-content"]/p/text()')
course_prereq = tree.xpath(
    '//div[@class="views-field views-field-field-prerequisite1"]/div[@class="field-content"]/strong/text()')

### Print a list of the data
print('Course Names: ', course_titles)
print('Hours: ', course_hours)
print('\n'.join(course_description))
print(course_prereq)

print(len(course_titles))
print(len(course_hours))
print(len(course_description))
print(len(course_prereq))

# TODO: generate flowchart using pygraphviz