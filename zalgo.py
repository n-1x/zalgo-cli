#Author: Nicholas J D Dean
#Date created: 2017-12-02
import random

#take the given string and add <addsPerChar> unicode
#combining characters after each character.
def zalgo(string, addsPerChar):
    result = ''

    for char in string:
        #add the additions to the character
        for i in range(0, addsPerChar):
            randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
            char += randBytes.decode('utf-16be')

        #add the character and its additions
        #to the final result
        result += char

    return result



#keep asking for input with <inputString> until a valid int is given
def intInput(inputString):
    result = -1
    valid = False

    while not valid:
        try:
            result = int(input(inputString)) #throws ValueError

            #wont run if exception is thrown
            valid = True
        except ValueError as e:
            print('Invalid input.')

    return result



#accept only a valid integer character or 0, which
#is used to identify there being no limit.
def charLimitInput(minLimit):
    charLimit = 0
    valid = False

    #receive a valid char input
    while not valid:
        charLimit = intInput('Character limit [0 for no limit, min ' + 
            str(minLimit) + ']: ')

        #valid if 0 or >= minimum
        if (charLimit == 0) or (charLimit >= minLimit):
            valid = True

        if not valid:
            print('Invalid character limit.')

    return charLimit



string = input('Initial string: ')

#the user can't select a limit less than twice
#the size of the string. This is to ensure that
#each character has at least one addition.
charLimit = charLimitInput(len(string) * 2)
    
addsPerChar = 0

#ask for the adds per char. else if they chose a limit
#then use the maximum possible per char without going
#over the limit
if charLimit == 0:
    addsPerChar = intInput('Number of additions per char: ')
else:
    addsPerChar = (charLimit - len(string)) // len(string)

amountWanted = intInput('Amount to generate: ')

#run the function the requested number of times
#and format the output
for i in range(0, amountWanted + 1):
    print(zalgo(string, addsPerChar), end='')

    #TODO: Change number of columns based on string size

    #print in 3 tabbed columns
    if ((i+1) % 3 == 0):
        print()
    else:
        print('\t', end='')

print()