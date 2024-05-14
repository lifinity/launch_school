# loop on command
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    # solution made valid point; added for extra feedback
    print("Wrong. We're trapped here till you answer 'yes'.")
    
# run str.lower() on answer if you want diff caps vers to be acceptable