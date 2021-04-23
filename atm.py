print('welcome,what will you like to do today?')
print('1.login')
print('2.register')
welcome = int(input(" "))

if(welcome == 1):
  name = input("what is your name? \n")
  allowedusers = ('iyi','semi','mike')
  allowedpassword = 'passwordiyi','passwordsemi','passwordseyi'
  if(name in allowedusers):
    password = input("your password? \n")
    userId  = allowedusers.index(name)

    import datetime

    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    if(password == allowedpassword[userId]):
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. create a new account')

        selectedOption =int(input('please select an option:'))

        if(selectedOption == 1):

            selectedAmount = int(input('How much would you like to withdraw:'))
            print('please take your cash')

        elif (selectedOption == 2):
            cashDeposit =int(input('How much would you like to deposit? '))
            print('your balance is #%s' %cashDeposit )

        elif (selectedOption == 3):
                    cashDeposit = (input(' What issue will you like to report? '))
                    print("Thank you for contacting us")

        else:
            print('invalid option selected,please try again')
    else:
        print('password incorrect, please try again')
if (welcome == 2):
 print('enter your full name' )
 input()
 print('enter your phone number')
 int(input())
 print(int('create a password'))
 import random

 print("Generating Account Number")
 retur = random.randint(1111111111,9999999999)
 print(retur)
