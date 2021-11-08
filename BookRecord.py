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
        book_listing = str(f'\'{self.title}\' \'{self.author}\' {self.date} {self.rating}\n')
        file.write(book_listing)
        file.close()

    def case_2(self):
        search_title = self.title
        file = open('record.txt', 'r')
        contents = file.read()
        lines = file.readlines()

        for line in lines:
            return f'Line {line.strip()}'
            # if entry.__contains__(search_title):
            #     return entry[:]
            # else:
            #     return 'Not found.'
        file.close()

    def case_3(self):
        search_author = self.author
        file = open('record.txt')
        contents = file.read()
        file.close()

        for entry in file:
            if entry.__contains__(search_author):
                return entry[:]
            else:
                return 'Not found.'
        file.close()

    def case_4(self):
        return 'Display all books.'

    def case_5(self):
        return 'Quit'
