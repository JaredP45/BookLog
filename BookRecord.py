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
        with open('record.txt', 'a') as file:
            if validateDate(self.date):
                book_listing = str(f'{self.title},{self.author},{self.date},{self.rating}\n')
                file.write(book_listing)

    def case_2(self):
        search_title = self.title
        found_title = False

        with open('record.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.split(',')
            if search_title in line[0]:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')
                found_title = True

        if not found_title:
            print('Not Found.')

    def case_3(self):
        search_author = self.author
        found_author = False

        with open('record.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.split(',')
            if search_author in line[1]:
                print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')
                found_author = True

        if not found_author:
            print('Not Found.')

    def case_4(self):
        with open('record.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.split(',')
            print(f'{line[0]}, by {line[1]}, Read {line[2]}, Rating {line[3]}', end='')

    def case_5(self):
        search_title = self.title

        with open('record.txt', 'r') as file:
            lines = file.readlines()

        with open('record.txt', 'w') as file:
            for line in lines:
                if search_title not in line.strip('\n'):
                    file.write(line)

        print(f'Deleted {search_title}')
