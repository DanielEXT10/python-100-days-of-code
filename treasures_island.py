print('Welcome to Treasure Island. Your mission is to find the treasure.')

flag = False
while True:
    if flag: break
    decision1 = input('Which way we should go, left or right?: ')
    if decision1 == 'rigth':
        print('Game Over')
        break
    elif decision1 == 'left':
        while True:
            if flag: break
            decision2 = input('We should, swim or walk?: ')
            if decision2 == 'swim':
                print('Game Over')
                break
            elif decision2 == 'walk':
                while True:
                    if flag: break
                    decision3 = input('Which door do you want to open, red, blue or yellow?: ')
                    if decision3 == 'red' or decision3 == 'blue':
                        print('Game Over')
                        break
                    elif decision3 == 'yellow':
                        print('You Win,thanks for playing!')
                        flag = True
                        break
            
                    else:
                        print('Insert a valid option')

            else:
                print('Insert a Valid option')
    else:
        print('Insert a valid option')

print('Treasure Island 2022')
                

