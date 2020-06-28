import time

###############################

def start_menu():
    time.sleep(1)
    start_choice = input('Start? (y/n)  ')
    if start_choice == ('y'):
        choose_menu()
    else:
        start_menu()

def choose_menu():
    print('1. Sum')
    print('2. Substraction')
    print('3. Multiplication. ')
    print('4. Division')
    choose = input('Choose your operation: ')
    if choose == ('1'):
        sum()
    elif choose == ('2'):
        subs()
    elif choose == ('3'):
        mult()
    elif choose == ('4'):
        div()
        
##############################

def sum():
    num1 = float(input('-> '))
    print('   + ')
    num2 = float(input('-> '))
    resSum = (num1 + num2)
    print('= ', resSum)
    while input:
        True
        sum()
        continue
    if num1 == ('back'):
        choose_menu()

def subs():
    num1 = float(input('-> '))
    print('  - ')
    num2 = float(input('-> '))
    resSubs = (num1 - num2)
    print('= ',  resSubs)
    while input:
        True
        subs()
        continue
    if num1 == ('back'):
        choose_menu()

def mult():
    num1 = float(input('-> '))
    print('  x ')
    num2 = float(input('-> '))
    resMult = (num1 * num2)
    print('= ',  resMult)
    while input:
        True
        mult()
        continue
    if num1 == ('back'):
        choose_menu()

def div():
    num1 = float(input('-> '))
    print('  ÷ ')
    num2 = float(input('-> '))
    resDiv = (num1 / num2)
    print('= ',  resDiv)
    while input:
        True
        div()
        continue
    if num1 == ('back'):
        choose_menu()

###############################

print(' C A L C U L A T O R ')
start_menu()
