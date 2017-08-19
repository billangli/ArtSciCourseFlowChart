"""
Scraper.py
Finds available courses from the UofT ArtSci calendar using BeautifulSoup
Bill Li
Jul. 25th, 2017

BeautifulSoup Tutorial
http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
"""

# Importing the required libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

r = urlopen('https://fas.calendar.utoronto.ca/print/search-courses-print?').read()
soup = BeautifulSoup(r, "lxml")
print(type(soup))

print(soup.prettify())

# Finding all courses
tag = soup.find("div", class_="view-content")
str = str(tag)
print(str[0:1000])

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

courses = []

# Parsing the courses
# TODO: parse the courses by tranversing through the text