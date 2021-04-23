print('welcome,what will you like to do today?')
print('1.login')
print('2.register')
welcome = int(input(" "))

if(welcome == 1):
  name = input("what is your name? \n")
  allowedusers = ('iyi','semi','mike')
  allowedpassword = 'passwordiyi','passwordsemi','passwordmike'
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
        print('3.transfer funds')
        print('4. Complaint')


        selectedOption =int(input('please select an option:'))

        if(selectedOption == 1):

            selectedAmount = int(input('How much would you like to withdraw:'))
            print('please take your cash')

        elif (selectedOption == 2):
            cashDeposit =int(input('How much would you like to deposit? '))
            print('your balance is #%s' %cashDeposit )

        elif(selectedOption == 3):
         print('how much would you like to transfer?')
         transfer = int(input(''))
         print('enter recipent account number')
         recieve =input('')
         print('enter your pin')
         int(input())
         print('transfer of #%s is succesful' %transfer )
        elif (selectedOption == 4):
                    cashDeposit = (input(' What issue will you like to report? '))
                    print("Thank you for contacting us")

        else:
            print('invalid option selected,please try again')
    else:
        print('password incorrect, please try again')
if (welcome == 2):
 print('enter your full name' )
 name = input()
 print('enter your phone number')
 phone = int(input())
 print('enter your email adress')
 email = input()
 print('create a pin')
 pin = int(input())

 import random
 def generation_account_number():
     return random.randrange(1111111111, 9999999999)


 account_number = generation_account_number()
 print(account_number)

