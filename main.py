from BookRecord import SelectOption as So

inputSelection = int(input('Enter your selection: '))
while inputSelection != 5:
    # Initialize switch
    switch = So()

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
        switch.option(inputSelection)
        break

    inputSelection = int(input('\nEnter your selection: '))
