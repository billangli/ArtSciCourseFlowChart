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

# Finding all courses
course_tags = soup.find("div", class_="view-content")
children = course_tags.findChildren(recursive=False)  # Finds direct children
num_courses = len(children)
print(num_courses)


### Creating a Course class
class Course:
    'Contains info related to the course'

    def __init__(self, html):
        self.info = {'title': '',
                     'hours': '',
                     'description': '',
                     'prerequisite': '',
                     'corequisite': '',
                     'exclusion': '',
                     'prep': '',
                     'distribution': '',
                     'breadth': ''}
        self.html = html


### Creating a Master List of All Courses
courses = []

info_tags = {
    'title': "views-field views-field-title",
    'hours': "views-field views-field-field-hours",
    'description': "views-field views-field-body",
    'prerequisite': "views-field views-field-field-prerequisite1",
    'corequisite': "views-field views-field-field-corequisite1",
    'exclusion': "views-field views-field-field-exclusion1",
    'prep': "views-field views-field-field-recommended1",
    'distribution': "views-field views-field-field-distribution-req",
    'breadth': "views-field views-field-field-breadth-req"}


print(children[0].prettify())
print(children[0].get_text())

print("\nTEST")
for key in info_tags:
    i = children[0].find(class_=info_tags[key])
    if i is not None and key != 'title' and key != 'description':
        i = i.find(class_="field-content")
        t = i.find(text=True, recursive=False)
    elif i is not None:
        t = i.get_text()
    print(t)