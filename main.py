if __name__ == '__main__':

 birthdays = {
    "Vincent Price": "5/27/1911",
    "Edgar Allan Poe": "1/19/1809",
    "Mary Shelley": "8/30/1797",
    "H.P. Lovecraft": "8/20/1890",
    "Stephen King": "9/21/1947"
    }

lst = birthdays.keys()

print('Welcome to my spooky birthday dictionary. I have the birthdays for these horror icons:\n')
for name in lst:
        print ('Vincent Price')
        print ('Edgar Allan Poe')
        print ('Mary Shelley')
        print ('H.P. Lovecraft')
        print ('Stephen King')
    

        choice = input('\nWhose birthday would you like to know?')
       
        if choice in birthdays:
            print('\n{}\'s birthday is {}.\n'.format(choice, birthdays[choice]))

        else:
          print('\nI\'m sorry, I don\'t know {}\'s birthday.\n'.format(choice))
