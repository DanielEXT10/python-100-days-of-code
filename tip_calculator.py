

print('Welcome to the tip calculator!')

while True:
    bill = float(input('What was the total bill: '))

    if bill > 0 and bill < 1000000:
        break
    else:
        print('Insert a valid value')

while True:
    
    tip_percentage = float(input('what percentage of the total bill do you want the tip to be: '))
    if tip_percentage > 0 and tip_percentage < 100:
        break 
    else:
        print('Insert a valid tip percentage')

number_people= int(input('How many people to split the bill?: '))

def calculate_tip(bill, percentage, people):
    tip_percentage= percentage/100
    tip=bill*tip_percentage
    total = bill + tip
    pay_by_person = total/people

    print('Total bill + tip is: ' + f'{total:.2f}')
    print('Each person should pay: $' + f'{pay_by_person:.2f}')
 
calculate_tip(bill, tip_percentage, number_people)
