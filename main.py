from BookRecord import SelectOption

count = 0
inputSelection = int(input('Enter your selection: '))
while count < 5:
    # Initialize switch
    switch = SelectOption('', '', '', '')

    if inputSelection == 1:
        inputTitle = input('Enter Title: ')
        inputAuthor = input('Enter Author: ')
        inputDate = input('Enter Date Read: ')
        inputRating = input('Enter Rating: ')
        switch = SelectOption(inputTitle, inputAuthor, inputDate, inputRating)
        switch.option(1)

    elif inputSelection == 2:
        # inputTitle = input('Enter Title: ')
        # switch = SelectOption(inputTitle, '', '', '')
        print(switch.option(2))

    elif inputSelection == 3:
        inputAuthor = input('Enter Author Name: ')
        switch = SelectOption('', inputAuthor, '', '')
        print(switch.option(3))

    inputSelection = int(input('Enter your selection: '))
    count += 1
