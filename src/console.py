"""
Console.py
Takes in user instructions from the console
Bill Li
Aug. 22nd, 2017
"""

from src.scraper import Scraper


print("--- Welcome to the Arts and Science Course Flow Chart ---")


def main_menu():
    print("Enter 0 to load the course calendar")
    print("Enter 1 to update the course calendar from the UofT website")
    choice = input()
    if choice == "0":
        load_calendar()
    elif choice == "1":
        update_calendar()


def load_calendar():
    print("Loading course calendar from text file")
    s = Scraper()
    s.load()


def update_calendar():
    print("Updating course calendar from UofT website")
    s = Scraper()
    s.update()


# Running the main menu
main_menu()
