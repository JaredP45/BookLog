from BookRecord import SelectOption as So

# Create switch instance
switch = So()
end_program = False

inputSelection = int(input('Enter your selection: '))
while inputSelection != 5 or end_program == True:

    if inputSelection == 1:
        inputTitle = input('Enter Title: ')
        inputAuthor = input('Enter Author: ')
        inputDate = input('Enter Date Read: ')
        inputRating = input('Enter Rating: ')
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
        end_program = True

    print('\n 1. Enter a book\n',
          '2. Search for a book\n',
          '3. Search for an author\n',
          '4. Display all books\n',
          '5. Exit')

    inputSelection = int(input('Enter your selection: '))

print('Thanks for using this application!')