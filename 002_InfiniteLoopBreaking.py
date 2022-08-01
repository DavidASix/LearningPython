while True:
    areWeDone = input('Input the word \'done\' to finish the loop: ')
    if areWeDone == 'done':
        break # Exit Loop
    elif areWeDone == 'never':
        print('Never Say Never - Justin Bieber')
        continue # Stop here and enter new iteration
    print('Please end the loop!')
