from exceptions import validateDate


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
        if validateDate(self.date):
            book_listing = str(f'{self.title},{self.author},{self.date},{self.rating}\n')
            file.write(book_listing)
        file.close()

    def case_2(self):
        search_title = self.title
        found_title = True
        file = open('record.txt')
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            if search_title in line[0]:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')
                found_title = True
                break
            else:
                found_title = False
        if not found_title:
            print('Not Found.')
        file.close()

    def case_3(self):
        search_author = self.author
        found_author = True
        file = open('record.txt')
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            if search_author in line[1]:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')
                found_author = True
            else:
                found_author = False
        if not found_author:
            print('Not Found.')
        file.close()

    def case_4(self):
        file = open('record.txt')
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')
        file.close()
