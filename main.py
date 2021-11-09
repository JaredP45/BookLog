from BookRecord import SelectOption as So

count = 0
inputSelection = int(input('Enter your selection: '))
while count < 5:
    # Initialize switch
    switch = So('', '', '', '')

    if inputSelection == 1:
        inputTitle = input('Enter Title: ')
        inputAuthor = input('Enter Author: ')
        inputDate = input('Enter Date Read: ')
        inputRating = input('Enter Rating: ')
        switch = So(inputTitle, inputAuthor, inputDate, inputRating)
        switch.option(inputSelection)
        count += 1

    elif inputSelection == 2:
        inputTitle = input('Enter Title: ')
        switch = So(title=inputTitle)
        switch.option(inputSelection)

    elif inputSelection == 3:
        inputAuthor = input('Enter Author Name: ')
        switch = So(author=inputAuthor)
        switch.option(inputSelection)

    inputSelection = int(input('Enter your selection: '))
