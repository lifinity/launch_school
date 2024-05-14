# match-case
animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')       
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

# prints 'neigh' b/c val of animal matches case 'horse'