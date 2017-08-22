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
from src import course
from src.course import Course


class Scraper:
    def __init__(self):
        print("Running the scraper")
        self.url = 'https://fas.calendar.utoronto.ca/print/search-courses-print?'
        self.file_name = 'courseInfo.txt'
        self.courses = []

    def clear_courses(self):
        self.courses = []

    def update(self):
        print("Running the scraper update method")
        self.clear_courses()
        r = urlopen(self.url).read()
        soup = BeautifulSoup(r, "lxml")
        print(type(soup))

        # Finding all courses
        course_tags = soup.find("div", class_="view-content")
        children = course_tags.findChildren(recursive=False)  # Finds direct children
        num_courses = len(children)
        print(num_courses)

        # Extracting the text from the html tags
        file = open(self.file_name, 'w', encoding='utf-8')
        file.write(f"{num_courses}\n")
        for child in children:
            # # Debugging
            # print(child.prettify())
            # print("\nExtracting information from the html tags")

            c = Course()
            for key in course.info_tags:
                if key != 'code':
                    t = None
                    i = child.find(class_=course.info_tags[key])

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

                    # Storing the information in the program
                    if t is not None:
                        c.info[key] = t

                        # Storing the information in a text file
                        file.write("%s\n" % t)

            c.info['code'] = c.info['title'][:8]
            self.courses.append(c)

        file.close()

    def load(self):
        print("Running the scraper load method")
        # Deleting all the courses
        self.clear_courses()

        # Reading the text file for the course info
        file = open(self.file_name, 'r', encoding='utf-8')
        num_courses = int(file.readline())
        print("%s courses found" % num_courses)

        for i in range(num_courses):
            c = Course()
            for index, key in enumerate(c.info):
                line_number = i * len(c.info) + index + 1  # Finding the line number based on course and info
                c.info[key] = file.readline(line_number)
            self.courses.append(c)

        # Debugging
        for info_name in course.info_tags:
            print("%s: %s" % (info_name, self.courses[400].info[info_name]))
