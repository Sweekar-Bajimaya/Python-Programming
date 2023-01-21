import random
import string
def temppass(Email):
   temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
   member_table[Email] = temp_password
   return temp_password
random_question_list = ['What is your favourite household appliance?',
                       'What is your favourite security question?',
                       'Which race do you hate the most?']
member_table = {}
security_question = {}

print('Press (z) to stop entering email')

while True:
   email = input('Enter email: ')
   if email.lower() == 'z':
       break
   password = input('Enter password: ')
   squestion = random.choice(random_question_list)
   print(squestion)
   sanswer = input(': ')
   member_table[email] = password
   security_question[email] = (squestion, sanswer)
print('\nLOGIN')c = True
while c:
   usrEmail = input('Enter your email: ')
   if usrEmail in member_table:
       usrPassword = input('Enter your password: ')
       sysPassword = member_table[usrEmail]
       if usrPassword == sysPassword:
           print('You are now logged in to your account')
           c = False
       else:
           print('Incorrect password')
           print(security_question[usrEmail][0])
           usrSanswer = input(': ')
           sysSanswer = security_question[usrEmail][1]
           if usrSanswer == sysSanswer:
               newTempPass = temppass(usrEmail)
               print('Your new password is: ', newTempPass)
               c = False
           else:
               print('Incorrect')
               continue
   else:
       print('Email does not exist!')
       continue