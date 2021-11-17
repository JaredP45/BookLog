from BookRecord import SelectOption as So

if __name__ == '__main__':
    # Create switch instance
    switch = So()
    inputSelection = 0

    while inputSelection != 6:

        print('\n 1. Enter a book\n',
              '2. Search for a book\n',
              '3. Search for an author\n',
              '4. Display all books\n',
              '5. Delete a book\n',
              '6. Exit\n')

        try:
            inputSelection = int(input('\nEnter your selection: '))
        except ValueError:
            print('\nYou must enter a number.\n')
            inputSelection = 0

        if inputSelection == 1:
            inputTitle = input('Enter Title: ')
            inputAuthor = input('Enter Author: ')
            inputDate = input('Enter Date Read (mm-dd-yyyy): ')
            inputRating = int(input('Enter Rating: '))

            while inputRating < 0 or inputRating > 10:
                print('You must enter rating score in range of 0 to 10.')
                inputRating = int(input('\nEnter Rating: '))
            switch = So(inputTitle, inputAuthor, inputDate, inputRating)
            switch.option(inputSelection)

        elif inputSelection == 2:
            inputTitle = input('Enter Title: ')
            switch = So(title=inputTitle)
            switch.option(inputSelection)

        elif inputSelection == 3:
            inputAuthor = input('Enter Author Name: ')
            switch = So(author=inputAuthor)
            switch.option(inputSelection)

        elif inputSelection == 4:
            switch.option(inputSelection)

        elif inputSelection == 5:
            inputTitle = input('Delete Title: ')
            switch = So(title=inputTitle)
            switch.option(inputSelection)

        elif inputSelection == 6:
            break

    print('Thanks for using this application!')
