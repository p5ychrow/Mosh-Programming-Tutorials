#variables
help = '''  
start - to start the car 
stop - to stop the car 
quit - to exit game
'''
started = False #Status of car during game
command = '' #command input by user

while True:
    command = input().lower()
    if command == 'start':
        if started:
            print('The car is already running.')
        else:
            started = True
            print('Car is running. Vroom! Vroom!')
    elif command == 'stop':
        if not started:
            print('The car is already stopped.')
        else:
            started = False
            print('The car has stopped.')
    elif command == 'quit':
        break
    elif command == 'help':
        print(help)
    else:
        print('I do not understand.')