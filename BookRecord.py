"""
Author: Jared Paubel
Date: 11/08/2021
WIP: Fix condition 3's output; does not output if correct.
"""

class SelectOption:
    def option(self, selection):
        default = 'Incorrect selection.'

        return getattr(self, 'case_' + str(selection), lambda: default)()

    def __init__(self, title='', author='', date='', rating=''):
        self.title = title
        self.author = author
        self.date = date
        self.rating = rating

    def case_1(self):
        file = open('record.txt', 'a')
        book_listing = str(f'{self.title}, {self.author}, {self.date}, {self.rating}\n')
        file.write(book_listing)
        file.close()

    def case_2(self):
        search_title = self.title
        file = open('record.txt')
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            if line[0] == search_title:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}')
        file.close()

    # FIXME Does not output if correct
    def case_3(self):
        search_author = self.author
        file = open('record.txt')
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            print(line[1])
            if line[1] == search_author:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}')
        file.close()

    # HELPME Finish rest of case conditions
    def case_4(self):
        return 'Display all books.'

    def case_5(self):
        return 'Quit'
