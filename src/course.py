"""
Course.py
A class that holds the information for a course
Bill Li
Aug. 22nd, 2017
"""


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
info_tags = {'code': '',
    'title': "views-field views-field-title",
    'hours': "views-field views-field-field-hours",
    'description': "views-field views-field-body",
    'prerequisite': "views-field views-field-field-prerequisite1",
    'corequisite': "views-field views-field-field-corequisite1",
    'exclusion': "views-field views-field-field-exclusion1",
    'prep': "views-field views-field-field-recommended1",
    'distribution': "views-field views-field-field-distribution-req",
    'breadth': "views-field views-field-field-breadth-req"}
