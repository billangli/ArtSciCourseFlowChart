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


# Creating a Course class
class Course:
    """Contains info related to the course"""

    def __init__(self):
        self.info = {'code': '',
                     'title': '',
                     'hours': '',
                     'description': '',
                     'prerequisite': '',
                     'corequisite': '',
                     'exclusion': '',
                     'prep': '',
                     'distribution': '',
                     'breadth': ''}

    def department(self):
        return self.info['code'][:3]

    def level(self):
        return self.info['code'][3:6]


# Creating a Master List of All Courses
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

# Extracting the text from the html tags
for child in children:
    # # Debugging
    # print(child.prettify())
    # print("\nExtracting information from the html tags")

    c = Course()
    for key in info_tags:
        t = None
        i = child.find(class_=info_tags[key])

        if i is not None:
            if key == 'title':
                i = i.find("h3")
                t = i.get_text()
            elif key == 'description':
                i = i.findChildren(recursive=False)[0]
                i = i.findChildren(recursive=False)[0]
                t = i.get_text()
            else:
                i = i.find(class_="field-content")
                t = i.find(text=True, recursive=False)

        # Storing the information
        if t is not None:
            c.info[key] = t

    c.info['code'] = c.info['title'][:8]
    courses.append(c)

for i, c in enumerate(courses):
    print("\n %s" % (i + 1))
    for info_name in c.info:
        print("%s: %s" % (info_name, c.info[info_name]))
